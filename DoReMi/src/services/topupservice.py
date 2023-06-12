from global_constants import TOPUP_DEVICE_RATES
from src.models.topup import TopUp

class TopupService:
    def __init__(self, topup_type: str, months: int) -> None:
        self.topup = TopUp(topup_type, months)
    
    def calculate_topup_price(self) -> float:
        if self.topup is None:
            return 0
        
        return TOPUP_DEVICE_RATES.get(self.topup.get_topup_type(), 0) * self.topup.get_no_of_months()
