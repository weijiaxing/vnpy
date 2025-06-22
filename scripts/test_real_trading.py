#!/usr/bin/env python3
"""
真实交易环境测试用例
==================

诊断并解决OKX连接成功但委托下单仍显示PAPER的问题

使用方法:
    python scripts/test_real_trading.py
"""

import os
import sys
import time
from datetime import datetime

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_gateway_status():
    """测试网关状态"""
    print("🔍 测试网关连接状态")
    print("-" * 50)
    
    try:
        from vnpy.event import EventEngine
        from vnpy.trader.engine import MainEngine
        from vnpy_okx import OkxGateway
        
        # 创建引擎
        event_engine = EventEngine()
        main_engine = MainEngine(event_engine)
        
        # 添加OKX网关
        main_engine.add_gateway(OkxGateway)
        
        # 获取所有网关
        gateways = main_engine.get_all_gateways()
        print(f"✅ 已注册网关数量: {len(gateways)}")
        
        for name, gateway in gateways.items():
            print(f"   网关名称: {name}")
            print(f"   网关类型: {type(gateway).__name__}")
            print(f"   连接状态: {'已连接' if hasattr(gateway, 'connected') and gateway.connected else '未连接'}")
        
        return main_engine, event_engine
        
    except Exception as e:
        print(f"❌ 网关状态测试失败: {e}")
        return None, None

def test_contract_query(main_engine):
    """测试合约查询"""
    print("\n📋 测试合约查询")
    print("-" * 50)
    
    if not main_engine:
        print("❌ 主引擎未初始化")
        return
    
    try:
        # 获取所有合约
        contracts = main_engine.get_all_contracts()
        print(f"✅ 合约总数: {len(contracts)}")
        
        # 查找DOGE相关合约
        doge_contracts = [c for c in contracts if 'DOGE' in c.symbol.upper()]
        print(f"✅ DOGE相关合约数量: {len(doge_contracts)}")
        
        # 显示前5个DOGE合约的详细信息
        print("\n📊 DOGE合约详情:")
        for i, contract in enumerate(doge_contracts[:5]):
            print(f"   {i+1}. {contract.symbol}")
            print(f"      交易所: {contract.exchange.value}")
            print(f"      网关: {contract.gateway_name}")
            print(f"      产品类型: {getattr(contract, 'product', 'N/A')}")
            print(f"      最小交易量: {getattr(contract, 'min_volume', 'N/A')}")
            print()
        
        return doge_contracts
        
    except Exception as e:
        print(f"❌ 合约查询测试失败: {e}")
        return []

def test_order_creation():
    """测试订单创建逻辑"""
    print("🧪 测试订单创建逻辑")
    print("-" * 50)
    
    try:
        from vnpy.trader.object import OrderRequest
        from vnpy.trader.constant import Direction, OrderType, Exchange
        
        # 创建测试订单请求
        order_req = OrderRequest(
            symbol="DOGE-USDT",
            exchange=Exchange.OKX,
            direction=Direction.LONG,
            type=OrderType.LIMIT,
            volume=100.0,
            price=0.15,
        )
        
        print(f"✅ 订单请求创建成功:")
        print(f"   交易对: {order_req.symbol}")
        print(f"   交易所: {order_req.exchange.value}")
        print(f"   方向: {order_req.direction.value}")
        print(f"   类型: {order_req.type.value}")
        print(f"   数量: {order_req.volume}")
        print(f"   价格: {order_req.price}")
        print(f"   vt_symbol: {order_req.vt_symbol}")
        
        return order_req
        
    except Exception as e:
        print(f"❌ 订单创建测试失败: {e}")
        return None

