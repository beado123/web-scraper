'''
Created on Mar 2, 2018

@author: yihan
'''
from vertex import Vertex

class Graph(object):
    '''
    class for graph
    The design follows from http://www.bogotobogo.com/python/python_graph_data_structures.php
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.vert_dict = {}
        self.num_vertices = 0
        
    
    def add_vertex(self, name, types, birth, movies, grossing, release_date, cast):
        '''
        This function adds a vertex to graph and increment number of vertices
        :param name:
        :param types:
        :param birth:
        :param movies:
        :param grossing:
        :param release_date:
        :param cast:
        '''
        self.num_vertices += 1
        new_vertex = Vertex(name, types, birth, movies, grossing, release_date, cast)
        self.vert_dict[name] = new_vertex 
        return new_vertex
            
    def add_actors(self, g, curr, lst):
        '''
        This function adds edges from curr to actors in list
        :param g: graph
        :param curr: movie
        :param lst: actor list
        '''
        rank = 0
        for actor in lst:
            g.add_edge(curr, actor, len(lst)-rank)
            rank += 1
            
    def add_movies(self, g, curr, lst):
        '''
        This function adds edges from curr to movies in list
        :param g: graph
        :param curr: actor
        :param lst: movie list
        '''
        for movie in lst:
            if movie in self.vert_dict:
                print movie, curr, self.vert_dict[movie].get_weight(curr)
                g.add_edge(curr, movie, self.vert_dict[movie].get_weight(curr))
            else:
                g.add_edge(curr, movie, 0)
                
    def add_edge(self, frm, to, weight ):  
        '''
        This function adds an edge from 'frm' to 'to' and add their edge weight
        :param frm:
        :param to:
        :param weight:
        '''
        if frm not in self.vert_dict:
            self.add_vertex(frm, '', '', [], '', '', [])      
        if to not in self.vert_dict:
            self.add_vertex(to, '', '', [], '', '', [])   
        #if to not in self.vert_dict[frm].adjacent:
        if self.vert_dict[frm].get_weight(to) == 0:
            self.vert_dict[frm].add_neighbor(to, weight)
        #if frm not in self.vert_dict[to].adjacent:
        if self.vert_dict[to].get_weight(frm) == 0:
            self.vert_dict[to].add_neighbor(frm, weight)
        
    def get_vertex(self, name):
        '''
        This function returns a vertex specified with name parameter
        :param name:
        '''
        if name in self.vert_dict:
            return self.vert_dict[name]
        else:
            return None
        
    def get_num_vertices(self):
        '''
        This function returns number of vertices in graph
        '''
        return self.num_vertices