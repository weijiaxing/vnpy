# VeighNa 项目架构文档

## 项目概述

VeighNa 是一个基于Python的开源量化交易平台，提供完整的交易系统解决方案。

## 目录结构

### 根目录文件

```
vnpy/
├── run.py                     # 🚀 主启动脚本（支持多网关多应用）
├── pyproject.toml            # 📦 项目配置和依赖管理
├── README.md                 # 📖 中文说明文档
├── README_ENG.md            # 📖 英文说明文档
├── CHANGELOG.md             # 📝 版本更新日志
├── LICENSE                  # ⚖️ 开源许可证
├── .gitignore               # 🚫 Git忽略文件配置
├── install.sh               # 🐧 Linux安装脚本
├── install.bat              # 🪟 Windows安装脚本
└── install_osx.sh           # 🍎 macOS安装脚本
```

### 核心代码目录

```
vnpy/                        # 🎯 核心代码包
├── __init__.py             # 包初始化文件
├── trader/                 # 💼 交易核心模块
│   ├── __init__.py
│   ├── engine.py          # 🔧 主引擎
│   ├── gateway.py         # 🌉 网关接口
│   ├── object.py          # 📊 数据对象定义
│   ├── constant.py        # 📋 常量定义
│   ├── event.py           # 📡 事件定义
│   ├── database.py        # 🗄️ 数据库操作
│   ├── datafeed.py        # 📈 数据源接口
│   ├── setting.py         # ⚙️ 全局设置
│   ├── utility.py         # 🛠️ 工具函数
│   ├── converter.py       # 🔄 数据转换
│   ├── optimize.py        # 📊 优化算法
│   ├── logger.py          # 📝 日志系统
│   ├── app.py            # 📱 应用管理
│   ├── locale/           # 🌍 国际化支持
│   │   ├── __init__.py   # 语言切换核心功能
│   │   ├── vnpy.pot      # 翻译模板
│   │   └── en/           # 英文翻译
│   └── ui/               # 🖥️ 图形界面
│       ├── __init__.py
│       ├── qt.py         # Qt基础组件
│       ├── mainwindow.py # 主窗口
│       ├── widget.py     # 通用组件
│       └── ico/          # 图标资源
├── event/                  # 📡 事件引擎
│   ├── __init__.py
│   └── engine.py          # 事件处理核心
├── chart/                  # 📈 图表组件
│   ├── __init__.py
│   ├── base.py           # 图表基类
│   ├── manager.py        # 图表管理器
│   ├── widget.py         # 图表组件
│   ├── item.py           # 图表元素
│   └── axis.py           # 坐标轴
├── rpc/                    # 🔗 RPC通信
│   ├── __init__.py
│   ├── server.py         # RPC服务端
│   ├── client.py         # RPC客户端
│   └── common.py         # 通用功能
└── alpha/                  # 🧮 量化研究
    ├── __init__.py
    ├── lab.py            # 研究实验室
    ├── logger.py         # 研究日志
    ├── dataset/          # 数据集处理
    ├── model/            # 机器学习模型
    └── strategy/         # Alpha策略
```

### 示例代码目录

```
examples/                    # 📚 示例代码
├── veighna_trader/         # 🎯 基础交易示例
│   ├── run.py             # 标准启动脚本
│   └── demo_script.py     # 演示脚本
├── no_ui/                  # 🖥️ 无界面运行示例
├── cta_backtesting/        # 📊 CTA策略回测
├── portfolio_backtesting/  # 📈 投资组合回测
├── spread_backtesting/     # 🔀 价差交易回测
├── alpha_research/         # 🧮 Alpha因子研究
├── notebook_trading/       # 📓 Jupyter交易示例
├── data_recorder/          # 📹 数据记录示例
├── download_bars/          # 📥 K线数据下载
├── candle_chart/          # 🕯️ K线图表示例
├── client_server/         # 🔗 客户端服务器示例
└── simple_rpc/            # 📡 简单RPC示例
```

### 文档目录

