'''
Created on Mar 3, 2018

@author: yihan
'''
import unittest
from web_scraper.graph import Graph

class Test(unittest.TestCase):
    '''
    This class contains test cases in http://www.bogotobogo.com/python/python_graph_data_structures.php
    as well as some I wrote
    '''

    def test_add_neighbor(self):
        g = Graph()
        a1 = g.add_vertex('a1', 'actor', '1989', ['m1','m2'], 'not for actor', 'not for actor', 'not for actor')
        g.add_movies(g, 'a1', ['m1','m2'])
        self.assertEquals(a1.get_weight('m1'),0)
        m1 = g.vert_dict['m1'].update_vertex('m1','movie','not for movie','not for movie','1001','1991', ['a1','a2','a3'])
        g.add_actors(g,'m1',['a1','a2','a3'])
        self.assertEquals(a1.get_weight('m1'),3)
        self.assertEquals(m1.get_weight('a2'),2)
        a2 = g.add_vertex('a2', 'actor', '1999', ['m1','m2'], 'not for actor', 'not for actor', 'not for actor')
        g.add_movies(g, 'a2', ['m1','m2'])
        self.assertEquals(a2.get_weight('m1'),2)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()