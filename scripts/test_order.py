#!/usr/bin/env python3
"""
测试下单脚本
============

这个脚本将帮助您测试下单功能

使用前请确保:
1. VeighNa已启动并连接到交易所
2. 账户有足够余额
3. API权限设置正确
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.object import OrderRequest
from vnpy.trader.constant import Direction, OrderType, Exchange

def test_order():
    """测试下单功能"""
    print("🧪 开始测试下单功能...")
    
    # 创建引擎
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    # 这里需要您手动添加和连接网关
    print("请确保已在VeighNa主界面连接到交易所")
    print("然后运行此脚本进行测试")
    
    # 测试订单参数
    order_req = OrderRequest(
        symbol="BTC-USDT",
        exchange=Exchange.OKX,
        direction=Direction.LONG,
        type=OrderType.LIMIT,
        volume=0.001,  # 小额测试
        price=50000,   # 请根据当前价格调整
    )
    
    print(f"测试订单: {order_req.symbol} {order_req.direction.value} {order_req.volume}")
    print("⚠️ 这只是测试脚本，实际下单请在VeighNa界面操作")

if __name__ == "__main__":
    test_order()
