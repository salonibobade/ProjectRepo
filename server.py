from flask import Flask,render_template,request,redirect,url_for
import MySQLdb
from flask_cors import CORS,cross_origin
import flask
import sys
#sys.path.append('code')
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from json import dumps
from flask_jsonpify import jsonify
import pandas as pd
import sys
import json
import decimal
import itertools
import pandas_datareader.data as web
from datetime import datetime
from iexfinance.refdata import get_symbols
from pandas import DataFrame
from collections import OrderedDict
from iexfinance.stocks import Stock
from datetime import date, timedelta
import os
import requests
import iexfinance
app = Flask(__name__)
api = Api(app)
CORS(app)
conn = MySQLdb.connect(host="localhost",user="root",password="Sallu@1811",db="testdb")
token=os.environ.get('IEX_TOKEN')
@app.route("/loggedin",methods=["POST",'GET'])
def login():

    username = request.args.get('user')
    password=request.args.get('password')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username ='"+username+"'and password='"+password+"'")
    user = cursor.fetchone()

    if user is None:
        response = flask.jsonify({"status":"false"})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
        return response
    response = flask.jsonify({"status":"true"})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
   
    return response
    #return user

# class Company:
#     def __init__(self,    symbol , companyName , previousClose_change  ,change , changePercent ,latestTime ,primaryExchange ,sector, marketCap , open , high ,low,close,previousClose,latestVolume,week52High,week52Low):
#         self.symbol = symbol
#         self.companyName = companyName
#         self.previousClose_change = previousClose_change
#         self.change = change
#         self.changePercent = changePercent
#         self.latestTime = latestTime
#         self.primaryExchange = primaryExchange
#         self.sector = sector
#         self.marketCap = marketCap
#         self.open = open
#         self.high = high
#         self.low = low
#         self.close = close
#         self.previousClose = previousClose
#         self.latestVolume = latestVolume
#         self.week52High = week52High
#         self.week52Low = week52Low
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__,
#             sort_keys=False, indent=4)

# class Employees(Resource):
   
#     def get(self,marketcap):
#         try:
#             companies={}
#             print("Received request")
#             selected_companies={}
#             print(type(marketcap))
#             marketCap=marketcap
           
#             prices = pd.DataFrame(list(get_symbols(token=token)))#pd.DataFrame(list(get_symbols()))   #datareader to read all stock symbols available
       
           
#             stock_list = prices['name'].tolist()
#             stock_symbol_list = prices['symbol'].tolist()
#             companies=dict(zip( stock_symbol_list,stock_list,))   #companies will give you company name with stock symbol
#             stock_symbol_list=stock_symbol_list[:1000] #dont forget to add more companies
#             batch_idx = 0
#             batch_size = 99
#             sym=[]
#             fundamentals_dict_for_symbol = {}
#             while batch_idx < len(stock_symbol_list):
#                 print(batch_idx)
#                 sym=stock_symbol_list[batch_idx:batch_idx+99]
#                 print(sym)
#                 stock_batch = Stock(sym)
#                 quote_json = stock_batch.get_quote()
#                 for stock_symbol in sym:
#                     if(quote_json[stock_symbol]['marketCap']):
#                         fundamentals_dict_for_symbol[stock_symbol]=quote_json[stock_symbol]['marketCap']  #fundamentals_dict_for_symbol will gie you market cap and
#                 batch_idx=batch_idx+batch_size
#             print("done")
#             #now finding companies relevant to market cap
#             for symbol, price in fundamentals_dict_for_symbol.items():
#                 value=(decimal.Decimal(price)-decimal.Decimal(marketCap))
#                 selected_companies[symbol]=value
#             print("got some companies")
#             sorted_x = sorted(selected_companies.items(), key=lambda kv: kv[1])
#             sorted_dict = dict(sorted_x)
#             sorted_dict=dict(itertools.islice(sorted_dict.items(), 40))
#             stock_symbol_list=list(sorted_dict.keys())
#             stock_batch = Stock(stock_symbol_list, token=token)
#             fundamentals_dict = {}#this will store required criteria and values
#             # Pull all the data we'll need from IEX.
#             # financials_json = stock_batch.get_financials()

#             quote_json = stock_batch.get_quote(token=token)

#             stats_json = stock_batch.get_key_stats(token=token)

#             for symbol in stock_symbol_list:
       
#             # Make sure we have all the data we'll need for our filters for this stock.
#                 if not data_quality_good(symbol, financials_json, quote_json, stats_json):
#                     continue

#                 fundamentals_dict[symbol] = get_fundamental_data_for_symbol(symbol,financials_json,quote_json,stats_json)

#             dictt = filter_fundamental_df(pd.DataFrame.from_dict(fundamentals_dict).T)  
#             stock_symbol_list=list(dictt.keys())
#             print("just fetching stock")
#             start = date.today() - timedelta(days = 15)
#             end = date.today()

#             Com=[]
#             for stock_symbol in stock_symbol_list:
           
