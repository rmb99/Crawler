from model.dollar_model import Dollar
from dollar import get_session
from model.config import BaseConfig
import matplotlib.pyplot as plt
import plotly.graph_objects as go

session = get_session(BaseConfig.SQLALCHEMY_DATABASE_URI)


def plot_daily_close_value():
    dollar_value = session.query(Dollar).all()
    close_value = []
    time =[]
    for item in dollar_value:
        close_value.append(item.last)
        time.append(item.miladi_date)

    plt.plot(time[1:], close_value[1:])
    plt.autoscale(time[1:])
    plt.title('Daily close value')
    plt.savefig('./daily_close_value.png')


def candlestick_chart():
    dollar = session.query(Dollar).all()
    time = []
    opening = []
    high = []
    low = []
    close = []
    for item in dollar:
        time.append(item.miladi_date)
        opening.append(item.opening)
        high.append(item.max_price)
        low.append(item.min_price)
        close.append(item.last)

    fig = go.Figure(data=[go.Candlestick(x=time,
                                         open=opening,
                                         high=high,
                                         low=low,
                                         close=close)])
    # fig.show()
    fig.update_layout(title='Daily candlestick chart')
    fig.write_image("candlestick.png")


if __name__ == '__main__':
    plot_daily_close_value()
    candlestick_chart()
