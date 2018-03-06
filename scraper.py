'''

Created on Feb 22, 2018

@author: yihan
'''
from bs4 import BeautifulSoup
from parser import Parser
from graph import Graph
import urllib2
import json
import logging
import time
            
parser = Parser()
graph = Graph()
data = {}
data['vertices'] = []
movie_num = 0
actor_num = 0
actor_max = 250
movie_max = 125
logging.basicConfig(filename='parser.log',filemode='w+', level=logging.DEBUG)
wiki = "https://en.wikipedia.org/wiki/Morgan_Freeman"
parser.get_q().put(wiki)
scraped_url = []

while True:
    print(actor_num)
    print(movie_num)
    if movie_num >= movie_max and actor_num>= actor_max:
        break
    wiki = parser.get_q().get()
    if wiki in scraped_url:
        continue
    print(wiki)
    page = urllib2.urlopen(wiki)
    soup = BeautifulSoup(page, 'html.parser')
    film = soup.find('span', id='Filmography')
    # it's an actor
    if film != None:
        film = parser.find_movies(soup)
        if film is None:
            logging.warning('page '+wiki+'was not able to be parsed because no films under Filmography.')
            continue
        if parser.get_movie_found() is True:
            parser.append_href(film)
            if actor_num > actor_max:
                print 'actor_num satisfied, continue skipping'
                continue
            
            movie_names = parser.extract_movie_name(film)
            actor = parser.find_title(soup,wiki)
            start = time.time()
            if actor in graph.vert_dict:
                new_vertex = graph.vert_dict[actor].update_vertex(parser.find_title(soup,wiki), "actor", parser.find_birth(soup,wiki), movie_names, 0, "not for actor", "not for actor")
            else:
                new_vertex = graph.add_vertex(parser.find_title(soup,wiki), "actor", parser.find_birth(soup,wiki), movie_names, 0, "not for actor", "not for actor")
           
            graph.add_actors(graph,actor, movie_names)
            data['vertices'].append(new_vertex)
            actor_num += 1            
            parser.set_movie_found(False)
    else:
        # it's a movie
        cast_title = soup.find('span', id='Cast')
        if cast_title is None:
            logging.warning('page '+wiki+'was not able to be parsed because Cast tag was not found.')
            continue
        actor_list = parser.find_actors(soup)
        if actor_list is None:
            logging.warning('page '+wiki+'was not able to be parsed because there is no cast under Cast tag.')
            continue
        if parser.get_cast_found() is True:
            parser.append_href(actor_list)
            if movie_num > movie_max:
                print 'movie_num satisfied, continue skipping'
                continue
            actor_names = parser.extract_actor_name(actor_list)
            movie = parser.find_title(soup,wiki)
            
            if movie in graph.vert_dict:
                new_vertex = graph.vert_dict[movie].update_vertex(parser.find_title(soup,wiki), "movie", "not for movie", "not for movie", parser.find_grossing(soup,wiki), parser.find_release_date(soup,wiki), actor_names)
            else:
                new_vertex = graph.add_vertex(parser.find_title(soup,wiki), "movie", "not for movie", "not for movie", parser.find_grossing(soup,wiki), parser.find_release_date(soup,wiki), actor_names)
           
            graph.add_movies(graph,movie,actor_names)
            #print parser.find_title(soup,wiki)
            data['vertices'].append(new_vertex)
            movie_num += 1            
            parser.set_cast_found(False)
    logging.info('scraped '+wiki)
    scraped_url.append(wiki)

with open('data_copy2.json', 'w+') as my_file:
    json_string = json.dumps(data, default=parser.dumper, indent=4, sort_keys=True, separators=(',', ':'))
    my_file.write(json_string)
my_file.close()