import datetime
import unittest
from src.services.subscriptionservice import SubscriptionService

class SubscriptionServiceTestCase(unittest.TestCase):
    def test_get_renewal_date(self):
        category = "MUSIC"
        start_date = datetime.datetime(2022, 2, 20)
        subscription_type = "PERSONAL"
        subscription_service = SubscriptionService(category, subscription_type, start_date)
        renewal_date = subscription_service.get_renewal_date()
        self.assertEqual(renewal_date, datetime.datetime(2022, 3, 20, 0, 0))

    def test_get_remainder_date(self):
        category = "MUSIC"
        start_date = datetime.datetime(2022, 2, 20)
        subscription_type = "PERSONAL"
        subscription_service = SubscriptionService(category, subscription_type, start_date)
        remainder_date = subscription_service.get_remainder_date()
        self.assertEqual(remainder_date, datetime.datetime(2022, 3, 10, 0, 0))

    def test_get_renewal_amount(self):
        category = "MUSIC"
        start_date = datetime.datetime(2022, 2, 20)
        subscription_type = "PERSONAL"
        subscription_service = SubscriptionService(category, subscription_type, start_date)
        renewal_amount = subscription_service.calculate_renewal_amount()
        self.assertEqual(renewal_amount, 100)

if __name__ == '__main__':
    unittest.main()
