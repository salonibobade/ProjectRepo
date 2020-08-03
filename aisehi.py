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

app = Flask(__name__)
api = Api(app)
CORS(app)
conn = MySQLdb.connect(host="localhost", user="root", password="Sallu@1811", db="testdb")
# demo = '60757d8382080062b8f1f1b626ddec5e'
demo = '72b0ad34e1969c2a84b305c436195097'

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
    p = requests.get(
        "https://fmpcloud.io/api/v3/ratios/" + symbol + "?period=quarter&apikey=72b0ad34e1969c2a84b305c436195097")
    p = p.json()
    count = 0
    for x in p:
        # y = json.loads(x)
        if x["currentRatio"] != None and x["currentRatio"] > 1.5:
            count = count + 1
        if x["debtEquityRatio"] != None and x["debtEquityRatio"] < 1.1:
            count = count + 1
        if x["priceEarningsRatio"] != None and x["priceEarningsRatio"] < 9:
            count = count + 1
        if x["priceToBookRatio"] != None and x["priceToBookRatio"] < 1.2:
            count = count + 1
        if x["dividendYield"] != None and x["dividendYield"] > 1.0:
            count = count + 1

        return count

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
    small_dict = dict(itertools.islice(small_dict.items(), 5))
    mid_dict = dict(itertools.islice(mid_dict.items(), 5))
    large_dict = dict(itertools.islice(large_dict.items(), 5))
    #m = (input)("Enter cap : ")
    m = request.args.get('cap')
    comp = {}
    if m == "smallcap":
        for key, value in small_dict.items():
            comp[key] = filterfunc(key)
        comp = dict(sorted(comp.items(), key=operator.itemgetter(1), reverse=True))
    elif m == "midcap":
        for key in mid_dict.items():
            comp[key] = filterfunc(key)
        comp = dict(sorted(comp.items(), key=operator.itemgetter(1), reverse=True))

    elif m == "largecap":
        for key in large_dict.items():
            comp[key] = filterfunc(key)
        comp = dict(sorted(comp.items(), key=operator.itemgetter(1), reverse=True))

    print("filtered")
    print(comp)
    Com = []
    for key, value in comp.items():
        quote = si.get_quote_table(key)

        c = Company(key, quote.get('1y Target Est'), quote.get('52 Week Range'), quote.get('Ask'),
                    quote.get('Avg. Volume'), quote.get('Beta (5Y Monthly)'), quote.get('Bid'),
                    quote.get("Day's Range"), quote.get('EPS (TTM)'), quote.get('Earnings Date'),
                    quote.get('Ex-Dividend Date'), quote.get('Forward Dividend & Yield'), quote.get('Market Cap'),
                    quote.get('Open'), quote.get('PE Ratio (TTM)'), quote.get('Previous Close'), quote.get('Price'),
                    quote.get('Volume'))
        Com.append(c.toJSON())
        print(c.toJSON())

    return jsonify(Com)


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