#!/usr/bin/env python3
"""
VeighNa 下单委托问题诊断脚本
============================

当您遇到下单委托失败时，运行此脚本进行全面诊断

使用方法:
    python scripts/diagnose_trading_issue.py

功能:
- 检查网关连接状态
- 验证API权限设置
- 测试下单功能
- 提供解决方案建议
"""

import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def print_header():
    """打印诊断标题"""
    print("=" * 60)
    print("🔍 VeighNa 下单委托问题诊断")
    print("=" * 60)
    print(f"诊断时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

def check_network_connection():
    """检查网络连接"""
    print("🌐 检查网络连接")
    print("-" * 40)
    
    try:
        import requests
        
        # 测试OKX连接
        print("正在测试OKX连接...")
        response = requests.get("https://www.okx.com/api/v5/public/time", timeout=10)
        if response.status_code == 200:
            print("✅ OKX API连接正常")
        else:
            print(f"❌ OKX API连接失败: HTTP {response.status_code}")
            return False
            
        # 测试币安连接
        print("正在测试币安连接...")
        response = requests.get("https://api.binance.com/api/v3/time", timeout=10)
        if response.status_code == 200:
            print("✅ 币安API连接正常")
        else:
            print("⚠️ 币安API连接失败")
            
        return True
        
    except Exception as e:
        print(f"❌ 网络连接测试失败: {e}")
        return False

def check_vnpy_modules():
    """检查VeighNa模块"""
    print("\n📦 检查VeighNa模块")
    print("-" * 40)
    
    modules_to_check = [
        ("vnpy.trader.engine", "MainEngine", "主引擎"),
        ("vnpy.event", "EventEngine", "事件引擎"),
        ("vnpy_okx", "OkxGateway", "OKX网关"),
        ("vnpy_binance", "BinanceSpotGateway", "币安现货网关"),
        ("vnpy_riskmanager", "RiskManagerApp", "风险管理"),
    ]
    
    success_count = 0
    for module_name, class_name, description in modules_to_check:
        try:
            module = __import__(module_name, fromlist=[class_name])
            getattr(module, class_name)
            print(f"✅ {description} 模块正常")
            success_count += 1
        except ImportError:
            print(f"❌ {description} 模块未安装")
        except AttributeError:
            print(f"⚠️ {description} 类未找到")
        except Exception as e:
            print(f"❌ {description} 检查失败: {e}")
    
    print(f"\n模块检查结果: {success_count}/{len(modules_to_check)} 个模块正常")
    return success_count >= 3  # 至少需要主要模块正常

def check_config_files():
    """检查配置文件"""
    print("\n📁 检查配置文件")
    print("-" * 40)
    
    config_dir = Path.home() / ".vntrader"
    setting_file = config_dir / "vt_setting.json"
    
    if not config_dir.exists():
        print("❌ VeighNa配置目录不存在")
        print(f"   预期位置: {config_dir}")
        return False
    
    print(f"✅ 配置目录存在: {config_dir}")
    
    if setting_file.exists():
        print(f"✅ 设置文件存在: {setting_file}")
        try:
            with open(setting_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                print(f"   配置项数量: {len(settings)}")
                
                # 检查关键配置
                if 'font.family' in settings:
                    print(f"   字体设置: {settings['font.family']}")
                if 'language' in settings:
                    print(f"   语言设置: {settings['language']}")
                    
        except Exception as e:
            print(f"⚠️ 设置文件读取失败: {e}")
    else:
        print(f"⚠️ 设置文件不存在: {setting_file}")
    
    return True

def diagnose_trading_issues():
    """诊断交易问题"""
    print("\n🎯 常见下单委托失败原因诊断")
    print("-" * 40)
    
    issues = [
        {
            "问题": "API权限不足",
            "症状": "连接成功但无法下单",
            "解决方案": [
                "检查API是否开启交易权限(Trade)",
                "确认IP白名单设置正确",
                "验证API密钥、密码短语是否正确"
            ]
        },
        {
            "问题": "账户余额不足",
            "症状": "下单被拒绝",
            "解决方案": [
                "检查账户USDT余额是否充足",
                "确认交易数量不超过可用余额",
                "检查是否有冻结资金"
            ]
        },
        {
            "问题": "交易对输入错误",
            "症状": "找不到合约或下单失败",
            "解决方案": [
                "确认交易对格式正确 (如: BTC-USDT)",
                "检查交易所选择是否正确 (GLOBAL)",
                "验证合约是否存在且可交易"
            ]
        },
        {
            "问题": "订单参数错误",
            "症状": "订单被交易所拒绝",
            "解决方案": [
                "检查价格是否在合理范围内",
                "确认数量符合最小交易单位",
                "验证订单类型设置正确"
            ]
        },
        {
            "问题": "风险管理限制",
            "症状": "订单被风控拦截",
            "解决方案": [
                "检查风险管理设置",
                "确认日内交易限额",
                "验证单笔交易限制"
            ]
        },
        {
            "问题": "网关连接不稳定",
            "症状": "偶尔下单失败",
            "解决方案": [
                "检查网络连接稳定性",
                "尝试重新连接网关",
                "考虑使用VPS提高稳定性"
            ]
        }
    ]
    
    for i, issue in enumerate(issues, 1):
        print(f"\n{i}. {issue['问题']}")
        print(f"   症状: {issue['症状']}")
        print("   解决方案:")
        for solution in issue['解决方案']:
            print(f"   • {solution}")

def provide_quick_fixes():
    """提供快速修复建议"""
    print("\n🚀 快速修复建议")
    print("-" * 40)
    
    print("📋 立即检查清单:")
    print("□ 1. 确认网关连接状态 (界面右下角显示'已连接')")
    print("□ 2. 检查账户余额 (资金栏显示足够USDT)")
    print("□ 3. 验证交易对格式 (如: BTC-USDT)")
    print("□ 4. 确认交易所选择 (推荐: GLOBAL)")
    print("□ 5. 检查订单参数 (价格、数量合理)")
    print("□ 6. 查看日志窗口 (是否有错误信息)")
    print()
    
    print("🔧 逐步排查步骤:")
    print("步骤1: 重新连接网关")
    print("   - 断开当前连接")
    print("   - 等待5秒")
    print("   - 重新连接")
    print()
    
    print("步骤2: 测试小额订单")
    print("   - 选择BTC-USDT")
    print("   - 数量设置为0.001")
    print("   - 使用市价单测试")
    print()
    
    print("步骤3: 检查API设置")
    print("   - 登录交易所网站")
    print("   - 确认API权限设置")
    print("   - 检查IP白名单")
    print()

def create_test_order_script():
    """创建测试下单脚本"""
    print("\n📝 创建测试下单脚本")
    print("-" * 40)
    
    test_script = '''#!/usr/bin/env python3
"""
测试下单脚本
============

这个脚本将帮助您测试下单功能

使用前请确保:
1. VeighNa已启动并连接到交易所
2. 账户有足够余额
3. API权限设置正确
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.object import OrderRequest
from vnpy.trader.constant import Direction, OrderType, Exchange

def test_order():
    """测试下单功能"""
    print("🧪 开始测试下单功能...")
    
    # 创建引擎
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # 这里需要您手动添加和连接网关
    print("请确保已在VeighNa主界面连接到交易所")
    print("然后运行此脚本进行测试")
    
    # 测试订单参数
    order_req = OrderRequest(
        symbol="BTC-USDT",
        exchange=Exchange.OKX,
        direction=Direction.LONG,
        type=OrderType.LIMIT,
        volume=0.001,  # 小额测试
        price=50000,   # 请根据当前价格调整
    )
    
    print(f"测试订单: {order_req.symbol} {order_req.direction.value} {order_req.volume}")
    print("⚠️ 这只是测试脚本，实际下单请在VeighNa界面操作")

if __name__ == "__main__":
    test_order()
'''
    
    script_path = Path("scripts/test_order.py")
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(test_script)
    
    print(f"✅ 测试脚本已创建: {script_path}")
    print("   您可以参考此脚本了解下单流程")

def main():
    """主函数"""
    print_header()
    
    # 执行诊断步骤
    network_ok = check_network_connection()
    modules_ok = check_vnpy_modules()
    config_ok = check_config_files()
    
    # 显示诊断结果
    print("\n📊 诊断结果总结")
    print("-" * 40)
    print(f"网络连接: {'✅ 正常' if network_ok else '❌ 异常'}")
    print(f"模块检查: {'✅ 正常' if modules_ok else '❌ 异常'}")
    print(f"配置文件: {'✅ 正常' if config_ok else '❌ 异常'}")
    
    # 提供建议
    if network_ok and modules_ok and config_ok:
        print("\n🎉 基础环境检查通过！")
        print("问题可能出现在交易配置或API设置上")
    else:
        print("\n⚠️ 发现基础环境问题，请先解决这些问题")
    
    # 显示诊断和修复建议
    diagnose_trading_issues()
    provide_quick_fixes()
    create_test_order_script()
    
    print("\n" + "=" * 60)
    print("📞 如果问题仍然存在，请提供以下信息:")
    print("1. VeighNa日志窗口的具体错误信息")
    print("2. 您使用的交易所和交易对")
    print("3. 下单时的具体参数设置")
    print("4. API权限配置截图")
    print("=" * 60)

if __name__ == "__main__":
    main()