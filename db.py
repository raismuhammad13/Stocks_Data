from model import StockEODPrice,session


# class CreateRecord:
#     print("We are in create Record class")
#     def stock_eod_price(self,**kwargs):
#         StockEODPrice.create(
#             stock_ticker=kwargs['stock_ticker'],
#             eod_date=kwargs['eod_date'],
#             open_price=kwargs['open_price'],
#             eod_price=kwargs['eod_price']
#         )
#     print("We are in end of Record class")


class CreateRecord:
    print("We are in create Record class")
    def stock_eod_price(stock_ticker, eod_date, open_price, close_price):
        session.add(
            StockEODPrice(
            stock_ticker=stock_ticker,
            eod_date=eod_date,
            open_price=open_price,
            close_price=close_price
        )
        )
        session.commit()
    print("We are in end of Record class")


class UpdateRecord:
    def stock_eod_price(self):
        pass


class DeleteRecord:
    def stock_eod_price(self):
        pass

class ReadRecords:
    def stock_eod_price(self):
        pass
