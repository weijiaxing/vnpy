# VeighNa 工具脚本目录

这个目录包含了 VeighNa 的各种实用工具脚本。

## 脚本说明

### 🧪 test_vnpy.py
**功能**: VeighNa 核心功能测试脚本
**用途**: 
- 测试事件引擎和主引擎是否正常工作
- 测试图形界面是否能正常显示
- 验证 VeighNa 安装是否完整

**使用方法**:
```bash
python scripts/test_vnpy.py
```

### 🌍 language_demo.py
**功能**: 语言切换功能演示脚本
**用途**:
- 演示中英文切换功能
- 测试翻译功能
- 交互式语言设置体验

**使用方法**:
```bash
python scripts/language_demo.py
```

**功能特性**:
- 显示当前语言设置
- 列出所有支持的语言
- 交互式语言切换
- 翻译功能演示

### ⚙️ set_language.py
**功能**: 语言设置工具脚本
**用途**:
- 快速设置系统语言
- 支持命令行参数和交互式设置
- 保存语言配置到设置文件

**使用方法**:

**命令行方式**:
```bash
# 设置为中文
python scripts/set_language.py --lang zh_CN

# 设置为英文
python scripts/set_language.py --lang en

# 显示帮助
python scripts/set_language.py --help
```

**交互式方式**:
```bash
python scripts/set_language.py
```

**支持的语言代码**:
- `zh_CN`: 中文（简体）
- `en`: English

## 使用建议

1. **首次安装后**: 运行 `test_vnpy.py` 确保系统正常
2. **语言设置**: 使用 `set_language.py` 快速设置语言
3. **功能演示**: 运行 `language_demo.py` 体验语言切换功能

## 注意事项

- 所有脚本都需要在 VeighNa 项目根目录下运行
- 语言设置会立即生效，但建议重启程序以确保完全生效
- 脚本执行前请确保已正确安装 VeighNa 及其依赖

## 故障排除

如果脚本运行出错，请检查：
1. Python 环境是否正确
2. VeighNa 是否正确安装
3. 依赖包是否完整
4. 是否在正确的目录下运行脚本