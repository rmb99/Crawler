import datetime
import requests
from bs4 import BeautifulSoup
from persiantools.jdatetime import JalaliDate
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model.config import BaseConfig
from model.dollar_model import Dollar

Base = declarative_base()


def get_session(conn_string):
    db = create_engine(conn_string)
    session = sessionmaker(db)
    return session()


def get_response(url):
    responses = requests.get(url)
    return responses.json()


def build_url():
    api = 'https://api.accessban.com/v1/market/indicator/summary-table-data/price_dollar_rl?length=500&start=0'
    return api


def format_shamsi_date(date):
    date_list = date.split('/')

    year = int(date_list[0])
    month =int(date_list[1])
    day = int(date_list[2])
    return JalaliDate(year, month, day)


def format_miladi_date(date):
    date_list = date.split('/')
    if len(date_list)>0:
        year = int(date_list[0])
        month = int(date_list[1])
        day = int(date_list[2])
        date_time = datetime.datetime(year, month, day)
    else:
        date_time = None
    return date_time


def populate(data):
    data_list = []
    for _list in data:

        opening = _list[0]
        min_price = _list[1]
        max_price = _list[2]
        last = _list[3]
        bs1 = BeautifulSoup(_list[4])
        change = bs1.find('span', {'dir': 'ltr'}).text
        try:
            change = float(change)
        except ValueError:
            change = 0
        bs2 = BeautifulSoup(_list[5])
        bs2_find_number = bs2.find('span', {'dir': 'ltr'})
        postive_change = bs2.find('span', {'class': 'high'})
        negetive_change = bs2.find('span', {'class': 'high'})
        if bs2_find_number:
            percent_change = bs2.text.replace('%', '')
        else:
            percent_change = 0
        if negetive_change:
            percent_change = -float(percent_change)

        shamsi_date = _list[7]
        shamsi_date_iso = format_shamsi_date(shamsi_date)

        miladi_date = _list[6]
        miladi_date_iso = format_miladi_date(miladi_date)

        data_list.append({
            'opening': float(opening.replace(',', '.')),
            'min_price': float(min_price.replace(',', '.')),
            'max_price': float(max_price.replace(',', '.')),
            'change': change,
            'percent_change': float(percent_change),
            'shamsi_date': shamsi_date_iso,
            'miladi_date': miladi_date_iso,
            'last': float(last.replace(',', '.'))

        })
    return data_list


def save_date(data_list):
    session = get_session(BaseConfig.SQLALCHEMY_DATABASE_URI)
    session.begin()

    for data in data_list:
        dollar = Dollar()
        dollar.max_price = data.get('max_price')
        dollar.min_price = data.get('min_price')
        dollar.change = data.get('change')
        dollar.percent_change = data.get('percent_change')
        dollar.last = data.get('last')
        dollar.opening = data.get('opening')
        # dollar.shamsi_date = data.get('shamsi_date')
        dollar.miladi_date = data.get('miladi_date')

        session.add(dollar)
    session.commit()


def execute():
    url = build_url()
    data = get_response(url)
    data = data['data']
    data_list = populate(data)
    print('start saving')
    save_date(data_list)
    print('saved')


if __name__ == '__main__':
    execute()













