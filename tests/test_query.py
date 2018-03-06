'''
Created on Feb 26, 2018

@author: yihan
'''
import unittest
from web_scraper.movie import Movie
from web_scraper.actor import Actor
from web_scraper.query import Query

cast = ['mary','ted']
movies1 = ['paprika','blackhole']
movies2 = ['inception','2012']
movie1 = Movie('paprika', 100, '1998', cast)
movie2 = Movie('inception', 200, '1988', cast)
actor1 = Actor('mary','2000',movies1,0)
actor2 = Actor('ted','2002',movies2,0)
m_lst = []
a_lst = []
m_lst.append(movie1)
m_lst.append(movie2)
a_lst.append(actor1)
a_lst.append(actor2)
query = Query(m_lst,a_lst)

class Test(unittest.TestCase):


    def test_find_movie_grossing(self):
        '''
        test for finding grossing of a film
        '''
        self.assertEqual(query.find_movie_grossing('paprika'), 100)
        
    def test_find_actor_movies(self):
        '''
        test for finding films of an actor
        '''
        self.assertEqual(query.find_actor_movies('mary'), movies1)
        
    def test_find_movie_actors(self):
        '''
        test for finding cast for a movie
        '''
        self.assertEqual(query.find_movie_actors('paprika'), cast)
        
    def test_actors_by_grossing(self):
        '''
        test for finding top x actors with most total grossing values
        '''
        self.assertEqual(query.find_actors_by_grossing(2)[0].get_name(), 'mary')
        self.assertEqual(query.find_actors_by_grossing(2)[1].get_name(), 'ted')
        
    def test_find_oldest_actors(self):
        '''
        test for finding oldest x actors
        '''
        self.assertEqual(query.find_oldest_actors(1)[0].get_name(), 'mary')
        
    def test_find_movies_by_year(self):
        '''
        test for listing all the movies for a given year
        '''
        self.assertEqual(query.find_movies_by_year('1988')[0], 'inception')
        
    def test_find_actors_by_year(self):
        '''
        test for listing all the actors for a given year
        '''
        self.assertEqual(query.find_actors_by_year('2000')[0], 'mary')


if __name__ == "__main__":
    unittest.main()