import unittest
from todo import app
import requests


class TestAPI(unittest.TestCase):
    """Tests with DB."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_get_todo(self):
        """Test retrieving todo item from db"""

        result = requests.get("http://localhost:5000/todo/1")
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(), {'description': 'Wash the lincoln', 'id': 1, 'name': 'Wash the car'})


if __name__ == '__main__':
    unittest.main()
