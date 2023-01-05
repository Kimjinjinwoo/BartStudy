from datetime import datetime
import yfinance as yf
import backtrader as bt

class MyStrategy(bt.Strategy):
        def __init__(self):
                self.dataclose = self.datas[0].close
                self.order = None
                self.buyprice = None
                self.buycomm = None
                self.rsi = bt.indicators.RSI(self.data.close)

        def notify_order(self , order):
                if order.status in [order.Submitted , order.Accepted]:
                        return
                if order.status in [order.Completed]:
                        if order.isbuy():       
                                self.log(f'BUY  : 주가 {order.executed.price:,.0f}, '
                                         f'수량 {order.executed.size:,.0f}, '
                                         f'수수료 {order.executed.comm:,.0f}, '
                                         f'자산 {cerebro.broker.getvalue():,.0f}')
                                self.buyprice = order.executed.price
                                self.buycomm = order.executed.comm
                        else:
                                self.log(f'SELL : 주가 {order.executed.price:,.0f}, '
                                         f'수량 {order.executed.size:,.0f}, '
                                         f'수수료 {order.executed.comm:,.0f}, '
                                         f'자산 {cerebro.broker.getvalue():,.0f}')
                        self.bar_executed = len(self)
                elif order.status in [order.Canceled]:
                        self.log('ORDER CANCELED')
                elif order.status in [order.Margin]:
                        self.log('ORDER MARGIN')
                elif order.status in [order.Rejected]:
                        self.log('ORDER REJECTED')
                self.order = None
                                                
        
        def next(self):
                if not self.position:
                        if self.rsi<30:
                                self.order = self.buy()
                        else:
                                if self.rsi > 70:
                                        self.order = self.sell()

        def log(self , txt , dt = None):
                dt = self.datas[0].datetime.date(0)
                print(f'[{dt.isoformat()}] {txt}')

cerebro = bt.Cerebro()
cerebro.addstrategy(MyStrategy)
data = bt.feeds.PandasData(dataname = yf.download('036570.KS' , '2021-01-01' , '2022-01-01'))
cerebro.adddata(data)
cerebro.broker.setcash(10000000)
cerebro.addsizer(bt.sizers.SizerFix, stake = 30)

print(f'Initial Portfolio Value : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.run()
print(f'slack_sendmessage.py    : {cerebro.broker.getvalue():,.0f} KRW')
cerebro.plot()
