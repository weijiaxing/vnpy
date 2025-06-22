# VeighNa 快速开始指南

## 🚀 一键启动

```bash
python run.py
```

## 📋 功能概览

### 已配置网关 (5个)
- 🟡 币安现货网关
- 🔵 OKX交易所网关  
- 🟠 Bybit交易所网关
- 🔷 富途证券网关
- 🔗 RPC网关

### 已安装应用 (16个)
- 📊 CTA策略应用
- 📈 CTA回测应用
- 💼 投资组合策略应用
- 🔀 价差交易应用
- 🤖 算法交易应用
- 📊 期权主控应用
- 🗄️ 数据管理应用
- 📹 数据记录应用
- 📝 脚本交易应用
- 📈 图表分析应用
- ⚠️ 风险管理应用
- 🌐 Web交易应用
- 📊 投资组合管理应用
- 📊 Excel RTD应用
- 🔗 RPC服务应用
- 🎯 模拟交易应用

## ⚙️ 快速配置

### 语言设置
```bash
# 设置中文
python scripts/set_language.py --lang zh_CN

# 设置英文  
python scripts/set_language.py --lang en
```

### 功能测试
```bash
python scripts/test_vnpy.py
```

## 📖 详细文档

- [完整项目架构](PROJECT_STRUCTURE.md)
- [语言配置指南](docs/language/LANGUAGE_SETUP.md)
- [工具脚本说明](scripts/README.md)

## 🔧 常见问题

**Q: 启动时出现模块未安装提示？**
A: 这是正常的，系统会自动跳过未安装的模块，不影响使用。

**Q: 如何添加更多网关？**
A: 安装对应的网关包，然后在 `run.py` 中添加配置即可。

**Q: 如何切换语言？**
A: 使用 `scripts/set_language.py` 脚本或在GUI中通过 系统->全局设置->语言 进行设置。

---
*VeighNa Team - 专业量化交易平台*