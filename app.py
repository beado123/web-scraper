'''
Created on Mar 4, 2018

@author: yihan
'''

import json
from flask import Flask, request, jsonify, abort
from parser import Parser
from graph import Graph


app = Flask(__name__)
parser = Parser()
g = Graph()
my_file = open('/home/yihan//eclipse_cs242/web_scraper/web_scraper/test_data1.json')
data = json.load(my_file)
data_actor = data[0]
data_movie = data[1]
        
@app.route('/actors', methods=['GET'])
def get_actor_attr(): 
    '''
    This function gets actor with specified attributes
    '''
    ret = data_actor
    name = request.args.get('name')
    age = request.args.get('age')
    total_gross = request.args.get('total_gross')
    first_time = True
    if name != None:
        if first_time:
            ret = [actor for actor in ret.items() if actor[1]['name'] == name]
            first_time = False
        else:
            ret = [actor for actor in ret if actor[1]['name'] == name]
    if age != None:
        if first_time:
            ret = [actor for actor in ret.items() if str(actor[1]['age']) == age]
            first_time = False
        else:
            ret = [actor for actor in ret if str(actor[1]['age']) == age]
    if total_gross != None:
        if first_time:
            ret = [actor for actor in ret.items() if str(actor[1]['total_gross']) == total_gross]
            first_time = False
        else:
            ret = [actor for actor in ret if str(actor[1]['total_gross']) == total_gross]
                
    return jsonify(dict(ret)),200

    
@app.route('/actors/<actor_name>', methods=['GET'])
def get_actor(actor_name):
    '''
    This function gets actor with specified name
    :param actor_name:
    '''
    ret = [actor for actor in data_actor.items() if actor[1]['name'] == actor_name]
    return jsonify(dict(ret)),200


@app.route('/movies', methods=['GET'])
def get_movie_attr(): 
    '''
    This function gets movie with specified attributes
    '''
    ret = data_movie
    name = request.args.get('name')
    grossing = request.args.get('box_office')
    year = request.args.get('year')
    first_time = True
    if name != None:
        if first_time:
            ret = [movie for movie in ret.items() if movie[1]['name'] == name]
            first_time = False
        else:
            ret = [movie for movie in ret if movie[1]['name'] == name]
    if grossing != None:
        if first_time:
            ret = [movie for movie in ret.items() if str(movie[1]['box_office']) == grossing]
            first_time = False
        else:
            ret = [movie for movie in ret if str(movie[1]['grossing']) == grossing]
    if year != None:
        if first_time:
            ret = [movie for movie in ret.items() if str(movie[1]['year']) == year] 
            first_time = False
        else:
            ret = [movie for movie in ret if str(movie[1]['year']) == year] 
        
    return jsonify(dict(ret)),200


@app.route('/movies/<movie_name>', methods=['GET'])
def get_movie(movie_name):
    '''
    This function gets movie with specified name
    :param movie_name:
    '''
    ret = [movie for movie in data_movie.items() if movie[1]['name'] == movie_name]
    return jsonify(dict(ret)),200


@app.route('/actors/<actor_name>', methods=['PUT'])
def put_actor(actor_name):
    '''
    This function updates an actor with attributes changed
    :param actor_name: passed in url
    '''
    actor = [actor for actor in data_actor.items() if actor[1]['name'] == actor_name][0]
    my_dict = request.get_json()
    for key in my_dict:
        if key == 'name':
            actor[1]['name'] = my_dict['name']
        if key == 'json_class':
            actor[1]['json_class'] = my_dict['json_class']
        if key == 'age':
            actor[1]['age'] = my_dict['age']
        if key == 'total_gross':
            actor[1]['total_gross'] = my_dict['total_gross']
        if key == 'movies':
            actor[1]['movies'] = my_dict['movies']
            
    with open("test_data_write.json", "w+") as json_file:
        json_string = json.dumps(data, default=parser.dumper, indent=4, sort_keys=True, separators=(',', ':'))
        json_file.write(json_string)
    json_file.close()
    
    return jsonify(dict([actor])),201


@app.route('/movies/<movie_name>', methods=['PUT'])
def put_movie(movie_name):
    '''
    This function updates a movie with attributes changed
    :param movie_name: passed in url
    '''
    movie = [movie for movie in data_movie.items() if movie[1]['name'] == movie_name][0]
    my_dict = request.get_json()
    for key in my_dict:
        if key == 'name':
            movie[1]['name'] = my_dict['name']
        if key == 'json_class':
            movie[1]['json_class'] = my_dict['json_class']
        if key == 'box_office':
            movie[1]['box_office'] = my_dict['box_office']
        if key == 'year':
            movie[1]['year'] = my_dict['year']
        if key == 'actors':
            movie[1]['actors'] = my_dict['actors']
        if key == 'wiki_page':
            movie[1]['wiki_page'] = my_dict['wiki_page']
            
    with open("test_data_write.json", "w+") as my_file:
        json_string = json.dumps(data, default=parser.dumper, indent=4, sort_keys=True, separators=(',', ':'))
        my_file.write(json_string)
    my_file.close()
    
    return jsonify(dict([movie])),201


@app.route('/actors', methods=['POST'])
def post_actor():
    '''
    This function posts a new actor
    '''
    my_dict = request.get_json()
    data_actor[my_dict.keys()[0]] = my_dict.values()[0]
    with open("test_data_write.json", "w+") as my_file:
        json_string = json.dumps(data, default=parser.dumper, indent=4, sort_keys=True, separators=(',', ':'))
        my_file.write(json_string)
    my_file.close()
    
    return jsonify(my_dict),201


@app.route('/movies', methods=['POST'])
def post_movie():
    '''
    This function posts a new movie
    '''
    my_dict = request.get_json()
    data_movie[my_dict.keys()[0]] = my_dict.values()[0]
    with open("test_data_write.json", "w+") as my_file:
        json_string = json.dumps(data, default=parser.dumper, indent=4, sort_keys=True, separators=(',', ':'))
        my_file.write(json_string)
    my_file.close()
    
    return jsonify(my_dict),201


@app.route('/actors/<actor_name>', methods=['DELETE'])
def delete_actor(actor_name):
    '''
    This function deletes an actor with specified name
    :param actor_name:
    '''
    
    if actor_name not in data_actor.keys(): return abort(404)
    deleted = data_actor[actor_name]
    ret = [item for item in data_actor.items() if item[1]['name'] != actor_name]
    data[0] = dict(ret)
    with open("test_data_write.json", "w+") as my_file:
        json_string = json.dumps(data, default=parser.dumper, indent=4, sort_keys=True, separators=(',', ':'))
        my_file.write(json_string)
    my_file.close()
    
    return jsonify(dict(deleted)),200


@app.route('/movies/<movie_name>', methods=['DELETE'])
def delete_movie(movie_name):
    '''
    This function deletes a movie with specified name
    :param movie_name:
    '''
    if movie_name not in data_movie.keys(): return abort(404)
    deleted = data_movie[movie_name]
    ret = [item for item in data_movie.items() if item[1]['name'] != movie_name]
    data[1] = dict(ret)
    with open("test_data_write.json", "w+") as my_file:
        json_string = json.dumps(data, default=parser.dumper, indent=4, sort_keys=True, separators=(',', ':'))
        my_file.write(json_string)
    my_file.close()
    
    return jsonify(dict(deleted)),200

if __name__ == '__main__':
    app.run(debug=True)