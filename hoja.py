# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:53:40 2020

@author: Bobde
"""
import yahoo_fin.stock_info as si
import requests
import pandas as pd
import requests
import pandas as pd
from pprint import pprint
import json
import sys
from flask_jsonpify import jsonify
import yfinance as yf
from pprint import pprint
import operator
import itertools
demo='60757d8382080062b8f1f1b626ddec5e'
companies =requests.get(f'https://fmpcloud.io/api/v3/stock-screener?exchange=NASDAQ&limit=3859&apikey={demo}')
companies =companies.json()
def filterfunc(symbol):
    p=requests.get("https://fmpcloud.io/api/v3/ratios/"+symbol+"?period=quarter&apikey=60757d8382080062b8f1f1b626ddec5e")
    p=p.json()
    count=0    
    for x in p:
        # y = json.loads(x)
        if x["currentRatio"]!=None and x["currentRatio"]> 1.5 :
            count=count+1
        if x["debtEquityRatio"]!=None and x["debtEquityRatio"]< 1.1:
            count=count+1
        if x["priceEarningsRatio"]!=None and x["priceEarningsRatio"]< 9:
            count=count+1
        if x["priceToBookRatio"]!=None and x["priceToBookRatio"]< 1.2 :
            count=count+1
        if x["dividendYield"]!=None and x["dividendYield"]> 1.0:
            count=count+1
            
        return count
        
        
sym={}
batch_id=0
batch_size=1
small_dict={}
mid_dict={}
large_dict={}

while batch_id<len(companies):
    sym=companies[batch_id:batch_id+batch_size]
    if sym[0]['marketCap']<20000000:
        small_dict[sym[0]['symbol']]=sym[0]['marketCap']
    elif sym[0]['marketCap']<100000000 and sym[0]['marketCap']>20000000:
        mid_dict[sym[0]['symbol']]=sym[0]['marketCap']
    else:
        large_dict[sym[0]['symbol']]=sym[0]['marketCap']
    batch_id=batch_id+batch_size
small_dict=dict(itertools.islice(small_dict.items(), 5))
mid_dict=dict(itertools.islice(mid_dict.items(), 5))
large_dict=dict(itertools.islice(large_dict.items(), 5))

comp={}
m=input("Enter cap")
if m=="smallcap":
    for key,value in  small_dict.items():
        comp[key]=filterfunc(key)
    comp=dict(sorted(comp.items(), key=operator.itemgetter(1),reverse=True))
elif m=="midcap":
    for key in  mid_dict.items():
        comp[key]=filterfunc(key) 
    comp=dict(sorted(comp.items(), key=operator.itemgetter(1),reverse=True))

elif m=="largecap":
    for key in  large_dict.items():
        comp[key]=filterfunc(key) 
    comp=dict(sorted(comp.items(), key=operator.itemgetter(1),reverse=True))

print("filtered")
print(comp)
# Com=[]
# for key,value in comp.items():
#     quote = si.get_quote_table(key)
        
        
#     c=Company(key,quote.get('1y Target Est'),quote.get('52 Week Range'),quote.get('Ask'),quote.get('Avg. Volume'),quote.get('Beta (5Y Monthly)'),quote.get('Bid'),quote.get("Day's Range"),quote.get('EPS (TTM)'),quote.get('Earnings Date'),quote.get('Ex-Dividend Date'),quote.get('Forward Dividend & Yield'),quote.get('Market Cap'),quote.get('Open'),quote.get('PE Ratio (TTM)'),quote.get('Previous Close'),quote.get('Price'),quote.get('Volume')) 
#     Com.append(c.toJSON())
#     print(c.toJSON())   
    
# return jsonify(Com)

  
class Company:
    def __init__(self,symbol,oneyTarget,Week52Range,Ask,AvgVolume,Beta5YMonthly,Bid,DayRange,EPS,EarningsDate,ExDividendDate,ForwardDividendYield,MarketCap,Open,PERatio,PreviousClose,QuotePrice,Volume):
        self.symbol=symbol,
        self.oneyTarget=oneyTarget,
        self.Week52Range=Week52Range,
        self.Ask=Ask,
        self.AvgVolume=AvgVolume,
        self.Beta5YMonthly=Beta5YMonthly ,
        self.Bid=Bid,
        self.DayRange=DayRange,
        self.EPS=EPS,
        self.EarningsDate=EarningsDate,
        self.ExDividendDate=ExDividendDate,
        self.ForwardDividendYield=ForwardDividendYield,
        self.MarketCap=MarketCap,
        self.Open=Open,
        self.PERatio=PERatio,
        self.PreviousClose=PreviousClose,
        self.QuotePrice=QuotePrice,
        self.Volume=Volume
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=False, indent=4)
 


  