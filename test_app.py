import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Trimitem un request la pagina principala
        response = self.app.get('/')
        # Verificam ca primim codul 200 (OK)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()


