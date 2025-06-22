#!/usr/bin/env python3
"""
VeighNa 语言设置脚本
Quick language setting script for VeighNa
"""

import os
import sys
import argparse

# 添加项目路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from vnpy.trader.locale import get_supported_languages, switch_language
from vnpy.trader.setting import SETTINGS, SETTING_FILENAME
from vnpy.trader.utility import save_json


def set_language(language: str, save_to_file: bool = True):
    """设置语言"""
    supported_langs = get_supported_languages()
    
    if language not in supported_langs:
        print(f"❌ 不支持的语言: {language}")
        print(f"支持的语言: {list(supported_langs.keys())}")
        return False
    
    # 切换语言
    switch_language(language)
    
    if save_to_file:
        # 保存到设置文件
        SETTINGS["language"] = language
        save_json(SETTING_FILENAME, SETTINGS)
        print(f"✅ 语言已设置为: {supported_langs[language]} ({language})")
        print(f"✅ 设置已保存到: {SETTING_FILENAME}")
    else:
        print(f"✅ 当前会话语言已设置为: {supported_langs[language]} ({language})")
    
    return True


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="VeighNa 语言设置工具 / VeighNa Language Setting Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例 / Examples:
  python set_language.py zh_CN        # 设置为中文
  python set_language.py en           # 设置为英文
  python set_language.py --list       # 显示支持的语言
  python set_language.py --temp en    # 临时设置为英文（不保存）
        """
    )
    
    parser.add_argument(
        "language", 
        nargs="?",
        help="语言代码 / Language code (zh_CN, en)"
    )
    
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="显示支持的语言列表 / Show supported languages"
    )
    
    parser.add_argument(
        "--temp", "-t",
        action="store_true",
        help="临时设置（不保存到文件）/ Temporary setting (don't save to file)"
    )
    
    args = parser.parse_args()
    
    # 显示支持的语言
    if args.list:
        supported_langs = get_supported_languages()
        print("支持的语言 / Supported Languages:")
        for code, name in supported_langs.items():
            print(f"  {code}: {name}")
        return
    
    # 设置语言
    if args.language:
        save_to_file = not args.temp
        set_language(args.language, save_to_file)
    else:
        # 交互式设置
        supported_langs = get_supported_languages()
        print("VeighNa 语言设置 / VeighNa Language Setting")
        print("=" * 40)
        print("选择语言 / Choose Language:")
        
        for i, (code, name) in enumerate(supported_langs.items(), 1):
            print(f"  {i}. {name} ({code})")
        
        try:
            choice = input("\n请输入选择 / Enter choice: ").strip()
            
            if choice.isdigit():
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < len(supported_langs):
                    lang_code = list(supported_langs.keys())[choice_idx]
                    set_language(lang_code, save_to_file=True)
                else:
                    print("❌ 无效选择 / Invalid choice")
            else:
                # 直接输入语言代码
                set_language(choice, save_to_file=True)
                
        except KeyboardInterrupt:
            print("\n\n程序被中断 / Program interrupted")
        except Exception as e:
            print(f"❌ 错误 / Error: {e}")


if __name__ == "__main__":
    main()