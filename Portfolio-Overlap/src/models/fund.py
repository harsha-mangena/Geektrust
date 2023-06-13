from src.models.stock import Stock


class Fund:
    def __init__(self, name:str) -> None:
        self._name = name
        self._list_of_stocks = list()
    
    def get_fund_name(self) -> str:
        return self._name
    
    def add_stock(self, stock:Stock) -> None:
        self._list_of_stocks.append(stock)
    
    def number_of_stocks(self) -> int:
        return len(self._list_of_stocks)

        