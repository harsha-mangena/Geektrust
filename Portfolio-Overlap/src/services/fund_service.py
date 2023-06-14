from models.fund import Fund


class FundService:
    def __init__(self) -> None:
        self._fund = Fund()
    
    
    def add_stock_to_fund(self, stock) -> None:
        self._fund.add_stock(stock)
    
    def get_stock_names(self):
        stock_names = list()
        for stock in self._fund.get_stocks():
            stock_names.append(stock.get_stock_name())
        
        return stock_names

    def find_stock_in_fund(self, stock_name):
        for stock in self._fund.get_stocks():
            if stock.get_stock_name() == stock_name:
                return stock
        return None
    
    def common_stocks_between_funds(self, other_fund:Fund):
        return len(set(self._fund.get_stocks()).intersection(other_fund.get_stocks()))
    
    def calculate_stock_overlap(self, other_fund:Fund):
        return self.common_stocks_between_funds(other_fund) // (self._fund.get_no_of_stocks() + other_fund.get_no_of_stocks()) * 100