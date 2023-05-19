import  unittest

from api_requests.shows import get_show_episodes



class TestShows(unittest.TestCase):
    def test_get_show_episdoes(self):
        response = get_show_episodes('4rOoJ6Egrf8K2IrywzwOMk', 2)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.json()["languages"], "en-US") #??????????