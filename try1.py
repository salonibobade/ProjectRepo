from iexfinance.stocks import Stock
import os
token = os.environ.get('IEX_TOKEN')
a = Stock("AAPL", token=token)
a.get_quote()