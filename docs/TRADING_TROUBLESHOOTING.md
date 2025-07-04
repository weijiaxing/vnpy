# VeighNa 下单委托故障排除指南

## 🎯 问题现象
- 网关连接正常 ✅
- 能看到行情数据 ✅
- 能看到账户资金 ✅
- 但是下单委托失败 ❌

## 🔍 原因分析与解决方案

### 1. API权限不足 (最常见原因 - 80%)

#### 症状表现：
- 连接成功，数据正常
- 下单时没有反应或报错
- 委托栏始终为空

#### 解决步骤：
1. **登录交易所网站检查API权限**
   ```
   OKX: https://www.okx.com → API管理
   币安: https://www.binance.com → API管理
   ```

2. **确认必要权限已开启**
   ```
   ✅ Read (读取权限) - 必须
   ✅ Trade (交易权限) - 必须  
   ❌ Withdraw (提币权限) - 不推荐
   ```

3. **检查IP白名单设置**
   ```
   - 如果设置了IP白名单，确保当前IP在列表中
   - 建议：先不设IP限制，测试成功后再设置
   ```

### 2. 交易对格式错误 (15%)

#### OKX正确格式：
```
✅ BTC-USDT (现货)
✅ ETH-USDT (现货)
✅ BTC-USDT-SWAP (永续合约)
❌ BTCUSDT (错误格式)
❌ BTC/USDT (错误格式)
```

#### 币安正确格式：
```
✅ BTCUSDT (现货)
✅ ETHUSDT (现货)
❌ BTC-USDT (错误格式)
```

### 3. 订单参数错误 (5%)

#### 常见参数问题：
```
价格问题：
- 限价单价格偏离市价太远
- 价格精度不符合要求

数量问题：
- 低于最小交易单位
- 超过账户可用余额
- 数量精度不正确
```

## 🛠️ 分步排查流程

### 步骤1：API权限验证
```bash
# 运行API测试脚本
python scripts/test_okx_connection.py
```

### 步骤2：重新连接网关
1. 在VeighNa界面断开连接
2. 等待5秒
3. 重新输入API信息并连接

### 步骤3：测试小额订单
```
推荐测试参数：
交易所：GLOBAL
代码：BTC-USDT
方向：多
类型：市价
数量：0.001 (约50-100美元)
```

### 步骤4：检查日志信息
在VeighNa日志窗口查看：
- 是否有错误信息
- API调用是否成功
- 订单状态变化

## 🎯 快速解决检查清单

### 立即检查项目：
- [ ] API交易权限已开启
- [ ] 交易对格式正确 (OKX用"-"，币安不用)
- [ ] 账户USDT余额充足
- [ ] 网关连接状态正常
- [ ] 订单参数合理
- [ ] 查看日志错误信息

### OKX专用检查：
- [ ] 交易所选择：GLOBAL
- [ ] 代码格式：BTC-USDT
- [ ] 服务器选择：aws (推荐)
- [ ] API权限：Read + Trade

## 🚨 紧急修复方案

### 方案A：重新创建API
1. 删除当前API密钥
2. 创建新的API密钥
3. 确保开启Trade权限
4. 重新在VeighNa中配置

### 方案B：切换到模拟交易
1. 启用模拟交易应用
2. 先在模拟环境测试
3. 确认功能正常后再用实盘

### 方案C：使用其他网关
1. 如果OKX有问题，可以尝试币安
2. 币安配置相对简单
3. 作为备选方案

## 📞 获取技术支持

如果以上方案都无法解决，请提供：

1. **VeighNa日志截图** (重要)
2. **API权限设置截图**
3. **下单参数设置截图**
4. **具体错误信息**

### 常见错误代码：
```
51008: 余额不足
51024: 账户权限不足
51001: 交易对不存在
51004: 订单参数错误
```

## 🎉 成功标志

下单成功的标志：
- 委托栏出现订单记录
- 日志显示订单提交成功
- 账户余额发生变化
- 可以看到订单状态更新

---
**提示**: 建议先用小额测试，确认功能正常后再进行正式交易。 