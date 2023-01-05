from datetime import datetime
import yfinance as yf
import backtrader as bt

class MyStrategy(bt.Strategy):
        def __init__(self):
                self.rsi = bt.indicators.RSI(self.data.close)
        def next(self):
                if not self.position:
                        if self.rsi<30:
                                self.order = self.buy()
                        else:
                                if self.rsi > 70:
                                        self.order = self.sell()

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
