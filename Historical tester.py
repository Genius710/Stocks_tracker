# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 12:25:35 2022

@author: Povilas-Predator-PC
"""

#run analizer with variable current date simulating withdrawal after N days
from Analizer import Analizer,load_data,calc_deltas,all_positive
#import Analizer
import pandas as pd
import numpy as np
price = pd.DataFrame(columns={'ticker','sell','buy'})
price.set_index('ticker')


end_date = pd.Timestamp('2022-12-10')
td_days = 14
time_delta = pd.Timedelta(str(td_days)+'days')
dt_range =  pd.date_range(end_date-time_delta,end_date)


active_tickers,historical_datas = load_data()
historical_datas = calc_deltas(active_tickers, historical_datas)





    
#gt = Analizer(end_date,td_days,historical_datas)
price_list = {}
for iii in range(17,30):
    end_date = pd.Timestamp('2022-11-'+str(iii))
    td_days = 14
    time_delta = pd.Timedelta(str(td_days)+'days')
    dt_range =  pd.date_range(end_date-time_delta,end_date)
    print(end_date)

    gt = Analizer(end_date,td_days,historical_datas)
    
    price = pd.DataFrame(columns={'ticker','sell','buy'})        
    for xxx in range(0,len(gt)-1): 
        if len(gt)> 0: 
            sell_date = end_date+ pd.Timedelta('5days')
            sell_date = sell_date.strftime('%Y-%m-%d')
            
            date_index =  historical_datas[gt[xxx]]['Unnamed: 0']
            
            # find sell price
            idx = -1
            while idx == -1:
                for iii in range(0,len(date_index)-1):
                    if date_index[iii] == sell_date:
                        idx = iii
                sell_date = pd.Timestamp(sell_date)
                sell_date = sell_date+ pd.Timedelta('1days')
                sell_date = sell_date.strftime('%Y-%m-%d')
            
            
            
            #price.append({'ticker': gt[0],'sell' : historical_datas[gt[0]]['close'][idx]},ignore_index =True)
            
            #) 
            
            # find buy price
            buy_date = end_date+ pd.Timedelta('1days')
            buy_date = buy_date.strftime('%Y-%m-%d')
            
            idxb = -1
            while idxb == -1:
                for iii in range(0,len(date_index)-1):
                    if date_index[iii] == buy_date:
                        idxb = iii
                buy_date = pd.Timestamp(buy_date)
                buy_date = buy_date+ pd.Timedelta('1days')
                buy_date = buy_date.strftime('%Y-%m-%d')
              
               
            price = price.append({'ticker': gt[xxx],'sell' : historical_datas[gt[xxx]]['close'][idx],'buy' : historical_datas[gt[xxx]]['close'][idxb]},ignore_index =True)
        #price['ratio'][gt[xxx]] = price['sell'][gt[xxx]] / price['buy'][gt[xxx]] 
    if len(gt)> 0:
        price = price[['ticker', 'buy','sell']]
        price_np = np.c_[ price.to_numpy(), np.ones([len(gt)-1,2]) ]
    
    
        for xxx in range(0,len(price_np)):
            price_np[xxx][3] =  1-(price_np[xxx][1] / price_np[xxx][2])
            price_np[xxx][4] =  price_np[xxx][2] - price_np[xxx][1]
    if(price_np):
        print(price_np)
        price_list[iii] = price_np

#def Analizer(end_date,td_days,historical_datas):