# VeighNa 快速入门 (macOS 适配版)

本指南旨在帮助 macOS 用户在 **4.1.0+** 版本上快速搭建并启动环境。

---

## 1. 环境准备 (Conda 独立环境)

在 macOS 上，强烈建议使用专用的虚拟环境以避免依赖冲突。

### 1.1 激活环境
进入项目目录后，运行：
```bash
conda activate ./venv
```
*(如果没有环境，请创建一个 Python 3.11 环境)*

### 1.2 安装核心插件
激活环境后，安装必要的网关和应用插件：
```bash
pip install vnpy_futu vnpy_ctastrategy vnpy_ctabacktester vnpy_sqlite -i https://pypi.vnpy.com
```

> [!TIP]
> **富途网关源码安装**：如果 `pip` 安装 `vnpy_futu` 失败，请尝试：
> `pip install https://github.com/vnpy/vnpy_futu/archive/master.tar.gz`

---

## 2. 脚本运行 (`run.py`)

在 macOS 上，图形化启动可能由于部分底层 C++ 库（如 CTP）不兼容而报错。建议使用已适配的 `run.py`。

### 脚本说明：
- **已移除 CTP**：CTP 官方不提供 Mac 版 SDK。
- **已集成富途 (Futu)**：默认加载富途证券网关。
- **已加载 应用模块**：包含 CTA 策略引擎和回测引擎。

### 启动命令：
```bash
python run.py
```

---

## 3. 常见问题排查 (FAQ)

### Q1: `ModuleNotFoundError: No module named 'vnpy_sqlite'`
**解决**：补全数据库驱动插件。
`pip install vnpy_sqlite -i https://pypi.vnpy.com`

### Q2: 界面启动慢或卡顿
**解决**：macOS 首次加载字体家族别名需要 1-2 秒，请稍候。

### Q3: 无法连接富途行情
**解决**：请确认你的电脑上已经启动并登录了 **FutuOpenD** 客户端。

---

## 4. 后续步骤
- 在 `run.py` 中根据需要添加其他网关（如 OKX, Binance）。
- 在 `MACOS_GUIDE.md` (已合并) 指引下，你可以开始正式的策略开发。
