'''
Created on Feb 26, 2018

@author: yihan
'''
import unittest
from web_scraper.actor import Actor
movies = ['a', b'']
actor = Actor('Andy', '1998', movies, 0)

class Test(unittest.TestCase):


    def test_attr(self):
        self.assertEqual(actor.get_name(), 'Andy')
        self.assertEqual(actor.get_birth(), '1998')
        self.assertEqual(len(actor.get_movies()), 2)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()