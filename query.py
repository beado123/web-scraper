'''
Created on Feb 26, 2018

@author: yihan
'''

class Query:
    '''
    This class handles queries from user
    '''


    def __init__(self, movies, actors):
        '''
        Constructor
        '''
        self.movies = movies
        self.actors = actors
        
    def find_movie_grossing(self,name):
        '''
        This function finds how much a movie has grossed
        :param name: movie name
        '''
        for item in self.movies:
            if item.get_title() ==name:
                return item.get_grossing()
            
    def find_actor_movies(self, name):
        '''
        This function finds movies an actor has worked in
        :param name:
        '''
        for item in self.actors:
            if item.get_name() == name:
                return item.get_movies()
    
    def find_movie_actors(self, name):
        '''
        This function finds which actors worked in a movie
        :param name:
        '''
        for item in self.movies:
            if item.get_title() == name:
                return item.get_cast()
    
    def find_oldest_actors(self, num):
        '''
        List the oldest X actors
        :param num:
        '''
        lst = []
        self.actors.sort(key=lambda x: x.birth, reverse=False)
        for i in range(num):
            lst.append(self.actors[i])
        return lst
    
    def find_actors_by_grossing(self, num):
        '''
        List the top X actors with the most total grossing value
        :param num:
        '''
        actor_lst = []
        for actor in self.actors:
            grossing = 0
            actor_name = actor.get_name()
            movie_lst = actor.get_movies()
            for i in range(len(movie_lst)):
                mov_name = movie_lst[i]
                for movie in self.movies:
                    if movie.get_title() == mov_name:
                        cast = movie.get_cast()
                        for i in range(len(cast)):
                            if cast[i] == actor_name:
                                grossing += len(cast)-i
            actor.set_total_grossing(grossing)
        self.actors.sort(key=lambda x: x.total_grossing, reverse=True)
        for i in range(int(num)):
            actor_lst.append(self.actors[i])
        return actor_lst
                
                
    def find_movies_by_year(self, year):
        '''
         List all the movies for a given year
        :param year:
        '''
        lst = []
        for item in self.movies:
            if item.get_release_date() == year:
                lst.append(item.get_title())
        return lst
    
    def find_actors_by_year(self, year):
        '''
        List all the actors for a given year
        :param year:
        '''
        lst = []
        for item in self.actors:
            if item.get_birth() == year:
                lst.append(item.get_name())
        return lst
            
        