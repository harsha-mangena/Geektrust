class TopUp:
    def __init__(self, topup_type, no_of_months) -> None:
        self._topup_type = topup_type
        self._no_of_months = int(no_of_months)
    
    def get_topup_type(self) -> int:
        return self._topup_type
    
    def get_no_of_months(self) -> int:
        return self._no_of_months
        