from tests.test_base import BaseTestCase
from app.utils import calculate_environmental_impact

class TestUtils(BaseTestCase):
    def test_calculate_environmental_impact(self):
        recycled_items = [
            {'item': 'plastic', 'quantity': 10},
            {'item': 'paper', 'quantity': 20},
            {'item': 'glass', 'quantity': 5}
        ]
        impact = calculate_environmental_impact(recycled_items)
        self.assertIsInstance(impact, float)
        self.assertGreater(impact, 0)
