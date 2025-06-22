#!/usr/bin/env python3
"""
VeighNa 交易平台主启动脚本
=============================

功能特性:
- 支持多网关动态加载 (数字货币、期货、股票等)
- 支持多应用模块加载 (策略、数据、工具等)
- 自动检测并跳过未安装的模块
- 完整的启动状态报告
- 支持国际化 (中英文切换)

使用方法:
    python run.py

作者: VeighNa Team
版本: 2.0
最后更新: 2024-12-22
"""

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp


def main():
    """启动 VeighNa 交易平台主程序"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # 网关配置列表 - 包含已安装和未安装的网关
    gateways_to_load = [
        # 数字货币交易所
        ("vnpy_binance", "BinanceSpotGateway", "币安现货网关"),
        ("vnpy_binance", "BinanceLinearGateway", "币安线性合约网关"),
        ("vnpy_binance", "BinanceInverseGateway", "币安反向合约网关"),
        ("vnpy_okx", "OkxGateway", "OKX交易所网关"),
        ("vnpy_bybit", "BybitGateway", "Bybit交易所网关"),
        
        # 传统金融网关
        # ("vnpy_ib", "IbGateway", "Interactive Brokers网关"),  # 暂时禁用：ibapi版本兼容性问题
        ("vnpy_futu", "FutuGateway", "富途证券网关"),
        
        # 期货网关
        # ("vnpy_ctp", "CtpGateway", "CTP期货网关"),
        # ("vnpy_ctptest", "CtptestGateway", "CTP测试网关"),
        # ("vnpy_mini", "MiniGateway", "迷你期货网关"),
        # ("vnpy_femas", "FemasGateway", "飞马期货网关"),
        # ("vnpy_esunny", "EsunnyGateway", "易盛期货网关"),
        
        # 股票网关
        # ("vnpy_xtp", "XtpGateway", "XTP股票网关"),
        # ("vnpy_tora", "ToraStockGateway", "TORA股票网关"),
        # ("vnpy_tora", "ToraOptionGateway", "TORA期权网关"),
        
        # 其他网关
        # ("vnpy_tap", "TapGateway", "TAP网关"),
        # ("vnpy_da", "DaGateway", "大连飞创网关"),
        # ("vnpy_rohon", "RohonGateway", "融航网关"),
        # ("vnpy_tts", "TtsGateway", "TTS网关"),
        # ("vnpy_uft", "UftGateway", "恒生UFT网关"),
        # ("vnpy_sopt", "SoptGateway", "SOPT网关"),
        
        # RPC网关（用于分布式部署）
        ("vnpy_rpcservice", "RpcGateway", "RPC网关"),
    ]
    
    # 动态加载网关
    loaded_gateways = []
    for module_name, gateway_class_name, description in gateways_to_load:
        try:
            module = __import__(module_name, fromlist=[gateway_class_name])
            gateway_class = getattr(module, gateway_class_name)
            main_engine.add_gateway(gateway_class)
            loaded_gateways.append(description)
            print(f"✓ 已加载 {description}")
        except ImportError:
            print(f"✗ {description} 模块未安装，跳过加载")
        except AttributeError:
            print(f"✗ {description} 类未找到，跳过加载")
        except Exception as e:
            print(f"✗ 加载 {description} 时出错: {e}")
    
    # 应用模块配置列表
    apps_to_load = [
        # 策略相关
        ("vnpy_ctastrategy", "CtaStrategyApp", "CTA策略应用"),
        ("vnpy_ctabacktester", "CtaBacktesterApp", "CTA回测应用"),
        ("vnpy_portfoliostrategy", "PortfolioStrategyApp", "投资组合策略应用"),
        ("vnpy_spreadtrading", "SpreadTradingApp", "价差交易应用"),
        ("vnpy_algotrading", "AlgoTradingApp", "算法交易应用"),
        ("vnpy_optionmaster", "OptionMasterApp", "期权主控应用"),
        
        # 数据相关
        ("vnpy_datamanager", "DataManagerApp", "数据管理应用"),
        ("vnpy_datarecorder", "DataRecorderApp", "数据记录应用"),
        
        # 工具应用
        ("vnpy_scripttrader", "ScriptTraderApp", "脚本交易应用"),
        ("vnpy_chartwizard", "ChartWizardApp", "图表分析应用"),
        ("vnpy_riskmanager", "RiskManagerApp", "风险管理应用"),
        # ("vnpy_webtrader", "WebTraderApp", "Web交易应用"),
        ("vnpy_portfoliomanager", "PortfolioManagerApp", "投资组合管理应用"),
        # ("vnpy_excelrtd", "ExcelRtdApp", "Excel RTD应用"),
        # ("vnpy_rpcservice", "RpcServiceApp", "RPC服务应用"),
        
        # 模拟交易应用
        # ("vnpy_paperaccount", "PaperAccountApp", "模拟交易应用"),
    ]
    
    # 动态加载应用
    loaded_apps = []
    for module_name, app_class_name, description in apps_to_load:
        try:
            module = __import__(module_name, fromlist=[app_class_name])
            app_class = getattr(module, app_class_name)
            main_engine.add_app(app_class)
            loaded_apps.append(description)
            print(f"✓ 已加载 {description}")
        except ImportError:
            print(f"✗ {description} 模块未安装，跳过加载")
        except AttributeError:
            print(f"✗ {description} 类未找到，跳过加载")
        except Exception as e:
            print(f"✗ 加载 {description} 时出错: {e}")

    print(f"\n=== 加载总结 ===")
    print(f"成功加载 {len(loaded_gateways)} 个网关:")
    for gateway in loaded_gateways:
        print(f"  • {gateway}")
    print(f"\n成功加载 {len(loaded_apps)} 个应用:")
    for app in loaded_apps:
        print(f"  • {app}")
    print("=================\n")

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()