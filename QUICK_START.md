# VeighNa 快速入门 (macOS 版)

## 脚本运行
除了使用图形化启动方式外，在 macOS 上建议使用针对 Mac 优化的启动脚本。

我们在根目录下创建了 `run.py`，它支持：
1. **富途证券 (FutuGateway)**：支持港股、美股和 A 股通。
2. **CTA 策略应用**：完整的 CTA 策略投研和实盘模块。
3. **CTA 回测模块**：在本地进行策略历史回溯分析。

### 示例代码 (run.py)

```python
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy_futu import FutuGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp

def main():
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # 添加富途网关 (Futu)
    main_engine.add_gateway(FutuGateway, gateway_name="FUTU")
    
    # 添加应用模块 (CTA)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()

if __name__ == "__main__":
    main()
```

### 运行步骤

1. **环境准备**：
   确保已安装相关插件：
   ```bash
   pip install vnpy_futu vnpy_ctastrategy vnpy_ctabacktester
   ```

2. **启动程序**：
   在项目根目录下运行：
   ```bash
   python run.py
   ```

3. **连接富途**：
   请确保你的电脑上已经启动并登录了 **FutuOpenD** 或 **Futu API** 客户端，否则无法完成行情连接。
