# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:22:48 2022

@author: Povilas-Predator-PC
"""


import pandas as pd
import numpy as np
end_date = pd.Timestamp('2022-10-18')
td_days = 14
#time_delta = pd.Timedelta(str(td_days)+'days')
#dt_range =  pd.date_range(end_date-time_delta,end_date)

def load_data():
    
#end_date = pd.Timestamp('2022-12-10')
#td_days = 10
    
#import data or run reader
#ticker_list


    df = pd.read_csv('Revolut Stocks List - 1. Revolut stocks list.csv')

    ticker_list = df['Symbol']
    historical_datas = {}

#historical_datas
    for ticker in ticker_list:
        try:
            historical_datas[ticker] = pd.read_csv('ticker_data/'+ticker+'.csv')
        except FileNotFoundError:
            pass
        
    #analyze data for N consequitive weeks of growth
    #staticData.iterrows()
    active_tickers = list(historical_datas)
    return active_tickers,historical_datas



def calc_deltas(active_tickers,historical_datas):
    for ticker in active_tickers:
    
        try:
            historical_datas[ticker]['delta']= historical_datas[ticker]['close'] - historical_datas[ticker]['open']
        except KeyError:
            print(f'Ticker {ticker} missing data')
            pass
        except AssertionError:
            print(f'Ticker {ticker} delisted')
            pass
    return historical_datas

#active_tickers,historical_datas = load_data(end_date, td_days)

#active_tickers = {'ZEN'}


#historical_datas = calc_deltas(active_tickers, historical_datas)




#output suitable tickers


def all_positive(series):
    #expects pandas series object
    positive = 1
   # series = series.fillna(0)
    #series_np = series.to_numpy()
    #indexed_series = series.iloc()
    array = np.array(list(series.items()))
    np.nan_to_num(array)
    array = np.nan_to_num(array)
    suma = 0
    for iii in range(0,len(series)-1):
        #print(series)
        if (array[iii][1] < 0 ):
            positive =0
        else:
            suma += array[iii][1]
    if positive and suma > 1:
            #print(array)
            return 1
    else: 
        return 0


"""        
counter =0
good_tickers ={}
dt_counter =0
d_series = {}

for ticker in active_tickers:
   # pd.date_range(end_date-time_delta,end_date):
        dt_counter =0
        try:
            index_list={}
            delta_series =historical_datas[ticker].to_numpy()
            d_series = {}
            for iii in range(0,len(delta_series[:])):
                for yyy in range(0,td_days-1):
                    if pd.Timestamp(delta_series[iii][0]) == dt_range[yyy]:
                        d_series[dt_counter] = delta_series[iii][8]
                        dt_counter +=1
                        if dt_counter > td_days:
                            dt_counter = td_days
                    
                
                
            if len(d_series) >0:    
                if all_positive(d_series):
                    good_tickers[counter] = ticker
                    counter +=1
                    print (ticker)
            
                
        except KeyError:
            #print(f'Ticker {ticker} missing data')
            pass
        except AssertionError:
            print(f'Ticker {ticker} delisted')
            pass

"""

"""
end_date = pd.Timestamp(end_date)
time_delta = pd.Timedelta(str(td_days)+'days')
dt_range =  pd.date_range(end_date-time_delta,end_date)

active_tickers,historical_datas = load_data(end_date, td_days)

#active_tickers = {'ZEN'}


historical_datas = calc_deltas(active_tickers, historical_datas)
    """
def Analizer(end_date,td_days,historical_datas):
    time_delta = pd.Timedelta(str(td_days)+'days')
    dt_range =  pd.date_range(end_date-time_delta,end_date)
    
    counter =0
    good_tickers ={}
    dt_counter =0
    d_series = {}
    active_tickers = list(historical_datas)
    
    for ticker in active_tickers:
   # pd.date_range(end_date-time_delta,end_date):
        dt_counter =0
        try:
            index_list={}
            delta_series =historical_datas[ticker].to_numpy()
            d_series = {}
            for iii in range(0,len(delta_series[:])):
                for yyy in range(0,td_days-1):
                    if pd.Timestamp(delta_series[iii][0]) == dt_range[yyy]:
                        d_series[dt_counter] = delta_series[iii][8]
                        dt_counter +=1
                        if dt_counter > td_days:
                            dt_counter = td_days
                    
                
                
            if len(d_series) >0:    
                if all_positive(d_series):
                    good_tickers[counter] = ticker
                    counter +=1
                    #print (ticker)
            
                
        except KeyError:
            #print(f'Ticker {ticker} missing data')
            pass
        except AssertionError:
            #print(f'Ticker {ticker} delisted')
            pass
    
    return good_tickers
        
        
#gt = Analizer('2022-10-18',14)
        
        
        
        
        
        
        