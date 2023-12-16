from db import CreateRecord
from marketapi import EndodDayAPI
from model import session, StockEODPrice



if __name__ == '__main__':
    print("Started the Process")
    tickers_list = ['AAPL', 'C', 'UAL', 'MMM']
    data_List = []
    for ticker in tickers_list:
        eod_data = EndodDayAPI().get(ticker)
        data_List.append(eod_data)
    """
    data_List1 = [{
                    'open': 197.53, 
                    'high': 198.3999, 
                    'low': 197.02, 
                    'close': 197.57, 
                    'volume': 114815314.0, 
                    'adj_high': 198.3999, 
                    'adj_low': 197.0, 
                    'adj_close': 197.57, 
                    'adj_open': 197.53, 
                    'adj_volume': 128538401.0, 
                    'split_factor': 1.0, 
                    'dividend': 0.0, 
                    'symbol': 'AAPL', 
                    'exchange': 'XNAS', 
                    'date': '2023-12-15T00:00:00+0000'
                   }, 
                   {
                    'open': 49.69, 
                    'high': 50.1, 
                    'low': 49.2, 
                    'close': 49.83, 
                    'volume': 35151100.0, 
                    'adj_high': 50.1, 
                    'adj_low': 49.2, 
                    'adj_close': 49.83, 
                    'adj_open': 49.69, 
                    'adj_volume': 35156095.0, 
                    'split_factor': 1.0, 
                    'dividend': 0.0, 
                    'symbol': 'C', 
                    'exchange': 'XNYS', 
                    'date': '2023-12-15T00:00:00+0000'
                    },
                    {
                    'open': 43.51, 
                    'high': 43.87, 
                    'low': 43.22, 
                    'close': 43.58, 
                    'volume': 8675900.0, 
                    'adj_high': 43.87, 
                    'adj_low': 43.22, 
                    'adj_close': 43.58, 
                    'adj_open': 43.51, 
                    'adj_volume': 8679614.0, 
                    'split_factor': 1.0, 
                    'dividend': 0.0, 
                    'symbol': 'UAL', 
                    'exchange': 'XNAS', 
                    'date': '2023-12-15T00:00:00+0000'}]
    """
    for i in data_List:
        CreateRecord.stock_eod_price(i['symbol'], i['date'], i['open'], i['close'])


