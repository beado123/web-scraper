'''
Created on Feb 23, 2018

@author: yihan
'''

class Actor:
    '''
    This class builds an actor object
    '''


    def __init__(self, name, birth, movies, total_grossing):
        '''
        Constructor
        '''
        self.name = name
        self.birth = birth
        self.film = movies
        self.total_grossing = total_grossing
    
    def get_name(self):
        '''
        get name of the actor
        '''
        return self.name
    
    def get_birth(self):
        '''
        get birth of the actor
        '''
        return self.birth
    
    def get_movies(self):
        '''
        get movies
        '''
        return self.film
    
    def get_total_grossing(self):
        '''
        return total grossing
        '''
        return self.total_grossing
    
    def set_total_grossing(self, grossing):
        '''
        set total grossing of actor
        :param grossing:
        '''
        self.total_grossing = grossing