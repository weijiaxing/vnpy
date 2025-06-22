#!/usr/bin/env python3
"""
VeighNa 语言切换演示脚本
Language switching demo for VeighNa
"""

import os
import sys

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from vnpy.trader.locale import (
    switch_language, 
    get_current_language, 
    get_supported_languages,
    _
)


def demo_language_switch():
    """演示语言切换功能"""
    print("=" * 50)
    print("VeighNa 语言切换演示 / VeighNa Language Switch Demo")
    print("=" * 50)
    
    # 显示支持的语言
    supported_langs = get_supported_languages()
    print(f"\n支持的语言 / Supported Languages:")
    for code, name in supported_langs.items():
        current = "✓" if code == get_current_language() else " "
        print(f"  [{current}] {code}: {name}")
    
    print(f"\n当前语言 / Current Language: {get_current_language()}")
    
    # 测试翻译
    print(f"\n翻译测试 / Translation Test:")
    test_strings = [
        "系统",
        "功能", 
        "配置",
        "帮助",
        "连接",
        "退出"
    ]
    
    for text in test_strings:
        translated = _(text)
        print(f"  '{text}' -> '{translated}'")
    
    # 交互式语言切换
    print(f"\n" + "=" * 30)
    print("交互式语言切换 / Interactive Language Switch")
    print("=" * 30)
    
    while True:
        print(f"\n当前语言 / Current: {get_current_language()}")
        print("选择语言 / Choose language:")
        for i, (code, name) in enumerate(supported_langs.items(), 1):
            print(f"  {i}. {name} ({code})")
        print("  0. 退出 / Exit")
        
        try:
            choice = input("\n请输入选择 / Enter choice (0-2): ").strip()
            
            if choice == "0":
                print("再见! / Goodbye!")
                break
            elif choice == "1":
                switch_language("zh_CN")
            elif choice == "2":
                switch_language("en")
            else:
                print("无效选择 / Invalid choice")
                continue
                
            # 重新测试翻译
            print(f"\n切换后的翻译测试 / Translation test after switch:")
            for text in test_strings[:3]:  # 只显示前3个
                translated = _(text)
                print(f"  '{text}' -> '{translated}'")
                
        except KeyboardInterrupt:
            print("\n\n程序被中断 / Program interrupted")
            break
        except Exception as e:
            print(f"错误 / Error: {e}")


if __name__ == "__main__":
    demo_language_switch()