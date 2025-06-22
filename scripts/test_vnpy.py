#!/usr/bin/env python3
"""
测试 VeighNa 核心功能
"""

import sys
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

def test_core_functionality():
    """测试核心功能"""
    print("正在测试 VeighNa 核心功能...")
    
    try:
        # 创建事件引擎
        event_engine = EventEngine()
        print("✓ 事件引擎创建成功")
        
        # 创建主引擎
        main_engine = MainEngine(event_engine)
        print("✓ 主引擎创建成功")
        
        # 测试基本功能
        print(f"✓ VeighNa 版本: {main_engine.get_version()}")
        
        print("✓ 核心功能测试通过！")
        return True
        
    except Exception as e:
        print(f"✗ 核心功能测试失败: {e}")
        return False

def test_gui():
    """测试图形界面"""
    print("\n正在测试图形界面...")
    
    try:
        # 创建 Qt 应用
        qapp = create_qapp()
        print("✓ Qt 应用创建成功")
        
        # 创建事件引擎和主引擎
        event_engine = EventEngine()
        main_engine = MainEngine(event_engine)
        
        # 创建主窗口
        main_window = MainWindow(main_engine, event_engine)
        print("✓ 主窗口创建成功")
        
        # 显示窗口（但不进入事件循环）
        main_window.show()
        print("✓ 图形界面测试通过！")
        print("✓ 窗口已显示，请检查是否正常显示")
        
        # 让窗口显示一会儿
        qapp.processEvents()
        
        return True
        
    except Exception as e:
        print(f"✗ 图形界面测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=== VeighNa 功能测试 ===\n")
    
    # 测试核心功能
    core_ok = test_core_functionality()
    
    if core_ok:
        # 测试图形界面
        gui_ok = test_gui()
        
        if gui_ok:
            print("\n=== 测试结果 ===")
            print("✓ 所有测试通过！VeighNa 可以正常运行")
            print("\n要启动完整的 VeighNa 交易系统，请运行:")
            print("python examples/veighna_trader/run.py")
        else:
            print("\n=== 测试结果 ===")
            print("✗ 图形界面测试失败")
    else:
        print("\n=== 测试结果 ===")
        print("✗ 核心功能测试失败")
        sys.exit(1)

if __name__ == "__main__":
    main() 