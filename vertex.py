'''
Created on Mar 2, 2018

@author: yihan
'''

class Vertex(object):
    '''
    class for vertex
    The design follows from http://www.bogotobogo.com/python/python_graph_data_structures.php
    '''

    def __init__(self, name, my_type, birth, movies, grossing, release_date, cast ):
        '''
        Constructor
        '''
        self.name = name
        self.type = my_type
        self.birth = birth
        self.movies = movies
        self.grossing = grossing
        self.release_date = release_date
        self.cast = cast
        self.adjacent = {}
        
    def add_neighbor(self, neighbor, weight):
        '''
        This function adds an adjacent node to 'self' with passed in weight
        :param neighbor: adjacent node
        :param weight
        '''
        self.adjacent[neighbor] = weight
        
    def get_neighbors(self):
        '''
        This function returns the adjacent dictionary of all adjacent nodes
        '''
        return self.adjacent.keys()  
    
    def get_weight(self, neighbor):
        '''
        This function returns weight of the edge of 'self' and its neighbor
        :param neighbor
        '''
        if neighbor in self.adjacent.keys():
            return self.adjacent[neighbor]
        else:
            return 0
    def update_vertex(self, name, type1, birth, movies, grossing, release_date, cast):
        '''
        This function updates attributes of 'self'
        :param name:
        :param type:
        :param birth:
        :param movies:
        :param grossing:
        :param release_date:
        :param cast:
        '''
        self.name = name
        self.type = type1
        self.birth = birth
        self.movies = movies
        self.grossing = grossing
        self.release_date = release_date
        self.cast = cast
        return self
    
    def get_type(self):
        '''
        This function returns type of 'self'
        '''
        return self.type
    
    def get_name(self):
        '''
        This function returns name of 'self
        '''
        return self.name
    
    def get_birth(self):
        '''
        This function returns birth of 'self'
        '''
        return self.birth
    
    def get_movies(self):
        '''
        This function returns movie list of 'self'
        '''
        return self.movies
    
    def get_grossing(self):
        '''
        This function returns grossing value of 'self'
        '''
        return self.grossing
    
    def get_release_date(self):
        '''
        This function returns release_date of 'self'
        '''
        return self.release_date
    
    def get_cast(self):
        '''
        This function returns cast list of 'self'
        '''
        return self.cast
    
    def get_adjacent(self):
        '''
        This function returns adjacent dictionary
        '''
        return self.adjacent
    