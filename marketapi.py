import requests
from config import MS_ACCESS_KEY


class EndodDayAPI:
    def get(self,stock_ticker):
        
        params = {
            'access_key': MS_ACCESS_KEY
        }
        url = f"http://api.marketstack.com/v1/tickers/{stock_ticker}/eod/latest"
        results = requests.get(url, params=params)

        return results.json()

class RealTimeAPI:
    def get(self):
        pass