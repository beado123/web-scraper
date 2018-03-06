'''
Created on Feb 23, 2018

@author: yihan
'''

class Movie:
    '''
    This class builds a movie object
    '''


    def __init__(self, title, grossing, release_date, cast):
        '''
        Constructor
        '''
        self.title = title
        self.grossing = grossing
        self.release_date = release_date
        self.cast = cast
        
    def get_title(self):
        '''
        get title of the film
        '''
        
        return self.title
        
    def get_grossing(self):
        '''
        get grossing of the film
        '''
        return self.grossing
    
    def get_release_date(self):
        '''
        get year released of the film
        '''
        return self.release_date
    
    def get_cast(self):
        '''
        return cast of the movie
        '''
        return self.cast