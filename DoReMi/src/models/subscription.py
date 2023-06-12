import datetime

from global_constants import DURATION_MAP

class Subscription:
    def __init__(self, category:str, 
                       start_date:datetime, 
                       subscription_type:str,
                       duration:int) -> None:
        """
        Initializes a new instance of the class with the given category and subscription type.

        :param category: The category of the subscription.
        :type category: str
        :param subscription_type: The type of the subscription.
        :type subscription_type: str
        :return: None
        """
        self._category = category
        self._subscription_type = subscription_type
        self._start_date = start_date
        self._duration = duration
    
    def get_start_date(self) -> datetime:
        return self._start_date if self._start_date is not None else None

    def get_category(self) -> str:
        return self._category
    
    def get_duration(self) -> int:
        return self._duration
    
    def get_subscription_type(self) -> str:
        return self._subscription_type
        