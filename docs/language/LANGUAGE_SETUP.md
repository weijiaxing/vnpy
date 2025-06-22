# VeighNa 语言配置说明 / VeighNa Language Configuration

## 概述 / Overview

VeighNa 现在支持动态语言切换功能，可以在中文和英文之间自由切换。

VeighNa now supports dynamic language switching between Chinese and English.

## 支持的语言 / Supported Languages

- `zh_CN`: 中文 (Chinese)
- `en`: English (英文)

## 配置方法 / Configuration Methods

### 1. 通过命令行脚本 / Via Command Line Script

#### 快速设置 / Quick Setup
```bash
# 设置为中文
python set_language.py zh_CN

# 设置为英文  
python set_language.py en

# 查看支持的语言
python set_language.py --list
```

#### 交互式设置 / Interactive Setup
```bash
python set_language.py
```

#### 临时设置（不保存）/ Temporary Setting (Not Saved)
```bash
python set_language.py --temp en
```

### 2. 通过图形界面 / Via GUI

1. 启动 VeighNa 主程序
2. 在菜单栏找到 "语言" 菜单
3. 选择所需语言
4. 重启程序以应用新语言

1. Start VeighNa main program
2. Find "语言" menu in menu bar  
3. Select desired language
4. Restart program to apply new language

### 3. 通过环境变量 / Via Environment Variable

```bash
# 设置环境变量
export VNPY_LANGUAGE=en

# 启动程序
python run.py
```

### 4. 直接编辑配置文件 / Direct Configuration File Edit

编辑 `vt_setting.json` 文件：
```json
{
    "language": "en"
}
```

## 程序功能 / Program Features

### 主要功能 / Main Features

✅ **已完成的功能 / Completed Features:**
- 动态语言切换 / Dynamic language switching
- 配置文件保存 / Configuration file saving  
- 环境变量支持 / Environment variable support
- 图形界面语言菜单 / GUI language menu
- 命令行工具 / Command line tools

### 网关支持 / Gateway Support

✅ **已加载的网关 / Loaded Gateways:**
- 币安现货网关 / Binance Spot Gateway
- OKX交易所网关 / OKX Exchange Gateway  
- Bybit交易所网关 / Bybit Exchange Gateway
- 富途证券网关 / Futu Securities Gateway

### 应用支持 / Application Support

✅ **已加载的应用 / Loaded Applications:**
- CTA策略应用 / CTA Strategy App
- CTA回测应用 / CTA Backtester App
- 数据管理应用 / Data Manager App
- **风险管理应用** / **Risk Manager App** ⭐
- **投资组合管理应用** / **Portfolio Manager App** ⭐  
- 模拟交易应用 / Paper Account App

## 使用示例 / Usage Examples

### 示例1: 快速切换到英文 / Example 1: Quick Switch to English
```bash
python set_language.py en
python run.py
```

### 示例2: 测试语言功能 / Example 2: Test Language Features  
```bash
python language_demo.py
```

### 示例3: 查看当前配置 / Example 3: Check Current Configuration
```bash
python -c "from vnpy.trader.locale import get_current_language; print(f'当前语言: {get_current_language()}')"
```

## 故障排除 / Troubleshooting

### 常见问题 / Common Issues

1. **语言切换后界面没有变化 / UI doesn't change after language switch**
   - 解决方案：重启程序 / Solution: Restart the program

2. **找不到翻译文件 / Translation files not found**
   - 检查 `vnpy/trader/locale/en/LC_MESSAGES/` 目录
   - Check `vnpy/trader/locale/en/LC_MESSAGES/` directory

3. **设置不保存 / Settings not saved**
   - 检查 `vt_setting.json` 文件权限
   - Check `vt_setting.json` file permissions

### 重置配置 / Reset Configuration
```bash
# 删除配置文件，恢复默认设置
rm vt_setting.json

# 重新设置语言
python set_language.py zh_CN
```

## 开发者信息 / Developer Information

### 文件结构 / File Structure
```
vnpy/
├── trader/
│   ├── locale/
│   │   ├── __init__.py          # 语言切换核心功能
│   │   ├── en/LC_MESSAGES/      # 英文翻译文件
│   │   └── vnpy.pot             # 翻译模板
│   ├── setting.py               # 全局设置
│   └── ui/mainwindow.py         # 主窗口（包含语言菜单）
├── run.py                       # 主启动文件
├── set_language.py              # 语言设置工具
├── language_demo.py             # 语言功能演示
└── LANGUAGE_SETUP.md            # 本说明文档
```

### API 接口 / API Interface
```python
from vnpy.trader.locale import (
    switch_language,           # 切换语言
    get_current_language,      # 获取当前语言
    get_supported_languages,   # 获取支持的语言列表
    _                         # 翻译函数
)

# 使用示例
switch_language("en")
current = get_current_language()
translated = _("系统")  # 返回 "System" 或 "系统"
```

## 更新日志 / Changelog

### v1.0.0 (2024-12-19)
- ✅ 实现基础语言切换功能
- ✅ 添加图形界面语言菜单
- ✅ 创建命令行设置工具
- ✅ 集成风险管理和投资组合管理应用
- ✅ 完善网关配置和加载

---

**注意 / Note:** 语言切换功能需要重启程序才能完全生效。/ Language switching requires program restart to take full effect.