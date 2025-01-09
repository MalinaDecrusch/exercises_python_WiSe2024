# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:41:46 2024

@author: s_decrusch22
"""

import pandas as pd


data_frames = {}

for file_name in file_names:
    file_path = f'data/{file_name}.csv'
    data_frames[file_name] = pd.read_csv(file_path)
    
aapl_data = data_frames['AAPL'][['Date', 'Close']].rename(
    columns = {'Close':'AAPL'})
goog_data = data_frames['GOOG'][['Date', 'Close']].rename(
    columns = {'Close':'GOOG'})
meta_data = data_frames['META'][['Date', 'Close']].rename(
    columns = {'Close':'META'})
msft_data = data_frames['MSFT'][['Date', 'Close']].rename(
    columns = {'Close':'MSFT'})

merged_data_AG = pd.merge(aapl_data, goog_data, on = 'Date', how='outer')
merged_data_AGM = pd.merge(pd.merged_data_AG, meta_data, on ='date', how ='outer')
df_final = pd.merge(
    merged_data_AGM, msft_data, on ='Date', how = "outer")
df_finale = df_final.reset_index(drop=True)
df_final.head() 
df_final.to_csv('data/stocks.csv', sep = ',', decimal ='.')
