import datetime
from dateutil.relativedelta import relativedelta
from global_constants import DURATION_MAP, EARLY_REMINDER_DAY, SUBSCRIPTION_FEES
from src.models.subscription import Subscription

class SubscriptionService:
    def __init__(self, category:str, 
                       subscription_type:str,
                       start_date:datetime) -> None:
        
        duration = DURATION_MAP.get(subscription_type)
        self._subscription = Subscription(category, start_date, subscription_type, duration)
    
    def get_renewal_date(self) -> datetime:
        
        start_date = self._subscription.get_start_date()
        if start_date is None:
            return 

        renewal_date = start_date + relativedelta(months=self._subscription.get_duration())
        return renewal_date
    
    def get_remainder_date(self) -> datetime:
        return self.get_renewal_date() - datetime.timedelta(days=EARLY_REMINDER_DAY)
    
    def calculate_renewal_amount(self) -> int:
        category = self._subscription.get_category()
        plan_type = self._subscription.get_subscription_type()
        
        return SUBSCRIPTION_FEES.get(category).get(plan_type)
        