"""
VeighNa Trader国际化模块

支持中英文动态切换，语言设置会自动保存到配置文件中。
"""

import os
import gettext
from typing import Union, Dict, Optional

# 支持的语言列表
SUPPORTED_LANGUAGES = {
    "zh_CN": "中文 (简体)",
    "en": "English"
}

# 全局翻译对象
_translator: Optional[Union[gettext.GNUTranslations, gettext.NullTranslations]] = None
_current_language: str = "zh_CN"  # 默认语言
_initialized: bool = False  # 初始化标志


def _get_language_from_settings() -> str:
    """从设置文件中获取语言配置"""
    try:
        # 延迟导入避免循环依赖
        import json
        import os
        from pathlib import Path
        
        # 直接读取配置文件，避免依赖其他模块
        vntrader_dir = Path.home() / ".vntrader"
        setting_file = vntrader_dir / "vt_setting.json"
        
        if setting_file.exists():
            with open(setting_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                language = settings.get("language", "zh_CN")
                print(f"Read language from config file: {language}")
                return language
        else:
            print("Config file not found, using default language")
            return "zh_CN"
    except Exception as e:
        print(f"Error reading config file: {e}, using default language")
        return "zh_CN"


def _get_language_from_env() -> str:
    """从环境变量获取语言设置"""
    return os.environ.get("VNPY_LANGUAGE", "zh_CN")


def _get_system_language() -> str:
    """获取系统默认语言"""
    import locale
    try:
        system_locale = locale.getdefaultlocale()[0]
        if system_locale and system_locale.startswith("zh"):
            return "zh_CN"
        else:
            return "en"
    except:
        return "zh_CN"


def _detect_language() -> str:
    """检测应该使用的语言"""
    # 优先级：环境变量 > 配置文件 > 系统语言 > 默认中文
    
    # 1. 从环境变量读取（最高优先级，用于临时覆盖）
    lang = _get_language_from_env()
    if lang != "zh_CN" and lang in SUPPORTED_LANGUAGES:  # 环境变量非默认值时使用
        print(f"Using language from environment: {lang}")
        return lang
    
    # 2. 从配置文件读取
    lang = _get_language_from_settings()
    if lang in SUPPORTED_LANGUAGES:
        return lang
    
    # 3. 从系统语言检测
    lang = _get_system_language()
    if lang in SUPPORTED_LANGUAGES:
        print(f"Using system language: {lang}")
        return lang
    
    # 4. 默认中文
    print("Using default language: zh_CN")
    return "zh_CN"


def _load_translator(language: str) -> Union[gettext.GNUTranslations, gettext.NullTranslations]:
    """加载指定语言的翻译器"""
    if language == "zh_CN":
        # 中文不需要翻译，返回 NullTranslations
        return gettext.NullTranslations()
    
    # 英文需要加载翻译文件
    try:
        locale_dir = os.path.join(os.path.dirname(__file__))
        return gettext.translation("vnpy", locale_dir, languages=[language])
    except FileNotFoundError:
        print(f"Warning: Translation file for {language} not found, using NullTranslations")
        return gettext.NullTranslations()


def _initialize_language():
    """初始化语言设置"""
    global _translator, _current_language, _initialized
    
    if _initialized:
        return
    
    _current_language = _detect_language()
    _translator = _load_translator(_current_language)
    _initialized = True
    
    print(f"Language initialized: {_current_language} ({SUPPORTED_LANGUAGES.get(_current_language, 'Unknown')})")


def switch_language(language: str) -> bool:
    """
    切换语言
    
    Args:
        language: 语言代码，如 'zh_CN' 或 'en'
    
    Returns:
        bool: 切换是否成功
    """
    global _translator, _current_language, _initialized
    
    if language not in SUPPORTED_LANGUAGES:
        print(f"Unsupported language: {language}")
        return False
    
    if language == _current_language:
        print(f"Language is already set to {language}")
        return True
    
    # 加载新的翻译器
    _translator = _load_translator(language)
    _current_language = language
    _initialized = True
    
    # 保存到设置文件
    try:
        # 延迟导入避免循环依赖
        import json
        from pathlib import Path
        
        # 直接操作配置文件
        vntrader_dir = Path.home() / ".vntrader"
        vntrader_dir.mkdir(exist_ok=True)
        setting_file = vntrader_dir / "vt_setting.json"
        
        # 读取现有设置
        settings = {}
        if setting_file.exists():
            with open(setting_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
        
        # 更新语言设置
        settings["language"] = language
        
        # 保存设置
        with open(setting_file, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=4, ensure_ascii=False)
            
        print(f"Language switched to {language} and saved to settings")
    except Exception as e:
        print(f"Failed to save language setting: {e}")
    
    return True


def get_current_language() -> str:
    """
    获取当前语言
    
    Returns:
        str: 当前语言代码
    """
    if not _initialized:
        _initialize_language()
    return _current_language


def get_supported_languages() -> Dict[str, str]:
    """
    获取支持的语言列表
    
    Returns:
        Dict[str, str]: 语言代码到语言名称的映射
    """
    return SUPPORTED_LANGUAGES.copy()


def _(message: str) -> str:
    """
    翻译函数
    
    Args:
        message: 要翻译的文本
    
    Returns:
        str: 翻译后的文本
    """
    if not _initialized:
        _initialize_language()
    
    if _translator:
        return _translator.gettext(message)
    else:
        return message


# 不在模块加载时立即初始化，而是延迟到第一次使用时
# 这样可以避免循环导入问题
