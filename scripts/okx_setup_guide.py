#!/usr/bin/env python3
"""
OKX交易所配置指南脚本
===================

这个脚本将帮助您：
1. 测试OKX网关连接
2. 配置API密钥
3. 验证连接状态
4. 提供详细的设置步骤

使用方法:
    python scripts/okx_setup_guide.py
"""

import os
import sys
import json
from pathlib import Path

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def print_header():
    """打印标题"""
    print("=" * 60)
    print("🚀 OKX交易所配置指南")
    print("=" * 60)
    print()

def print_step_1():
    """步骤1: 创建OKX API"""
    print("📋 步骤 1: 创建OKX API密钥")
    print("-" * 40)
    print("1. 访问 OKX官网: https://www.okx.com")
    print("2. 登录您的账户")
    print("3. 进入 [API管理] 页面:")
    print("   - 点击右上角头像")
    print("   - 选择 'API管理'")
    print("   - 点击 '创建API'")
    print()
    print("4. 设置API权限:")
    print("   ✅ Read (读取) - 必须")
    print("   ✅ Trade (交易) - 推荐")
    print("   ❌ Withdraw (提币) - 不推荐新手开启")
    print()
    print("5. 记录以下信息:")
    print("   📝 API Key")
    print("   📝 Secret Key")
    print("   📝 Passphrase (密码短语)")
    print()
    print("⚠️  安全提示:")
    print("   - 设置IP白名单限制访问")
    print("   - 不要泄露API密钥给任何人")
    print("   - 建议先在测试环境练习")
    print()

def print_step_2():
    """步骤2: 在VeighNa中配置"""
    print("⚙️  步骤 2: 在VeighNa中配置OKX")
    print("-" * 40)
    print("1. 启动VeighNa: python run.py")
    print("2. 在主界面点击 [交易] 菜单")
    print("3. 选择 [连接] → [OKX]")
    print("4. 输入您的API信息:")
    print("   - API Key: 您的API密钥")
    print("   - Secret: 您的Secret密钥")
    print("   - Passphrase: 您的密码短语")
    print("   - 服务器: aws (推荐) 或 其他")
    print("   - 代理: 如果需要的话")
    print("5. 点击 [连接] 按钮")
    print()

def print_step_3():
    """步骤3: 验证连接"""
    print("✅ 步骤 3: 验证连接状态")
    print("-" * 40)
    print("连接成功的标志:")
    print("✅ Public API connected - 公共API连接成功")
    print("✅ Private API connected - 私有API连接成功")
    print("✅ Private websocket API connected - 私有WebSocket连接成功")
    print()
    print("如果看到错误:")
    print("❌ Private API request failed - 检查API密钥是否正确")
    print("❌ Invalid signature - 检查Secret和Passphrase")
    print("❌ IP restricted - 检查IP白名单设置")
    print()

def test_okx_import():
    """测试OKX模块导入"""
    print("🧪 测试 OKX 模块导入")
    print("-" * 40)
    try:
        from vnpy_okx import OkxGateway
        print("✅ OKX网关模块导入成功")
        return True
    except ImportError as e:
        print(f"❌ OKX网关模块导入失败: {e}")
        print("请确保已安装 vnpy_okx 包:")
        print("pip install vnpy_okx")
        return False

def create_sample_config():
    """创建示例配置文件"""
    print("📄 创建示例配置文件")
    print("-" * 40)
    
    config_dir = Path.home() / ".vntrader"
    config_dir.mkdir(exist_ok=True)
    
    sample_config = {
        "okx_api_key": "your_api_key_here",
        "okx_secret_key": "your_secret_key_here", 
        "okx_passphrase": "your_passphrase_here",
        "okx_server": "aws",
        "okx_proxy_host": "",
        "okx_proxy_port": 0
    }
    
    config_file = config_dir / "okx_config_sample.json"
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(sample_config, f, indent=4, ensure_ascii=False)
    
    print(f"✅ 示例配置文件已创建: {config_file}")
    print("请修改其中的API信息为您的真实信息")
    print()

def print_trading_tips():
    """交易建议"""
    print("💡 OKX交易建议")
    print("-" * 40)
    print("🎯 推荐交易品种:")
    print("   • BTC/USDT - 比特币现货")
    print("   • ETH/USDT - 以太坊现货")
    print("   • BTC-USDT-SWAP - 比特币永续合约")
    print("   • ETH-USDT-SWAP - 以太坊永续合约")
    print()
    print("📊 交易策略建议:")
    print("   • 现货交易: 适合长期投资")
    print("   • 合约交易: 适合短期套利")
    print("   • 网格交易: 适合震荡行情")
    print("   • DCA策略: 适合定投")
    print()
    print("⚠️  风险管理:")
    print("   • 设置止损止盈")
    print("   • 控制仓位大小")
    print("   • 分散投资组合")
    print("   • 先小额测试")
    print()

def print_troubleshooting():
    """故障排除"""
    print("🔧 常见问题解决")
    print("-" * 40)
    print("问题1: API连接失败")
    print("解决方案:")
    print("   • 检查API密钥是否正确")
    print("   • 确认IP白名单设置")
    print("   • 检查网络连接")
    print("   • 确认API权限设置")
    print()
    print("问题2: 无法下单")
    print("解决方案:")
    print("   • 确认账户有足够余额")
    print("   • 检查交易权限是否开启")
    print("   • 确认交易对是否正确")
    print("   • 检查订单参数")
    print()
    print("问题3: 数据延迟")
    print("解决方案:")
    print("   • 选择合适的服务器节点")
    print("   • 检查网络延迟")
    print("   • 考虑使用VPS")
    print()

def main():
    """主函数"""
    print_header()
    
    # 测试模块导入
    if not test_okx_import():
        return
    
    print()
    print_step_1()
    
    input("按回车键继续到下一步...")
    print()
    
    print_step_2()
    
    input("按回车键继续到下一步...")
    print()
    
    print_step_3()
    
    input("按回车键查看更多信息...")
    print()
    
    create_sample_config()
    
    print_trading_tips()
    
    print_troubleshooting()
    
    print("🎉 OKX配置指南完成！")
    print("如果您已经配置好API，可以启动VeighNa开始交易了：")
    print("python run.py")
    print()
    print("祝您交易愉快！💰")

if __name__ == "__main__":
    main()