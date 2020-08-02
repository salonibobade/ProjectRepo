from flask import Flask, render_template, request, redirect, url_for
import MySQLdb
from flask_cors import CORS, cross_origin
import flask
import sys
# sys.path.append('code')
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from json import dumps
from flask_jsonpify import jsonify
import json
import os
import requests
import yahoo_fin.stock_info as si
import requests
import pandas as pd
import requests
from pprint import pprint
import json
import sys
import yfinance as yf
from pprint import pprint
import operator
import itertools
import numpy
app = Flask(__name__)
api = Api(app)
CORS(app)
conn = MySQLdb.connect(host="localhost", user="root", password="Sallu@1811", db="testdb")
# demo = '60757d8382080062b8f1f1b626ddec5e'
demo = 'da1bff6d9e6788fd6e40d5fabf24343a'

companies = requests.get(f'https://fmpcloud.io/api/v3/stock-screener?exchange=NASDAQ&limit=3859&apikey={demo}')
companies = companies.json()


@app.route("/loggedin", methods=["POST", 'GET'])
def login():
    username = request.args.get('user')
    password = request.args.get('password')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username ='" + username + "'and password='" + password + "'")
    user = cursor.fetchone()

    if user is None:
        response = flask.jsonify({"status": "false"})
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
        return response
    response = flask.jsonify({"status": "true"})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')

    return response
    # return user


def filterfunc(symbol):
    p = requests.get(f"https://fmpcloud.io/api/v3/ratios/" + symbol + "?period=quarter&apikey=da1bff6d9e6788fd6e40d5fabf24343a")
    p = p.json()

    if len(p)!=0:
        count = 0
        # y = json.loads(x)
        if p[0]["currentRatio"] != None and p[0]["currentRatio"] > 1.5:
            count = count + 1
        if p[0]["debtEquityRatio"] != None and p[0]["debtEquityRatio"] < 1.1:
            count = count + 1
        if p[0]["priceEarningsRatio"] != None and p[0]["priceEarningsRatio"] < 9:
            count = count + 1
        if p[0]["priceToBookRatio"] != None and p[0]["priceToBookRatio"] < 1.2:
            count = count + 1
        if p[0]["dividendYield"] != None and p[0]["dividendYield"] > 1.0:
            count = count + 1

        return count
    else:
        return 0

