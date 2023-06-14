from models.fund import Fund
from models.portfolio import Portfolio


class PortfolioService:
    def __init__(self, ) -> None:
        self._portfolio = Portfolio()
        
    def add_new_fund(self, fund: Fund) -> None:
        self._portfolio.add_new_fund(fund)
    
    def get_all_funds(self) -> None:
        return self._portfolio.get_mutual_funds()

    def find_fund_by_name(self, fund_name:str):
        for fund in self._portfolio.get_mutual_funds():
            if fund.get_fund_name() == fund_name:
                return fund
        return None
    
    