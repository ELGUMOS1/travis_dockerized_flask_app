from app import app
import unittest

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass
    
    def test_fill_database(self):
        result = self.app.post('/')
        self.assertEqual(result.status_code, 200)
        
    def test_eight_queen_puzzle(self):
      
        result = self.app.get('/get/4')
        #print result.data
        
        self.assertIn('[[1, 3, 0, 2], [2, 0, 3, 1]]',result.data)

   