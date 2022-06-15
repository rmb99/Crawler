from app.dollar_model import Dollar
from dollar import get_session
from app.config import BaseConfig
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mpl_dates

session = get_session(BaseConfig.SQLALCHEMY_DATABASE_URI)
def plot_daily_close_value():
    dollar_value = session.query(Dollar).all()
    close_value = []
    time =[]
    for item in dollar_value:
        close_value.append(item.last)
        time.append((item.miladi_date))

    plt.plot(time[1:], close_value[1:])
    plt.autoscale(time[1:])
    plt.title('Daily close value')
    plt.savefig('./daily_close_value.png')

def candlestick_chart():
    dollar_value = session.query(Dollar).all()
    time = []
    for item in dollar_value:

    fig, ax = plt.subplots()

    candlestick_ohlc(ax, item.values, width=0.6, colorup='green', colordown='red', alpha=0.8

if __name__ == '__main__':
    plot_daily_close_value()