#                 additive = Stock(stock_symbol)
#                 newdata=additive.get_quote()
#                  c=Company(newdata.get('symbol'),newdata.get('companyName'),newdata.get('previousClose_change'),newdata.get('change'),newdata.get('changePercent'),newdata.get('latestTime'),newdata.get('primaryExchange'),newdata.get('sector'),newdata.get('marketCap'),newdata.get('open'),newdata.get('high'),newdata.get('low'),newdata.get('close'),newdata.get('previousClose'),newdata.get('latestVolume'),newdata.get('week52High'),newdata.get('week52Low'))
#                 Com.append(c.toJSON())
#                 print(c.toJSON())  
               
#             #jsonStr = json.dumps([e.toJSON() for e in Com])
#             #print(Com)      
#             return jsonify(Com)
#         except (iexfinance.utils.exceptions.IEXQueryError, TypeError, KeyError) as e:
#             print("ERROR",e)
#         #return  jsonStr
# def eps_good(earnings_reports):
#   # This method contains logic for filtering based on earnings reports.
#     if len(earnings_reports) < 4:
#         print("rejecting",earnings_reports)
#         # The company must be very new. We'll skip it until it's had time to
#         # prove itself.
#         return False

#     # earnings_reports should contain the information about the last four
#     # quarterly reports.
#     for report in earnings_reports:
#         # We want to see consistent positive EPS.
#         #try:
#         if not report['actualEPS']:
#             print("reject",report)
#             return False
#         if report['actualEPS'] < 0:
#             return False
#         #except KeyError:
#             print("ok")
#             # A KeyError here indicates that some data was missing or that a company is less than two years old.
#             # We don't mind skipping over new companies until they've had more
#             # time in the market.
#         #    return False
#     return True

# def data_quality_good(symbol, financials_json, quote_json, stats_json):
#     # This method makes sure that we're not going to be investing in
#     # securities we don't have accurate data for.

#     if len(financials_json[symbol] ) < 1 or quote_json[symbol]['latestPrice'] is None:
#         # No recent data was found. This can sometimes happen in case of recent
#         # markert suspensions.
#         return False

#     try:
#         if not (
#             quote_json[symbol]['marketCap'] and
#             stats_json[symbol]['priceToBook'] and
#             stats_json[symbol]['sharesOutstanding'] and
#             financials_json[symbol][0]['totalAssets'] and
#             financials_json[symbol][0]['currentAssets'] and
#             quote_json[symbol]['latestPrice']
#         ):
#             # Ignore companies IEX cannot report all necessary data for, or
#             # thinks are untradable.
#             return False
#     except KeyError:
#         # A KeyError here indicates that some data we need to evaluate this
#         # stock was missing.
#         return False

#     return True


# def get_fundamental_data_for_symbol(
#         symbol,
#         financials_json,
#         quote_json,
#         stats_json):
#     fundamentals_dict_for_symbol = {}

#     financials = financials_json[symbol][0]
#     # Calculate PB ratio.
#     fundamentals_dict_for_symbol['pb_ratio'] = stats_json[symbol]['priceToBook']

#     # Find the "Current Ratio" - current assets to current debt.
#     current_debt = financials['currentDebt'] if financials['currentDebt'] else 1
#     fundamentals_dict_for_symbol['current_ratio'] = financials['currentAssets'] / current_debt

#     # Find the ratio of long term debt to short-term liquiditable assets.
#     total_debt = financials['totalDebt'] if financials['totalDebt'] else 0
#     fundamentals_dict_for_symbol['debt_to_liq_ratio'] = total_debt / \
#         financials['currentAssets']

#     # Store other information for this stock so we can filter on the data
#     # later.
#     fundamentals_dict_for_symbol['pe_ratio'] = quote_json[symbol]['peRatio']
#     fundamentals_dict_for_symbol['market_cap'] = quote_json[symbol]['marketCap']
#     fundamentals_dict_for_symbol['dividend_yield'] = stats_json[symbol]['dividendYield']

#     return fundamentals_dict_for_symbol                    
# def filter_fundamental_df(fundamental_df):
#     count=0
#     comp={}
#     for index, row in fundamental_df.iterrows():
#         count=0
#         if(row["current_ratio"]> 1.5):
#             count=count+1
#         if(row["debt_to_liq_ratio"]< 1.1):
#             count=count+1
#         if(row["pe_ratio"]< 9):
#             count=count+1
#         if(row["pb_ratio"]< 1.2):
#             count=count+1
#         if(row["dividend_yield"]> 1.0):
#             count=count+1
#         comp[index]=count
#     print(comp)
#     sorted_x = sorted(comp.items(), key=lambda kv: kv[1])
#     sorted_dict = dict(sorted_x)
#     # This is where we remove stocks that don't meet our investment criteria.
#     return sorted_dict
   
# api.add_resource(Employees, '/stockmarket/<marketcap>') # Route_1      


if __name__ == '__main__':
    app.run(port=5000,debug=True)



