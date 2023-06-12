import datetime
from global_constants import ERROR_CODES
from src.services.subscriptionservice import SubscriptionService
from src.services.topupservice import TopupService

class DoremiService:
    def __init__(self):
        self._subscriptions = {}
        self._top_up = None
        
    def add_subscription(self, category: str, subscription_type: str, start_date: datetime) -> None:
        if category in self._subscriptions:
            print(ERROR_CODES['ERR_ADD_SUBS_DUPLICATE_CATEGORY'])
            return
        
        subscription = SubscriptionService(category, subscription_type, start_date)
        self._subscriptions[category] = subscription
        
    def add_top_up(self, topup_type: str, months: int) -> None:
        if not self._subscriptions:
            print(ERROR_CODES['ERR_TOPUP_FOR_NO_SUBS'])
            return 
        
        if self._top_up is not None:
            print(ERROR_CODES['ERR_DUPLICATE_TOPUP'])
            return 
        
        self._top_up = TopupService(topup_type, months)
    
    def calculate_total_payable_amount(self) -> float:
        total_amount = sum(subscription.calculate_renewal_amount() for subscription in self._subscriptions.values())
        
        if self._top_up:
            total_amount += self._top_up.calculate_topup_price()
        
        return total_amount
    
    def print_subscriptions_details(self) -> None:
        if not self._subscriptions:
            print(ERROR_CODES['ERR_NO_SUBS'])
            return
        
        for category, subscription in self._subscriptions.items():
            renewal_date = subscription.get_remainder_date()
            if renewal_date:
                print(f"RENEWAL_REMINDER {category} {renewal_date.strftime('%d-%m-%Y')}")
        
        renewal_amount = self.calculate_total_payable_amount()
        print(f"RENEWAL_AMOUNT {renewal_amount}")

    def get_subscriptions(self) -> dict:
        return self._subscriptions
    
    def get_topup(self) -> TopupService:
        return self._top_up