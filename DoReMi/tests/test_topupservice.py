import unittest
from global_constants import TOPUP_DEVICE_RATES
from src.models.topup import TopUp
from src.services.topupservice import TopupService

class TopupServiceTestCase(unittest.TestCase):
    def test_calculate_topup_price(self):
        topup_type = "Type A"
        months = 3
        topup_service = TopupService(topup_type, months)
        expected_rate = TOPUP_DEVICE_RATES.get(topup_type, 0)
        expected_price = expected_rate * months
        calculated_price = topup_service.calculate_topup_price()
        self.assertEqual(calculated_price, expected_price)

    def test_calculate_topup_price_no_rate(self):
        topup_type = "Non-existent Type"
        months = 5
        topup_service = TopupService(topup_type, months)
        expected_price = 0  # No rate exists for the given topup_type
        calculated_price = topup_service.calculate_topup_price()
        self.assertEqual(calculated_price, expected_price)

if __name__ == '__main__':
    unittest.main()
