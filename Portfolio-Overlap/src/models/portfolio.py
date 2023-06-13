from src.models.fund import Fund


class Portfolio:
    def __init__(self) -> None:
        self._list_of_funds : list()
        
    def get_all_funds(self) -> None:
        return self._list_of_funds
    
    def add_new_fund(self, fund: Fund) -> None:
        self._list_of_funds.append(fund)
        