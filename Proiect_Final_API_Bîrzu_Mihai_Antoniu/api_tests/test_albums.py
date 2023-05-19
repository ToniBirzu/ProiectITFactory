import unittest

from api_requests.albums import get_album_without_market, get_album_with_market, get_album_with_country_and_limit, get_album_tracks, save_albums, get_several_albums




class TestAlbums(unittest.TestCase):
    def test_get_album(self):
        response = get_album_without_market('6PFPjumGRpZnBzqnDci6qJ')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Hybrid Theory")
# in acest test verific un album cu id ul: 6PFPjumGRpZnBzqnDci6qJ
# verific daca status code este 200 (OK) si daca acel album se numeste Hybrid Theory

    def test_get_album_not_exist(self):
        response = get_album_without_market('4aawyAB9vmqN3uQ7FjRGTg')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"]["message"], "Non existing id: 'spotify:album:4aawyAB9vmqN3uQ7FjRGTg'")

# in acest test verific un album care nu exsita cu un  id gresit
# verific daca status code este 404 (Not Found) si daca mesajul de eroare corespunde

    def test_get_album_check_copyright(self):
        response = get_album_without_market('6PFPjumGRpZnBzqnDci6qJ')
        assert "2000 Warner Records Inc" in response.json()['copyrights'][0]['text']

# in acest test verific un album cu id ul: 6PFPjumGRpZnBzqnDci6qJ
# verific daca copyrights corespunde acelui album


    def test_get_album_check_artist_name(self):
        response = get_album_without_market('3YIUNL7qFE8NP3X3zaYSND')
        assert "Maluma" in response.json()['artists'][0]['name']

# in acest test verific un album cu id ul: 3YIUNL7qFE8NP3X3zaYSND
# verific daca artistul acelui album este corect


    def test_get_album_filter_by_market_invalid_market(self):
        response = get_album_with_market('3YIUNL7qFE8NP3X3zaYSND', "XY")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"]["message"], "Invalid market code")

# in acest test verific un album cu id ul: 3YIUNL7qFE8NP3X3zaYSND si cu criteriul tara,
# dar tara am scris-o gresit pentru a verifica daca status code este 400 (Bad Request)
# si daca mesajul de eroare este corect

    def test_get_album_tracks(self):
        response = get_album_tracks('0vE6mttRTBXRe9rKghyr1l')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], 20)

# in acest test verific melodiile de pe albumul cu id ul: 0vE6mttRTBXRe9rKghyr1l
# verific daca status code este 200 (OK) si daca acel album are un total de 20 melodii

    def test_get_several_albums(self):
        response = get_several_albums('3Bj8Yd9ANO4KufZkqOmG0W,4Gfnly5CzMJQqkUFfoHaP3,4Amv0hrD1UuVHSnexg1iqP')
        self.assertEqual(response.status_code, 200)

# in acest test verific o suita de albume cu id urile: 3Bj8Yd9ANO4KufZkqOmG0W,4Gfnly5CzMJQqkUFfoHaP3,4Amv0hrD1UuVHSnexg1iqP
# verific daca status code este 200 (OK)

    def test_get_new_releseases(self):
        response = get_album_with_country_and_limit('RO', 10)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["albums"]["total"], 100)

# in acest test verific 10 dintre cele mai noi melodii din Romania si
# verific daca status code este 200 (OK) si daca in acel album se gasesc 100 melodii

    def test_save_albums(self):
        response = save_albums('3Bj8Yd9ANO4KufZkqOmG0W,4Gfnly5CzMJQqkUFfoHaP3,4Amv0hrD1UuVHSnexg1iqP')
        self.assertEqual(response.status_code, 200)
# in acest test salvez albumele cu id urile: 3Bj8Yd9ANO4KufZkqOmG0W,4Gfnly5CzMJQqkUFfoHaP3,4Amv0hrD1UuVHSnexg1iqP
# verific daca status code este 200 (OK)




