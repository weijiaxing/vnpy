# VeighNa Trader 语言配置指南

## 概述

VeighNa Trader现在支持完整的中英文动态切换功能，语言设置会自动保存并在重启后保持。本指南介绍如何使用这些功能。

## 🆕 新功能特性

### 1. 自动语言检测与加载
- **智能检测**：程序启动时自动检测并加载语言设置
- **优先级顺序**：配置文件 > 环境变量 > 系统语言 > 默认中文
- **持久化保存**：语言设置自动保存到配置文件中

### 2. 全局设置集成
- **统一配置**：语言设置已集成到全局设置对话框中
- **可视化选择**：使用下拉菜单选择语言，无需手动输入
- **即时生效**：设置后立即切换语言并保存

### 3. 完整的翻译支持
- **界面翻译**：菜单、按钮、对话框等界面元素完全翻译
- **动态切换**：运行时可以切换语言，重启后界面更新

## 🎯 使用方法

### 方法一：通过全局设置（推荐）

1. **打开全局设置**
   - 在主窗口菜单栏点击 "配置" 或 "Settings"
   - 或者点击 "语言设置" / "Language Settings"

2. **选择语言**
   - 在设置对话框中找到 "language <语言选择>" 字段
   - 从下拉菜单中选择：
     - `中文 (简体)` - 中文界面
     - `English` - 英文界面

3. **保存设置**
   - 点击 "确定" 按钮
   - 系统会提示语言已立即生效，但界面需要重启后更新

4. **重启程序**
   - 关闭VeighNa Trader
   - 重新运行程序，界面将显示为选定的语言

### 方法二：通过命令行工具

```bash
# 使用语言设置工具
python set_language.py

# 或者直接指定语言
python set_language.py zh_CN  # 设置为中文
python set_language.py en     # 设置为英文
```

### 方法三：通过环境变量

```bash
# 设置环境变量（临时）
export VNPY_LANGUAGE=en
python run.py

# 或者在运行时指定
VNPY_LANGUAGE=zh_CN python run.py
```

## 🔧 技术细节

### 支持的语言

| 语言代码 | 语言名称 | 状态 |
|---------|---------|------|
| `zh_CN` | 中文 (简体) | ✅ 完全支持 |
| `en` | English | ✅ 完全支持 |

### 配置文件位置

语言设置保存在 VeighNa 的配置文件中：
- 文件名：`.vntrader/vt_setting.json`
- 字段名：`"language"`
- 可选值：`"zh_CN"` 或 `"en"`

### 翻译文件位置

英文翻译文件位于：
```
vnpy/trader/locale/en/LC_MESSAGES/
├── vnpy.po  # 翻译源文件
└── vnpy.mo  # 编译后的翻译文件
```

## 🛠 开发者信息

### API 接口

```python
from vnpy.trader.locale import (
    switch_language,        # 切换语言
    get_current_language,   # 获取当前语言
    get_supported_languages,# 获取支持的语言列表
    _                      # 翻译函数
)

# 切换语言
success = switch_language("en")

# 获取当前语言
current = get_current_language()  # 返回 "zh_CN" 或 "en"

# 获取支持的语言
languages = get_supported_languages()
# 返回: {"zh_CN": "中文 (简体)", "en": "English"}

# 翻译文本
translated = _("系统")  # 中文模式返回 "系统"，英文模式返回 "System"
```

### 初始化流程

1. **模块加载时**：自动调用 `_initialize_language()`
2. **语言检测**：按优先级检测应使用的语言
3. **翻译器加载**：根据检测结果加载相应的翻译器
4. **设置保存**：语言切换时自动保存到配置文件

## 🧪 测试工具

### 语言功能测试

```bash
# 运行完整的语言功能测试
python test_language_persistence.py

# 运行交互式语言演示
python language_demo.py
```

### 测试内容

- ✅ 语言设置持久化
- ✅ 重启后语言加载
- ✅ 翻译功能正确性
- ✅ 配置文件读写
- ✅ 环境变量支持

## 🔍 故障排除

### 常见问题

1. **重启后语言设置丢失**
   - ✅ 已修复：现在语言设置会自动保存并在重启后加载

2. **翻译不生效**
   - 检查翻译文件是否存在：`vnpy/trader/locale/en/LC_MESSAGES/vnpy.mo`
   - 确认当前语言设置：运行 `python -c "from vnpy.trader.locale import get_current_language; print(get_current_language())"`

3. **界面没有更新**
   - 语言切换后需要重启程序才能看到界面更新
   - 确认已经保存了设置并重启了程序

### 调试信息

程序启动时会在控制台显示语言初始化信息：
```
Language initialized: zh_CN (中文 (简体))
```

语言切换时会显示：
```
Language switched to en and saved to settings
```

## 📝 更新日志

### v2.0 (当前版本)
- ✅ 修复重启后语言配置丢失问题
- ✅ 将语言配置集成到全局设置对话框
- ✅ 简化语言菜单，提供更直观的设置方式
- ✅ 改进语言检测和加载逻辑
- ✅ 添加完整的测试工具和文档

### v1.0 (之前版本)
- ✅ 基础的中英文切换功能
- ✅ 菜单栏语言选择
- ✅ 翻译功能实现

## 🎉 总结

现在VeighNa Trader的语言配置功能已经完全集成到系统中，提供了：

1. **无缝的用户体验**：像字体大小一样，语言可以在全局设置中轻松配置
2. **可靠的持久化**：设置会自动保存，重启后正确加载
3. **智能的自动检测**：程序会智能检测和应用最合适的语言设置
4. **完整的开发者支持**：提供了完整的API和测试工具

用户现在可以轻松地在中英文之间切换，享受本地化的交易体验！ 