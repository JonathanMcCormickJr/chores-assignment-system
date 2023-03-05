# test_main.py

import unittest
from main import app



class TestMain(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_hello(self):
        response = self.client.get('/analytics')
        self.assertEqual(response.status_code, 200), print("Status code is", response.status_code)


if __name__ == '__main__':
    unittest.main()

