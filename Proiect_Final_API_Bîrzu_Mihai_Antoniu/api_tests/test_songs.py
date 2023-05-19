import  unittest

from api_requests.songs import get_track, save_tracks, remove_saved_tracks



class TestSongs(unittest.TestCase):
    def test_get_one_track(self):
        response = get_track('4bYLTrlcqctyHck3fjhMgW')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "One Step Closer")


    def test_save_tracks(self):
        response = save_tracks('0RcYEWXtbu4ehdv1tiBOi0,6x5LBP3nYXVdIDoomChGr3,2DQ1ITjI0YoLFzuADN1ZBW')
        self.assertEqual(response.status_code, 200)


    def test_delete_saved_tracks(self):
        response = remove_saved_tracks('7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')
        self.assertEqual(response.status_code, 200)