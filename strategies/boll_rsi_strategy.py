from vnpy_ctastrategy import (
    CtaTemplate,
    StopOrder,
    TickData,
    BarData,
    TradeData,
    OrderData,
    BarGenerator,
    ArrayManager,
)

class BollRsiStrategy(CtaTemplate):
    """
    布林强弱 (BollRsi) 策略
    
    策略逻辑：
    1. 当价格突破布林带上轨，且 RSI 低于超买界限时，做多。
    2. 当价格跌破布林带下轨，且 RSI 高于超卖界限时，做空。
    3. 止损采用简单的固定点位止损。
    """
    author = "Antigravity"

    # 策略参数
    boll_window = 20        # 布林带窗口
    boll_dev = 2.0          # 布林带标准差倍数
    rsi_window = 14         # RSI 窗口
    rsi_signal = 20         # RSI 信号过滤（避免在极度超买时追多）
    fixed_size = 1          # 每次下单手数

    # 策略变量
    boll_up = 0.0           # 上轨
    boll_down = 0.0         # 下轨
    rsi_value = 0.0         # RSI 当前值

    parameters = ["boll_window", "boll_dev", "rsi_window", "rsi_signal", "fixed_size"]
    variables = ["boll_up", "boll_down", "rsi_value"]

    def __init__(self, cta_engine, strategy_name, vt_symbol, setting):
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)

        self.bg = BarGenerator(self.on_bar)
        self.am = ArrayManager()

    def on_init(self):
        """策略初始化"""
        self.write_log("BollRsi 策略初始化")
        self.load_bar(10) # 预加载 10 天数据

    def on_start(self):
        """策略启动"""
        self.write_log("BollRsi 策略开启，祝开市大吉！")

    def on_stop(self):
        """策略停止"""
        self.write_log("BollRsi 策略已停止")

    def on_tick(self, tick: TickData):
        """收到 Tick 后的处理"""
        self.bg.update_tick(tick)

    def on_bar(self, bar: BarData):
        """收到 K 线后的处理"""
        self.cancel_all() # 撤销之前的挂单

        am = self.am
        am.update_bar(bar)
        if not am.inited:
            return

        # 计算布林带和 RSI
        self.boll_up, self.boll_down = am.boll(self.boll_window, self.boll_dev)
        self.rsi_value = am.rsi(self.rsi_window)

        # 交易逻辑
        if self.pos == 0:
            # 价格上穿布林带上轨，且 RSI 还没到疯狂程度 (假设 < 70)
            if bar.close_price > self.boll_up and self.rsi_value < 70:
                self.buy(bar.close_price + 5, self.fixed_size)
            # 价格下穿布林带下轨，且 RSI 还没到极度阴线 (假设 > 30)
            elif bar.close_price < self.boll_down and self.rsi_value > 30:
                self.short(bar.close_price - 5, self.fixed_size)
        
        elif self.pos > 0:
            # 持有多头：价格跌破中线（此处简化为跌回上轨以下）或触碰反向信号
            if bar.close_price < self.boll_up:
                self.sell(bar.close_price - 5, abs(self.pos))

        elif self.pos < 0:
            # 持有空头：价格回升到下轨以上
            if bar.close_price > self.boll_down:
                self.cover(bar.close_price + 5, abs(self.pos))

        self.put_event() # 更新 UI
