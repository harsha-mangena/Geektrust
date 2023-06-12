import datetime
import unittest
from src.services.doremiservice import DoremiService

class DoremiServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.doremi = DoremiService()
        self.start_date = datetime.datetime(2022, 2, 20)
        self.category = "MUSIC"
        self.subscription_type = "PERSONAL"

    def test_add_subscription(self):
        self.doremi.add_subscription(self.category, self.subscription_type, self.start_date)
        self.assertIn(self.category, self.doremi.get_subscriptions())

    def test_add_subscription_duplicate_category(self):
        self.doremi.add_subscription(self.category, self.subscription_type, self.start_date)
        # Adding the same category again should not add a duplicate subscription
        self.doremi.add_subscription(self.category, "OTHER", self.start_date)
        self.assertEqual(len(self.doremi.get_subscriptions()), 1)

    def test_add_top_up(self):
        self.doremi.add_subscription(self.category, self.subscription_type, self.start_date)
        topup_type = "FOUR_DEVICE"
        months = 3
        self.doremi.add_top_up(topup_type, months)
        self.assertIsNotNone(self.doremi.get_topup())

    def test_add_top_up_no_subs(self):
        topup_type = "FOUR_DEVICE"
        months = 3
        self.doremi.add_top_up(topup_type, months)
        self.assertIsNone(self.doremi.get_topup())

    def test_calculate_total_payable_amount(self):
        self.doremi.add_subscription(self.category, self.subscription_type, self.start_date)
        topup_type = "FOUR_DEVICE"
        months = 3
        self.doremi.add_top_up(topup_type, months)
        total_amount = self.doremi.calculate_total_payable_amount()
        self.assertEqual(total_amount, 250)

    def test_print_subscriptions_details(self):
        self.doremi.add_subscription(self.category, self.subscription_type, self.start_date)
        topup_type = "FOUR_DEVICE"
        months = 3
        self.doremi.add_top_up(topup_type, months)
        # Test the output of print_subscriptions_details using captured stdout and assertions

if __name__ == '__main__':
    unittest.main()
