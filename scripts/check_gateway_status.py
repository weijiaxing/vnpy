#!/usr/bin/env python3
"""
检查VeighNa网关连接状态
======================

帮助确认是否连接到真实交易所还是模拟交易

使用方法:
    python scripts/check_gateway_status.py
"""

import os
import sys

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def check_connection_status():
    """检查网关连接状态指南"""
    print("=" * 50)
    print("🔍 网关连接状态检查指南")
    print("=" * 50)
    
    print("\n📋 如何确认您的连接状态：")
    print("-" * 30)
    
    print("1. 查看VeighNa主界面右下角：")
    print("   ✅ 真实连接：显示 '已连接 OKX'")
    print("   ❌ 模拟交易：没有显示或显示其他")
    print()
    
    print("2. 查看下单时的接口栏：")
    print("   ✅ 真实交易：接口显示 'OKX'")
    print("   ❌ 模拟交易：接口显示 'PAPER'")
    print()
    
    print("3. 查看日志窗口：")
    print("   ✅ 真实连接：显示 'OKX Gateway connected'")
    print("   ❌ 模拟交易：没有相关连接信息")
    print()

def provide_connection_steps():
    """提供连接步骤"""
    print("🔧 连接到真实OKX交易所的步骤：")
    print("-" * 30)
    
    print("步骤1: 断开现有连接")
    print("   - 如果有任何连接，先断开")
    print("   - 确保界面右下角没有连接状态")
    print()
    
    print("步骤2: 连接OKX网关")
    print("   - 点击菜单：[交易] → [连接] → [OKX]")
    print("   - 输入您的API信息：")
    print("     * API Key: 您的API密钥")
    print("     * Secret: 您的Secret密钥")
    print("     * Passphrase: 您的密码短语")
    print("     * 服务器: aws (推荐)")
    print("   - 点击 [连接] 按钮")
    print()
    
    print("步骤3: 验证连接成功")
    print("   - 右下角显示：'已连接 OKX'")
    print("   - 日志显示：连接成功信息")
    print("   - 能看到真实的账户余额")
    print()

def explain_paper_trading():
    """解释模拟交易"""
    print("📝 关于模拟交易(Paper Trading)：")
    print("-" * 30)
    
    print("模拟交易的特点：")
    print("   ✅ 安全：不会使用真实资金")
    print("   ✅ 练习：可以测试策略和功能")
    print("   ✅ 学习：熟悉操作流程")
    print("   ❌ 虚拟：订单不会发送到真实交易所")
    print("   ❌ 无效：不会产生真实的盈亏")
    print()
    
    print("如何启用/禁用模拟交易：")
    print("   - 模拟交易通过'模拟交易应用'提供")
    print("   - 要进行真实交易，需要连接真实网关")
    print("   - 两者可以同时存在，但要注意区分")
    print()

def provide_troubleshooting():
    """提供故障排除建议"""
    print("🚨 常见问题及解决方案：")
    print("-" * 30)
    
    print("问题1: 连接后仍显示PAPER")
    print("解决方案：")
    print("   - 重启VeighNa程序")
    print("   - 确保API权限正确")
    print("   - 检查网络连接")
    print()
    
    print("问题2: 无法连接到OKX")
    print("解决方案：")
    print("   - 检查API密钥是否正确")
    print("   - 确认API权限包含Trade")
    print("   - 检查IP白名单设置")
    print()
    
    print("问题3: 连接成功但下单失败")
    print("解决方案：")
    print("   - 确认账户余额充足")
    print("   - 检查交易对格式(BTC-USDT)")
    print("   - 验证订单参数合理性")
    print()

def main():
    """主函数"""
    check_connection_status()
    provide_connection_steps()
    explain_paper_trading()
    provide_troubleshooting()
    
    print("=" * 50)
    print("💡 提示：建议先在模拟环境测试，")
    print("   确认功能正常后再切换到真实交易！")
    print("=" * 50)

if __name__ == "__main__":
    main() 