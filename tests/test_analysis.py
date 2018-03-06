'''
Created on Mar 6, 2018

@author: yihan
'''
import unittest
from web_scraper.graph import Graph
from web_scraper.analysis import compute_connection,compute_grossing
import operator


class Test(unittest.TestCase):

    def test_connection(self):
        '''
        This function tests computing actor with most connections
        '''
        g = Graph()
        actors = ['a1','a2','a3','a5']
        g.add_vertex('a1', 'actor', 23, ['m1','m2'], '', '', [])
        g.add_vertex('a2', 'actor', 24, ['m2','m3'], '', '', [])
        g.add_vertex('a3', 'actor', 24, ['m2','m4'], '', '', [])
        g.add_vertex('a5', 'actor', 24, [], '', '', [])
        g.add_vertex('m1', 'movie', '', [], 100, 2009, ['a1','a2'])
        g.add_vertex('m2', 'movie', '', [], 200, 2011, ['a3','a5'])
        g.add_vertex('m3', 'movie', '', [], 0, 0, [])
        g.add_vertex('m4', 'movie', '', [], 0, 0, [])
        con_dict = compute_connection(g,actors)
        self.assertEquals(max(con_dict.iteritems(), key=operator.itemgetter(1))[0],'a1')
        
    def test_grossing(self):
        '''
        This function tests age group with largest gross value
        '''
        g = Graph()
        actors = ['a1','a2','a3','a5']
        g.add_vertex('a1', 'actor', 23, ['m1','m2'], 22, '', [])
        g.add_vertex('a2', 'actor', 24, ['m2','m3'], 22, '', [])
        g.add_vertex('a3', 'actor', 24, ['m2','m4'], 66, '', [])
        g.add_vertex('a5', 'actor', 25, [], 33, '', [])
        gross_dict = compute_grossing(g, actors)
        self.assertEquals(max(gross_dict.iteritems(), key=operator.itemgetter(1))[0], 24)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_connection']
    unittest.main()