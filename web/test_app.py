

import os
import unittest

from app import app, db

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################
    sol_7 = '[[0, 2, 4, 6, 1, 3, 5], [0, 3, 6, 2, 5, 1, 4], [0, 4, 1, 5, 2, 6, 3],\
    [0, 5, 3, 1, 6, 4, 2], [1, 3, 0, 6, 4, 2, 5], [1, 3, 5, 0, 2, 4, 6], [1, 4, 0, 3, 6, 2, 5],\
    [1, 4, 2, 0, 6, 3, 5], [1, 4, 6, 3, 0, 2, 5], [1, 5, 2, 6, 3, 0, 4], [1, 6, 4, 2, 0, 5, 3],\
    [2, 0, 5, 1, 4, 6, 3], [2, 0, 5, 3, 1, 6, 4], [2, 4, 6, 1, 3, 5, 0], [2, 5, 1, 4, 0, 3, 6],\
    [2, 6, 1, 3, 5, 0, 4], [2, 6, 3, 0, 4, 1, 5], [3, 0, 2, 5, 1, 6, 4], [3, 0, 4, 1, 5, 2, 6],\
    [3, 1, 6, 4, 2, 0, 5], [3, 5, 0, 2, 4, 6, 1], [3, 6, 2, 5, 1, 4, 0], [3, 6, 4, 1, 5, 0, 2],\
    [4, 0, 3, 6, 2, 5, 1], [4, 0, 5, 3, 1, 6, 2], [4, 1, 5, 2, 6, 3, 0], [4, 2, 0, 5, 3, 1, 6],\
    [4, 6, 1, 3, 5, 0, 2], [4, 6, 1, 5, 2, 0, 3], [5, 0, 2, 4, 6, 1, 3], [5, 1, 4, 0, 3, 6, 2],\
    [5, 2, 0, 3, 6, 4, 1], [5, 2, 4, 6, 0, 3, 1], [5, 2, 6, 3, 0, 4, 1], [5, 3, 1, 6, 4, 2, 0],\
    [5, 3, 6, 0, 2, 4, 1], [6, 1, 3, 5, 0, 2, 4], [6, 2, 5, 1, 4, 0, 3], [6, 3, 0, 4, 1, 5, 2], [6, 4, 2, 0, 5, 3, 1]]'
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
        #self.assertEqual(result.status_code, 200)
        self.assertIn(b'[[1, 3, 0, 2], [2, 0, 3, 1]]',result.data)
        
    def test_eight_queen_puzzle_7(self):  
        result = self.app.get('/get/7')         
        #self.assertEqual(result.status_code, 200)
        self.assertIn(sol_7.encode(),result.data)
        
   ''' def test_eight_queen_puzzle_10(self):  
        result = self.app.get('/get/10') 
        l = list(result.data.decode())
        self.assertEqual(len(l), 724)'''
        

  
if __name__ == "__main__":
    unittest.main()
