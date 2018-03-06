'''
Created on Feb 23, 2018

@author: yihan
'''
import unittest
from web_scraper.parser import Parser
from bs4 import BeautifulSoup
import urllib2

parser = Parser()
class Test(unittest.TestCase):
        
    def test_find_movies(self):
        '''
        test for finding movies in html
        '''
        
        url = "https://en.wikipedia.org/wiki/Morgan_Freeman"  
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        self.assertEqual(parser.find_movies(soup)[4].get_text(), 'Glory')
        url = "https://en.wikipedia.org/wiki/Albert_Salmi"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        self.assertEqual(parser.find_movies(soup)[6].get_text(), 'The Outrage')
        url = "https://en.wikipedia.org/wiki/Joe_Pesci"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        self.assertEqual(parser.find_movies(soup)[11].get_text(), "The Legendary Life of Ernest Hemingway")
        url = "https://en.wikipedia.org/wiki/Patty_Duke"
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        self.assertEqual(parser.find_movies(soup)[2].get_text(), "4D Man")
    
    def test_find_birth(self):
        '''
        test for finding birth in html
        '''
        url = 'https://en.wikipedia.org/wiki/Morgan_Freeman'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        self.assertEqual(parser.find_birth(soup,url), '1937')
        
    def test_find_grossing(self):
        '''
        test for finding grossing of a movie
        '''
        url = 'https://en.wikipedia.org/wiki/Brubaker'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        self.assertEqual(parser.find_grossing(soup,url), '$37,121,708')
    
    def test_find_release_date(self):
        '''
        test for finding release date of a movie
        '''
        url = 'https://en.wikipedia.org/wiki/Brubaker'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        self.assertEqual(parser.find_release_date(soup,url), '1980')
    
    def test_find_actors(self):
        '''
        test for finding cast of a movie
        '''
        url = 'https://en.wikipedia.org/wiki/Brubaker'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        cast = parser.find_actors(soup)
        actors = parser.extract_actor_name(cast)
        self.assertEqual(actors[3], 'Murray Hamilton')
        
if __name__ == "__main__":
    unittest.main()       
        