# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:05:18 2022

@author: Povilas-Predator-PC
"""

from yahoo_fin.stock_info import get_data

amazon_weekly= get_data("amzn", start_date="12/04/2009", end_date="12/04/2019", index_as_date = True, interval="1wk")

ticker_list = ["amzn","enph","msft"]



        
import pandas as pd

df = pd.read_csv('Revolut Stocks List - 1. Revolut stocks list.csv')

ticker_list = df['Symbol']
historical_datas = {}
#for ticker in ticker_list:
#        historical_datas[ticker] = get_data(ticker, start_date="12/11/2022", end_date="15/12/2022", index_as_date = True, interval="1d")


for ticker in ticker_list:
    try:
        historical_datas[ticker] = get_data(ticker, start_date="01/01/2023", end_date="06/18/2023", index_as_date = True, interval="1d")
    except KeyError:
        print(f'Ticker {ticker} missing data')
        pass
    except AssertionError:
        print(f'Ticker {ticker} delisted')
        pass
    
for ticker in ticker_list:
    try:
        historical_datas[ticker].to_csv('ticker_data/'+ticker+'.csv')
    except KeyError:
        print(f'Ticker {ticker} missing data')
        pass
    except AssertionError:
        print(f'Ticker {ticker} delisted')
        pass