

import os
import unittest

from app import app, db

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################
    
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False        
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def test_database(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        
    def test_eight_queen_puzzle_4(self):  
        result = self.app.get('/get/4')         
        self.assertIn(b'[[1, 3, 0, 2], [2, 0, 3, 1]]',result.data)
        
  
    def test_eight_queen_puzzle_8(self):  
        result = self.app.get('/get/8')     
        self.assertIn(b'[5, 2, 0, 7, 3, 1, 6, 4], [5, 2, 0, 7, 4, 1, 3, 6]', result.data)
        

  
if __name__ == "__main__":
    unittest.main()
