# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 20:59:07 2022

@author: Povilas-Predator-PC
"""

if len(gt)> 0: 
    sell_date = end_date+ pd.Timedelta('10days')
    sell_date = sell_date.strftime('%Y-%m-%d')
    
    date_index =  historical_datas[gt[0]]['Unnamed: 0']
    
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
            if date_index[iii] == sell_date:
                idxb = iii
        buy_date = pd.Timestamp(buy_date)
        buy_date = buy_date+ pd.Timedelta('1days')
        buy_date = buy_date.strftime('%Y-%m-%d')
        
for xxx in range(0,len(gt)-1):        
    price = price.append({'ticker': gt[xxx],'sell' : historical_datas[gt[xxx]]['close'][idx],'buy' : historical_datas[gt[xxx]]['close'][idxb]},ignore_index =True)
    #price['ratio'][gt[xxx]] = price['sell'][gt[xxx]] / price['buy'][gt[xxx]] 
    price_np = np.c_[ price.to_numpy(), np.ones(16) ]


for xxx in range(len(price_np)):
    price_np[xxx][3] =  price_np[xxx][2] / price_np[xxx][1]