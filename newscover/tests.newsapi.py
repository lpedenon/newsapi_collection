import unittest
from newsapi import fetch_latest_news

class FetchLatestNewsTest(unittest.TestCase):

    def test_empty_inputs(self):

        self.assertRaises(TypeError, fetch_latest_news, None, None, None)

if __name__ == "__main__":
    unittest.main()