def diagnose_paper_trading_issue():
    """诊断PAPER交易问题"""
    print("\n🔧 诊断PAPER交易问题")
    print("-" * 50)
    
    # 检查可能的原因
    issues = [
        {
            "问题": "模拟交易应用仍在运行",
            "检查方法": "查看应用列表中是否有PaperAccountApp",
            "解决方案": "禁用或移除模拟交易应用"
        },
        {
            "问题": "网关优先级问题",
            "检查方法": "检查网关注册顺序",
            "解决方案": "确保OKX网关最后注册或优先级最高"
        },
        {
            "问题": "合约映射问题",
            "检查方法": "检查合约的gateway_name属性",
            "解决方案": "重新查询合约数据"
        },
        {
            "问题": "引擎状态问题",
            "检查方法": "检查主引擎的网关管理",
            "解决方案": "重启程序并只连接OKX"
        }
    ]
    
    for i, issue in enumerate(issues, 1):
        print(f"{i}. {issue['问题']}")
        print(f"   检查: {issue['检查方法']}")
        print(f"   解决: {issue['解决方案']}")
        print()

def provide_solutions():
    """提供解决方案"""
    print("🚀 解决方案")
    print("-" * 50)
    
    print("方案1: 修改run.py，禁用模拟交易应用")
    print("   - 注释掉PaperAccountApp相关代码")
    print("   - 重新启动程序")
    print()
    
    print("方案2: 清理网关状态")
    print("   - 断开所有连接")
    print("   - 重启VeighNa")
    print("   - 只连接OKX网关")
    print()
    
    print("方案3: 检查网关注册顺序")
    print("   - 确保OKX网关在模拟交易应用之后注册")
    print("   - 或者完全移除模拟交易功能")
    print()
    
    print("方案4: 强制指定网关")
    print("   - 在下单时明确指定gateway_name='OKX'")
    print("   - 修改订单路由逻辑")
    print()

def create_fixed_run_script():
    """创建修复版本的运行脚本"""
    print("\n📝 创建修复版本的运行脚本")
    print("-" * 50)
    
    fixed_script = '''#!/usr/bin/env python3
"""
VeighNa 纯真实交易启动脚本 (无模拟交易)
=====================================

这个版本移除了模拟交易应用，确保只使用真实交易
"""

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp


def main():
    """启动 VeighNa 纯真实交易平台"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # 只加载真实交易网关
    gateways_to_load = [
        ("vnpy_okx", "OkxGateway", "OKX交易所网关"),
        ("vnpy_binance", "BinanceSpotGateway", "币安现货网关"),
        ("vnpy_bybit", "BybitGateway", "Bybit交易所网关"),
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
        except Exception as e:
            print(f"✗ 加载 {description} 失败: {e}")
    
    # 只加载非模拟交易应用
    apps_to_load = [
        ("vnpy_ctastrategy", "CtaStrategyApp", "CTA策略应用"),
        ("vnpy_datamanager", "DataManagerApp", "数据管理应用"),
        ("vnpy_riskmanager", "RiskManagerApp", "风险管理应用"),
        # 注意：这里移除了 PaperAccountApp
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
        except Exception as e:
            print(f"✗ 加载 {description} 失败: {e}")

    print(f"\\n=== 纯真实交易模式启动 ===")
    print(f"已加载 {len(loaded_gateways)} 个真实网关")
    print(f"已加载 {len(loaded_apps)} 个应用")
    print("=========================\\n")

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
'''
    
    script_path = "run_real_trading.py"
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(fixed_script)
    
    print(f"✅ 修复版本脚本已创建: {script_path}")
    print("   使用方法: python run_real_trading.py")
    print("   这个版本移除了模拟交易，确保纯真实交易")

def main():
    """主函数"""
    print("=" * 60)
    print("🧪 VeighNa 真实交易环境测试")
    print("=" * 60)
    print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 执行测试
    main_engine, event_engine = test_gateway_status()
    contracts = test_contract_query(main_engine)
    order_req = test_order_creation()
    
    # 诊断问题
    diagnose_paper_trading_issue()
    provide_solutions()
    create_fixed_run_script()
    
    print("\n" + "=" * 60)
    print("📋 测试完成")
    print("建议使用 run_real_trading.py 启动纯真实交易环境")
    print("=" * 60)

if __name__ == "__main__":
    main() 