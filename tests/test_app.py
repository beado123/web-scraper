'''
Created on Mar 4, 2018

@author: yihan
'''
import unittest
import json
from web_scraper.app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        '''
        This function sets up the client for app.py
        '''
        self.app = app.test_client()
        #self.app.testing = True 

    def test_get_actor(self):
        '''
        This function tests getting an actor
        '''
        response = self.app.get('/actors/Denzel Washington')
        self.assertEquals(response.status_code,200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEquals(json_response['Denzel Washington']['age'], 62)
        
    
    def test_get_movie(self):
        '''
        This function tests getting a movie
        '''
        response = self.app.get('/movies/16 Blocks')
        self.assertEquals(response.status_code,200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEquals(json_response['16 Blocks']['box_office'], 65)
        
    def test_put_actor(self):
        '''
        This function tests updating actor
        '''
        response = self.app.put('/actors/Denzel Washington', data=json.dumps({'age': 100}),content_type='application/json')
        self.assertEquals(response.status_code,201)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEquals(json_response['Denzel Washington']['age'], 100)
    
        
    def test_post_actor(self):
        '''
        This function tests poting new actor
        '''
        new_actor = { "yihan":{'name': 'yihan',
                     'age': 30,
                     'movies': ['a','b'],
                     'json_class': 'actor',
                     'total_gross': 0,
                     }}
        response = self.app.post('/actors', data=json.dumps(new_actor),content_type='application/json')
        self.assertEquals(response.status_code,201)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEquals(json_response['yihan']['age'], 30)
        
    def test_post_movie(self):
        '''
        This function tests posting new movie
        '''
        new_actor = {'name': 'paprika',
                     'birth': 'not for movie',
                     'movies': 'not for movie',
                     'type': 'movie',
                     'grossing': '100000',
                     'release_date': '2018',
                     'cast': ['a1','b2']}
        response = self.app.post('/movies', data=json.dumps(new_actor),content_type='application/json')
        self.assertEquals(response.status_code,201)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEquals(json_response['name'], "paprika")
        
    def test_delete_actor(self):
        '''
        This function tests deleting an actor
        '''
        response = self.app.delete('/actors/Greta Scacchi')
        self.assertEquals(response.status_code,200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEquals(str(json_response['name']), 'Greta Scacchi')
        
    def test_delete_movie(self):
        '''
        This function tests deleting a movie
        '''
        response = self.app.delete('/movies/The Two Jakes')
        self.assertEquals(response.status_code,200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEquals(json_response['name'], "The Two Jakes")
        
        
if __name__ == "__main__":
    unittest.main()