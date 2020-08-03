## -*- coding: utf-8 -*-
#"""
#Created on Wed Jul 29 12:25:44 2020
#
#@author: Bobde
#"""
#import nsepy
#from nsepy import get_history
#from nsepy import get_index_pe_history
#from datetime import date
#data = get_history(symbol="SBIN", start=date(2020,5,5), end=date(2020,6,30))
#print(data)
#data[['Close']].plot()
#
#nifty_pe = get_index_pe_history(symbol="NIFTY",
#                               start=date(2020,5,5), end=date(2020,6,30))
#print(nifty_pe)
#import pandas as pd
#import io
#import requests
#url = 'https://www1.nseindia.com/content/indices/ind_nifty50list.csv'
#s = requests.get(url).content
#
#df = pd.read_csv(io.StringIO(s.decode('utf-8')))
#print(df.Symbol)
#
#        
#        
#   
import yahoo_fin.stock_info as si
quote = si.get_quote_table('GOOG')
print(quote)