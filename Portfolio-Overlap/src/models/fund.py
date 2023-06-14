from src.models.stock import Stock


class Fund:
    def __init__(self, name:str) -> None:
        self._name = name
        self._list_of_stocks = list(Stock)
    
    def get_fund_name(self) -> str:
        return self._name
    
    def get_stocks(self):
        return self._list_of_stocks
    
    def add_stock(self, stock:Stock) -> None:
        self._list_of_stocks.append(stock)
        
    def get_no_of_stocks(self) -> int:
        return len(self._list_of_stocks)


        