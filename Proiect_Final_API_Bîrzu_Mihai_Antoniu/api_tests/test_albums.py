import unittest

from api_requests.albums import get_album_without_market, get_album_with_market, get_album_with_country_and_limit, get_album_tracks, save_albums, get_several_albums




class TestAlbums(unittest.TestCase):
    def test_get_album(self):
        response = get_album_without_market('6PFPjumGRpZnBzqnDci6qJ')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Hybrid Theory")


    def test_get_album_not_exist(self):
        response = get_album_without_market('4aawyAB9vmqN3uQ7FjRGTg')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"]["message"], "Non existing id: 'spotify:album:4aawyAB9vmqN3uQ7FjRGTg'")



    def test_get_album_check_copyright(self):
        response = get_album_without_market('6PFPjumGRpZnBzqnDci6qJ')
        assert "2000 Warner Records Inc" in response.json()['copyrights'][0]['text']



    def test_get_album_check_artist_name(self):
        response = get_album_without_market('3YIUNL7qFE8NP3X3zaYSND')
        assert "Maluma" in response.json()['artists'][0]['name']



    def test_get_album_filter_by_market_invalid_market(self):
        response = get_album_with_market('3YIUNL7qFE8NP3X3zaYSND', "XY")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"]["message"], "Invalid market code")


    def test_get_album_tracks(self):
        response = get_album_tracks('0vE6mttRTBXRe9rKghyr1l')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], 20)


    def test_get_several_albums(self):
        response = get_several_albums('3Bj8Yd9ANO4KufZkqOmG0W,4Gfnly5CzMJQqkUFfoHaP3,4Amv0hrD1UuVHSnexg1iqP')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(response.json()["albums"]["artists"]["name"], "Mala Mía") #??????????

    def test_get_new_releseases(self):
        response = get_album_with_country_and_limit('RO', 10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["albums"]["total"], 100)


    def test_save_albums(self):
        response = save_albums('3Bj8Yd9ANO4KufZkqOmG0W,4Gfnly5CzMJQqkUFfoHaP3,4Amv0hrD1UuVHSnexg1iqP')
        self.assertEqual(response.status_code, 200)





