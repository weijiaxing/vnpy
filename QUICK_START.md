# VeighNa (vn.py) 快速入门 & 硬盘迁移指南

本文档总结了当前环境的配置细节，并指导如何在更换 Mac 电脑（通过 SSD 移动存储）后快速恢复交易环境。

## 1. 当前环境状态总结

- **工作目录**: `/Volumes/T7_Work_Data/Current_Work/workspace/invest/vnpy`
- **虚拟环境**: 已配置 Python 3.11 虚拟环境 (`./venv`)，安装了 `vnpy`, `vnpy_futu`, `vnpy_ctastrategy`, `vnpy_ctabacktester`。
- **核心修复**: 我们已修改 `venv` 内的 `vnpy_ctastrategy` 和 `vnpy_ctabacktester` 引擎源码。
  - **功能**: 引擎会自追踪 `run.py` 的物理路径，自动加载项目根目录下 `strategies/` 文件夹中的策略。
  - **意义**: 彻底解决了 macOS 下因 CWD（当前工作目录）偏差导致的策略无法加载问题。

## 2. 迁移到另一台 Mac 的步骤

如果你将 SSD 插到另一台新的 Mac 上，请按以下步骤操作：

### 第一步：确保 Python 环境一致
1. 新 Mac 建议安装 **Python 3.11**。
2. 在终端进入 SSD 的项目目录：
   ```bash
   cd /Volumes/T7_Work_Data/Current_Work/workspace/invest/vnpy
   ```
3. 激活现有的虚拟环境（注意：由于环境是 Conda 前缀环境，必须使用以下命令）：
   ```bash
   conda activate ./venv
   ```
   或者如果你的 conda 未初始化环境：
   ```bash
   source activate ./venv
   ```

### 第二步：检查路径依赖
由于我们在核心引擎里使用了“物理路径检测”，只要你在 SSD 上运行 `python run.py`，它就会自动找到 SSD 上的策略文件夹，**无需修改任何代码**。

### 第三步：运行与连接
1. 确保新 Mac 上安装并运行了 **FutuOpenD** 且已登录。
2. 执行启动脚本：
   ```bash
   python run.py
   ```

---

## 3. 如何新增策略？

想要增加业务逻辑，遵循以下三步即可：

1. **创建文件**: 在 `strategies/` 目录下新建 `.py` 文件（例如 `my_new_strategy.py`）。
2. **继承模版**: 确保你的类继承自 `CtaTemplate`，可以参考 `boll_rsi_strategy.py`。
   ```python
   from vnpy_ctastrategy import CtaTemplate
   
   class MyNewStrategy(CtaTemplate):
       # 你的逻辑...
       pass
   ```
3. **重启加载**: 保存文件后，直接重启 `run.py`。新策略将自动出现在 **CTA策略** 和 **CTA回测** 的下拉列表中。

---

## 4. 故障排除（如果换了电脑策略又不显示了）

如果在别的电脑上你**重新安装**了 `vnpy` 相关的库（而不是使用 SSD 上的 `venv`），加载逻辑会被还原。此时只需运行我为你准备的“修复引擎”补丁（即再次执行我们之前的 `sys.argv` 路径修改逻辑）即可恢复自动加载功能。

> [!IMPORTANT]
> **永远优先使用 SSD 上的 `./venv`**，它是目前唯一处于“已手术修复”状态的环境。
