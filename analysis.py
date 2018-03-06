'''
Created on Mar 3, 2018

@author: yihan
'''
import json
from graph import Graph
import matplotlib.pyplot as plt
import operator


def create_list(g, data_actor, data_movie):
    '''
    This function creates actor and movie lists from given json file
    '''
    actors = []
    movies = []
    for key,vertex in data_actor.items():
        if vertex['json_class'] == 'Actor':
            g.add_vertex(vertex['name'], vertex['json_class'], vertex['age'], vertex['movies'], vertex['total_gross'], 'not for actor', [])
            actors.append(vertex['name'])
        
    for key,vertex in data_movie.items():
        if vertex['json_class'] == 'Movie':
            g.add_vertex(vertex['name'], vertex['json_class'], 'not for movie', [], vertex['box_office'], vertex['year'], vertex['actors'])
            movies.append(vertex['name'])
    return actors,movies

def compute_connection(g, actors):
    '''
    This function computes hub actor
    '''
    con_dict = {}
    for curr_actor_name in actors:
        curr_actor = g.vert_dict[curr_actor_name]
        connection = 0
        for movie in curr_actor.get_movies():
            for other_actor_name in actors:
                other_actor = g.vert_dict[other_actor_name]
                if other_actor_name != curr_actor_name :
                    if movie in other_actor.get_movies():
                        connection += 1
        con_dict[curr_actor_name] = connection
        
    return con_dict

def compute_grossing(g, actors):
    '''
    This function computes grossing value of each age group
    '''
    gross_dict = {}
    for actor in actors:
        age = g.vert_dict[actor].get_birth()
        if age in gross_dict:
            gross_dict[age] += g.vert_dict[actor].get_grossing()
        else:
            gross_dict[age] = g.vert_dict[actor].get_grossing()
            
    return gross_dict

def plot_graph(xvalues,yvalues,label1,title,ylabel,xlabel):
    '''
    This function helps plot the graph
    :param xvalues: 
    :param yvalues:
    :param label1:
    :param title:
    :param ylabel:
    :param xlabel:
    '''
    plt.plot(xvalues, yvalues,label=label1)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    g = Graph()
    my_file = open('test_data.json')
    data = json.load(my_file)
    data_actor = data[0]
    data_movie = data[1]
    actors,movies = create_list(g,data_actor,data_movie)
    
    con_dict = compute_connection(g,actors)
    hub_actor = max(con_dict.iteritems(), key=operator.itemgetter(1))[0]
    x_value = list(range(len(actors)))
    
    gross_dict = compute_grossing(g,actors)
    max_grossing_group = max(gross_dict.iteritems(), key=operator.itemgetter(1))[0]  
    
    print "summary:"
    print "Total of " + str(g.get_num_vertices())+" number of nodes in graph, " + str(len(actors))+ ' actors, '+ str(len(movies)) + ' movies.'
    print "The hub actor is " + hub_actor+ ", with total " + str(con_dict[hub_actor]) + " connections with other actors"
    plot_graph(x_value,con_dict.values(),'connections','Connections of Actors','connections','number of actors')
    print 'Total of ' + str(len(gross_dict)) + ' age groups'
    print 'Age group ' + str(max_grossing_group) + ' generates the most amount of money'  
    plot_graph(gross_dict.keys(),gross_dict.values(),'grossing value of each age group','Connection between age group and grossing value',
               'grossing value','age group of actors')  