```
docs/                       # 📖 文档目录
├── community/             # 👥 社区版文档
│   ├── install/          # 🔧 安装指南
│   ├── info/             # ℹ️ 基础信息
│   └── app/              # 📱 应用说明
├── elite/                 # 💎 专业版文档
│   ├── info/             # ℹ️ 专业版信息
│   ├── strategy/         # 📊 策略文档
│   └── extension/        # 🔌 扩展功能
├── language/             # 🌍 语言配置文档
│   ├── LANGUAGE_SETUP.md # 语言设置指南
│   └── LANGUAGE_CONFIGURATION_GUIDE.md # 配置指南
└── conf.py               # 📝 文档配置
```

### 工具脚本目录

```
scripts/                    # 🛠️ 工具脚本
├── test_vnpy.py           # 🧪 功能测试脚本
├── language_demo.py       # 🌍 语言切换演示
└── set_language.py        # ⚙️ 语言设置工具
```

## 核心功能模块

### 1. 交易引擎 (trader/)
- **主引擎 (engine.py)**: 系统核心，管理所有模块
- **网关接口 (gateway.py)**: 连接各种交易接口
- **数据对象 (object.py)**: 定义交易数据结构
- **事件系统 (event.py)**: 处理系统内部通信

### 2. 图形界面 (ui/)
- **主窗口 (mainwindow.py)**: 主要用户界面
- **通用组件 (widget.py)**: 可复用的UI组件
- **国际化支持**: 中英文界面切换

### 3. 数据管理
- **数据库 (database.py)**: 数据持久化
- **数据源 (datafeed.py)**: 外部数据接入
- **数据转换 (converter.py)**: 格式转换

### 4. 策略框架
- **CTA策略**: 趋势跟踪策略
- **投资组合策略**: 多资产组合管理
- **价差交易**: 套利策略
- **算法交易**: 执行算法

## 支持的交易接口

### 数字货币交易所
- 🟡 **币安 (Binance)**: 现货、合约交易
- 🔵 **OKX**: 全品种交易
- 🟠 **Bybit**: 衍生品交易

### 传统金融
- 🔷 **富途证券 (Futu)**: 港美股交易
- 🟦 **Interactive Brokers**: 全球市场
- 🔶 **CTP**: 期货交易（需单独安装）

### 其他接口
- 🔗 **RPC网关**: 分布式部署
- 🎯 **模拟交易**: 纸上交易测试

## 应用生态

### 策略应用
- **CTA策略**: 技术分析策略
- **投资组合策略**: 多因子模型
- **价差交易**: 统计套利
- **算法交易**: 智能执行

### 数据应用
- **数据管理**: 历史数据管理
- **数据记录**: 实时数据采集
- **图表分析**: K线技术分析

### 工具应用
- **脚本交易**: 自定义交易脚本
- **风险管理**: 实时风控
- **Web交易**: 网页端交易
- **Excel RTD**: Excel数据接口

## 快速开始

### 1. 启动系统
```bash
python run.py
```

### 2. 语言设置
```bash
# 使用脚本设置语言
python scripts/set_language.py --lang zh_CN

# 或在GUI中通过 系统 -> 全局设置 -> 语言 进行设置
```

### 3. 功能测试
```bash
python scripts/test_vnpy.py
```

## 配置说明

### 全局设置文件
- 位置: `~/.vntrader/vt_setting.json`
- 包含: 数据库配置、语言设置、字体配置等

### 语言配置
- 支持语言: 中文(zh_CN)、英文(en)
- 配置方式: GUI设置、配置文件、环境变量
- 环境变量: `VNPY_LANGUAGE=zh_CN`

## 开发指南

### 添加新网关
1. 继承 `BaseGateway` 类
2. 实现必要的接口方法
3. 在 `run.py` 中注册

### 添加新应用
1. 继承 `BaseApp` 类
2. 实现应用逻辑
3. 在应用列表中注册

### 国际化支持
1. 使用 `_()` 函数包装文��
2. 更新翻译文件
3. 重新生成 mo 文件

## 版本信息

- **当前版本**: VeighNa 4.1.0
- **Python版本**: 3.10+
- **GUI框架**: PySide6
- **数据库**: SQLite/MongoDB/InfluxDB

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

---

*最后更新: 2024-12-22*
*文档版本: 1.0*