@app.route("/stockMarket", methods=["POST", 'GET'])
def get():
    sym = {}
    batch_id = 0
    batch_size = 1
    small_dict = {}
    mid_dict = {}
    large_dict = {}

    while batch_id < len(companies):
        sym = companies[batch_id:batch_id + batch_size]
        if sym[0]['marketCap'] < 20000000:
            small_dict[sym[0]['symbol']] = sym[0]['marketCap']
        elif sym[0]['marketCap'] < 100000000 and sym[0]['marketCap'] > 20000000:
            mid_dict[sym[0]['symbol']] = sym[0]['marketCap']
        else:
            large_dict[sym[0]['symbol']] = sym[0]['marketCap']
        batch_id = batch_id + batch_size
    small_dict = dict(itertools.islice(small_dict.items(), 10))
    mid_dict = dict(itertools.islice(mid_dict.items(), 10))
    large_dict = dict(itertools.islice(large_dict.items(), 10))
    #m = (input)("Enter cap : ")
    m = request.args.get('cap')
    comp = {}
    if m == "smallcap":
        for key, value in small_dict.items():
            comp[key] = filterfunc(key)
        comp = dict(sorted(comp.items(), key=operator.itemgetter(1), reverse=True))
    elif m == "midcap":
        for key,value in mid_dict.items():
            comp[key] = filterfunc(key)
        comp = dict(sorted(comp.items(), key=operator.itemgetter(1), reverse=True))

    elif m == "largecap":
        for key,value in large_dict.items():
            comp[key] = filterfunc(key)
        comp = dict(sorted(comp.items(), key=operator.itemgetter(1), reverse=True))

    print("filtered")
    print(comp)
    comp = dict(itertools.islice(comp.items(), 5))
    Com = []
    
    for key, value in comp.items():
        symbol = str
        oneyTarget = str
        Week52Range = str
        Ask = str
        AvgVolume = str
        Beta5YMonthly = str
        Bid = str
        DayRange = str
        EPS = str
        EarningsDate = str
        ExDividendDate = str
        ForwardDividendYield = str
        MarketCap = str
        Open = str
        PERatio = str
        PreviousClose = str
        QuotePrice = str
        Volume = str
        quote = si.get_quote_table(key)
        c={}
        c['symbol']=key
        if str(quote['1y Target Est'])=='nan':
            c['oneytarget']=""
        else:
            c['oneytarget']=quote['1y Target Est']
        if str(quote['52 Week Range'])=='nan':
            c['Week52Range']=""
        else:
            c['Week52Range']=quote['52 Week Range']
        if  str(quote['Ask'])=='nan':
            c[' Ask']=""
        else:
            c[' Ask']= quote['Ask']
        if str(quote['Avg. Volume'])=='nan':
            quote['Avg. Volume']=""
        else:
            c['AvgVolume']=quote['Avg. Volume']
        if str(quote['Beta (5Y Monthly)'])=='nan':
            quote['Beta (5Y Monthly)']=""
        else:
            c['Beta5YMonthly']=quote['Beta (5Y Monthly)']
        if str(quote['Bid'])=='nan':
            quote['Bid']=""
        else:
            c['Bid']=quote['Bid']
        if str(quote["Day's Range"])=='nan':
            c['DayRange']=""
        else:
            c['DayRange']=quote["Day's Range"]
        if str(quote['EPS (TTM)'])=='nan':
            c['EPS']=""
        else:
            c['EPS']=quote['EPS (TTM)']
        if str(quote['Earnings Date'])=='nan':
            c['EarningsDate']=""
            print(c['EarningsDate'])
        else:
            c['EarningsDate']=quote['Earnings Date']
            print(c['EarningsDate'])
        if str(quote['Ex-Dividend Date'])=='nan':
            c['ExDividendDate']=""
        else:
            c['ExDividendDate']=quote['Ex-Dividend Date']
        if str(quote['Forward Dividend & Yield'])=='nan':
            c['ForwardDividendYield']=""
        else:
            c['ForwardDividendYield']=quote['Forward Dividend & Yield']
        if str(quote['Market Cap'])=='nan':
            c['MarketCap']=""
        else:
            c['MarketCap']=quote['Market Cap']
        if str(quote['Open'])=='nan':
            c['Open']=""
        else:    
            c['Open']=quote['Open']
        if str(quote['PE Ratio (TTM)'])=='nan':
            c['PERatio']=""
        else:
            c['PERatio']=quote['PE Ratio (TTM)']
        if str(quote['Previous Close'])=='nan':
            c['PreviousClose']=""   
        else:
            c['PreviousClose']=quote['Previous Close']
        if str(quote['Quote Price'])=='nan':
            c['QuotePrice']=""
        else:
            c['QuotePrice']=quote['Quote Price']
        if str(quote['Volume'])=='nan':
            c['Volume']=""
        else:
            c['Volume']=quote['Volume']
        # c = Company(key, quote.get('1y Target Est'), quote.get('52 Week Range'), quote.get('Ask'),
        #             quote.get('Avg. Volume'), quote.get('Beta (5Y Monthly)'), quote.get('Bid'),
        #             quote.get("Day's Range"), quote.get('EPS (TTM)'), quote.get('Earnings Date'),
        #             quote.get('Ex-Dividend Date'), quote.get('Forward Dividend & Yield'), quote.get('Market Cap'),
        #             quote.get('Open'), quote.get('PE Ratio (TTM)'), quote.get('Previous Close'), quote.get('Price'),
        #             quote.get('Volume'))
        # Com.append(c.toJSON())
        Com.append(json.dumps(c))
        # print(c.toJSON())
    print(Com)
    # response = flask.jsonify({"status": "true"})
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response = flask.jsonify(Com)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    # return jsonify(json.dumps(Com))
    return response


class Company:
    def __init__(self, symbol, oneyTarget, Week52Range, Ask, AvgVolume, Beta5YMonthly, Bid, DayRange, EPS, EarningsDate,
                 ExDividendDate, ForwardDividendYield, MarketCap, Open, PERatio, PreviousClose, QuotePrice, Volume):
        self.symbol = symbol,
        self.oneyTarget = oneyTarget,
        self.Week52Range = Week52Range,
        self.Ask = Ask,
        self.AvgVolume = AvgVolume,
        self.Beta5YMonthly = Beta5YMonthly,
        self.Bid = Bid,
        self.DayRange = DayRange,
        self.EPS = EPS,
        self.EarningsDate = EarningsDate,
        self.ExDividendDate = ExDividendDate,
        self.ForwardDividendYield = ForwardDividendYield,
        self.MarketCap = MarketCap,
        self.Open = Open,
        self.PERatio = PERatio,
        self.PreviousClose = PreviousClose,
        self.QuotePrice = QuotePrice,
        self.Volume = Volume

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


if __name__ == '__main__':
    app.run(port=5000, debug=True)