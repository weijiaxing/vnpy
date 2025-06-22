#!/usr/bin/env python3
"""
OKX连接测试脚本
===============

快速测试OKX网关连接状态和基本功能

使用方法:
    python scripts/test_okx_connection.py
"""

import os
import sys
import time
from datetime import datetime

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_okx_basic():
    """测试OKX基本功能"""
    print("🧪 测试OKX基本功能")
    print("-" * 40)
    
    try:
        from vnpy_okx import OkxGateway
        from vnpy.trader.gateway import BaseGateway
        from vnpy.event import EventEngine
        from vnpy.trader.engine import MainEngine
        
        print("✅ OKX模块导入成功")
        
        # 创建事件引擎和主引擎
        event_engine = EventEngine()
        main_engine = MainEngine(event_engine)
        
        # 添加OKX网关
        main_engine.add_gateway(OkxGateway)
        print("✅ OKX网关添加成功")
        
        # 获取网关实例
        okx_gateway = main_engine.get_gateway("OKX")
        if okx_gateway:
            print("✅ OKX网关实例创建成功")
            print(f"   网关名称: {okx_gateway.gateway_name}")
            return True
        else:
            print("❌ OKX网关实例创建失败")
            return False
            
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False

def test_okx_public_data():
    """测试OKX公共数据获取"""
    print("\n📊 测试OKX公共数据")
    print("-" * 40)
    
    try:
        import requests
        import json
        
        # 测试OKX公共API
        url = "https://www.okx.com/api/v5/public/instruments"
        params = {
            "instType": "SPOT"
        }
        
        print("正在获取OKX现货交易对信息...")
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('code') == '0':
                instruments = data.get('data', [])
                print(f"✅ 成功获取 {len(instruments)} 个现货交易对")
                
                # 显示前5个交易对
                print("📋 热门交易对:")
                for i, inst in enumerate(instruments[:5]):
                    print(f"   {i+1}. {inst.get('instId')} - {inst.get('baseCcy')}/{inst.get('quoteCcy')}")
                
                return True
            else:
                print(f"❌ API返回错误: {data.get('msg')}")
                return False
        else:
            print(f"❌ HTTP请求失败: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ 公共数据测试失败: {e}")
        return False

def show_okx_config_template():
    """显示OKX配置模板"""
    print("\n⚙️ OKX配置模板")
    print("-" * 40)
    
    config_template = """
在VeighNa中连接OKX需要以下信息:

🔑 API配置:
   API Key:     your_api_key_here
   Secret Key:  your_secret_key_here  
   Passphrase:  your_passphrase_here
   
🌐 服务器选择:
   • aws (推荐，速度快)
   • hk (香港节点)
   • sg (新加坡节点)
   
🔒 安全设置:
   • 启用IP白名单
   • 只开启必要权限
   • 定期更换API密钥
   
📝 权限设置:
   ✅ Read (读取权限) - 必须
   ✅ Trade (交易权限) - 推荐  
   ❌ Withdraw (提币权限) - 不推荐
"""
    
    print(config_template)

def show_next_steps():
    """显示下一步操作"""
    print("\n🚀 下一步操作")
    print("-" * 40)
    print("1. 创建OKX API密钥:")
    print("   https://www.okx.com/account/my-api")
    print()
    print("2. 运行详细配置指南:")
    print("   python scripts/okx_setup_guide.py")
    print()
    print("3. 启动VeighNa并连接OKX:")
    print("   python run.py")
    print()
    print("4. 在VeighNa中配置API信息:")
    print("   交易 → 连接 → OKX")
    print()
    print("5. 开始交易:")
    print("   • 先用小额测试")
    print("   • 设置止损策略")
    print("   • 关注风险管理")

def main():
    """主函数"""
    print("=" * 50)
    print("🔍 OKX连接测试")
    print("=" * 50)
    print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # 测试基本功能
    basic_ok = test_okx_basic()
    
    # 测试公共数据
    public_ok = test_okx_public_data()
    
    # 显示配置模板
    show_okx_config_template()
    
    # 显示测试结果
    print("\n📊 测试结果总结")
    print("-" * 40)
    print(f"基本功能测试: {'✅ 通过' if basic_ok else '❌ 失败'}")
    print(f"公共数据测试: {'✅ 通过' if public_ok else '❌ 失败'}")
    
    if basic_ok and public_ok:
        print("\n🎉 所有测试通过！OKX网关准备就绪")
        print("您现在可以配置API密钥开始交易了")
    else:
        print("\n⚠️ 部分测试失败，请检查网络连接和依赖安装")
    
    show_next_steps()

if __name__ == "__main__":
    main()