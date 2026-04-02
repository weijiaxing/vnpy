#!/usr/bin/env python3
"""
VeighNa Trader 启动脚本 (macOS 兼容版)
=====================================

本脚本提供了一个在 macOS 上运行 VeighNa 的示例，主要针对：
1. 移除不支持 Mac 的 CTP 网关
2. 添加富途证券网关 (FutuGateway)
3. 加载 CTA 策略和回测应用

使用前请确保已安装相关插件：
pip install vnpy_futu vnpy_ctastrategy vnpy_ctabacktester
"""

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

# ----------------------------------------------------------------------
# 网关 (Gateways) 导入
# ----------------------------------------------------------------------
# ⚠️ 注意：CTP 网关目前不支持 macOS，因此在本脚本中被禁用。
# from vnpy_ctp import CtpGateway 

# 富途证券网关：支持港股、美股和 A 股通
try:
    from vnpy_futu import FutuGateway
except ImportError:
    FutuGateway = None
    print("✗ 未检测到 vnpy_futu 模块，请运行 'pip install vnpy_futu' 安装")

# ----------------------------------------------------------------------
# 应用 (Apps) 导入
# ----------------------------------------------------------------------
from vnpy_ctastrategy import CtaStrategyApp    # CTA 策略应用
from vnpy_ctabacktester import CtaBacktesterApp  # CTA 回测分析应用


def main():
    """启动 VeighNa Trader 主程序"""
    
    # 1. 创建 Qt 应用程序对象
    qapp = create_qapp()

    # 2. 创建事件引擎 (EventEngine)
    # 事件引擎负责系统内部的异步消息传递
    event_engine = EventEngine()

    # 3. 创建主引擎 (MainEngine)
    # 主引擎是整个系统的核心，管理网关和应用。
    main_engine = MainEngine(event_engine)
    
    # 4. 添加交易网关 (Add Gateways)
    # 尝试加载富途网关，确保已在后台运行 FutuOpenD
    if FutuGateway:
        main_engine.add_gateway(FutuGateway, gateway_name="FUTU")
        print("✓ 已加载富途证券网关 (FutuGateway)")
    
    # ⚠️ 如何添加 CTP：
    # 如果你在 Windows/Linux 上运行，可以取消下面代码的注释来加载 CTP
    # main_engine.add_gateway(CtpGateway)

    # 5. 添加应用程序 (Add Apps)
    main_engine.add_app(CtaStrategyApp)      # 加载 CTA 策略模块
    main_engine.add_app(CtaBacktesterApp)    # 加载 CTA 回测模块
    print("✓ 已加载 CTA 策略与回测应用")

    # 6. 创建并显示主窗口 (GUI Setup)
    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    # 7. 进入 Qt 事件循环
    # 程序会保持运行直到用户关闭窗口
    qapp.exec()


if __name__ == "__main__":
    main()
