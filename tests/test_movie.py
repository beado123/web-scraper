'''
Created on Feb 23, 2018

@author: yihan
'''
import unittest
from web_scraper.movie import Movie

cast = ['Mary', 'Ted']
movie = Movie('fly', 100,'1998',cast)

class Test(unittest.TestCase):

    def test_grossing_value(self):
        self.assertEqual(movie.get_title(), 'fly')
        self.assertEqual(movie.get_grossing(), 100)
        self.assertEqual(movie.get_release_date(), '1998')
        self.assertEqual(movie.get_cast()[0], 'Mary')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()