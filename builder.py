'''
Created on Feb 26, 2018

@author: yihan
'''
import json
from movie import Movie
from actor import Actor
from query import Query

def print_list(lst):
    '''
    This function prints item in list one by one
    :param lst:
    '''
    for item in lst:
        print item
    print '\n'
   
def print_name_age(lst):
    '''
    This function prints actor's name and birth
    :param lst:
    '''
    for item in lst:
        print item.name+' ' + item.birth
    print '\n'
    
def print_actors_grossing(lst):
    '''
    This function prints actor's name and total grossing value
    :param lst:
    '''
    for item in lst:
        print item.get_name() + ' ' + str(item.get_total_grossing())
    print '\n'
         
my_file = open('data.json')
data = json.load(my_file)
movie_lst = data['movies']
actor_lst = data['actors']
movies = []
actors = []
for item in movie_lst:
    mov = Movie(item['title'],item['grossing'], item['release_date'],item['cast'])
    movies.append(mov)
for item in actor_lst:
    act = Actor(item['name'],item['birth'],item['film'])
    actors.append(act)
query = Query(movies,actors)

while True:
    q_num = input("Please select a question.\n"
                  "1 Find how much a movie has grossed.\n"
                  "2 List which movies an actor has worked in. \n"
                  "3 List which actors worked in a movie \n"
                  "4 List the top X actors with the most total grossing value\n"
                  "5 List the oldest X actors. \n"
                  "6 List all the movies for a given year.\n"
                  "7 List all the actors for a given year.\n"
                  "8 for exit\n")
    q_num = int(q_num)
    if q_num == 1:
        mov_name = raw_input("Please enter a movie name.\n")
        print query.find_movie_grossing(mov_name) + '\n'
        
    if q_num == 2:
        act_name = raw_input("Please enter an actor's name.\n")
        print_list(query.find_actor_movies(act_name))
         
    if q_num == 3:
        mov_name = raw_input("Please enter a movie name.\n")
        print_list(query.find_movie_actors(mov_name))
        
    if q_num == 4:
        num = str(raw_input("Please enter a number.\n"))
        print_actors_grossing(query.find_actors_by_grossing(num))
        
    if q_num == 5:
        num = int(raw_input("Please enter a number.\n"))
        print_name_age(query.find_oldest_actors(num))
        
    if q_num == 6:
        year = raw_input("Please enter a year.\n")
        print_list(query.find_movies_by_year(year))
        
    if q_num == 7:
        year = raw_input("Please enter a year.\n")
        print_list(query.find_actors_by_year(year))
        
    if q_num == 8:
        exit(0)
        