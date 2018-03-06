'''
Created on Feb 26, 2018

@author: yihan
'''
import logging
import Queue


class Parser:
    '''
    This classes has functions that help scrape the page
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.movie_found = False
        self.cast_found = False
        self.q = Queue.Queue(maxsize=20000)
        
    def set_movie_found(self,bo):
        '''
        set boolean variable movie_found
        :param bo:
        '''
        self.movie_found = bo
        
    def set_cast_found(self,bo):
        '''
        set boolean variable cast_found
        :param bo:
        '''
        self.cast_found = bo
        
    def get_movie_found(self):
        '''
        get boolean variable movie_found
        '''
        return self.movie_found
    
    def get_cast_found(self):
        '''
        get boolean variable actor_found
        '''
        return self.cast_found
    
    def get_q(self):
        '''
        get queue
        '''
        return self.q  
    
    def find_movies(self,soup):
        '''
        This function finds movie list
        :param soup:
        '''
        filmography = soup.find('span', id="Filmography")
        sib = filmography.parent.find_next_siblings(limit=3)   
        for i in range(3):
            #table form
            if sib[i].name == 'table':
                self.set_movie_found(True)
                return sib[i].findAll('i')
            #list form
            if sib[i].find('ul') != None:
                self.set_movie_found(True)
                return sib[i].findAll('i') 
            #movies are in another page
        
    def find_actors(self, soup):
        '''
        This function finds actor list
        :param soup:
        '''
        
        cast_title = soup.find('span', id='Cast')
        sibs = cast_title.parent.find_next_siblings(limit=3)
        for i in range(3):  
            if sibs[i].find('ul') != None or sibs[i].name == 'ul':
                self.set_cast_found(True)
                return sibs[i].findAll('li') 
            if sibs[i].name == 'table':
                self.set_cast_found(True)
                return sibs[i].findAll('a')
        
    def find_birth(self, soup, wiki):
        '''
        This function finds birth of actor
        :param soup:
        :param wiki:
        '''
        born = soup.find('th', string='Born')
        if born is None:
            logging.info('Cannot find birthday because incorrect format.'+wiki)
            return 'birth not found'
        birth_tag = born.find_next_sibling()
        if birth_tag is None:
            logging.info('Cannot find birthday because incorrect format.'+wiki)
            return 'birth not found'
        year_tag = birth_tag.find('span', style='display:none')
        if year_tag != None:
            year = year_tag.contents[1].string[:4]
        else:
            logging.info('Cannot find birthday because incorrect format.'+wiki)
            return 'birth not found'
        return year
    
    def find_grossing(self, soup, wiki):
        '''
        This function finds grossing of a movie
        :param soup:
        :param wiki:
        '''
        box_office = soup.find('th', string='Box office')
        if box_office is None:
            logging.debug('cannot find Box office in '+wiki)
            return "grossing not Found"
        sib = box_office.find_next_sibling()
        return sib.contents[0].string
    
    def find_release_date(self, soup, wiki):
        '''
        This function finds release date of movie
        :param soup:
        :param wiki:
        '''
        release_date = soup.find('div', string='Release date')
        if release_date is None:
            logging.debug('cannot find release date in '+wiki)
            return "date not found"
        sib = release_date.parent.find_next_sibling()
        li = sib.findAll('li')
        if len(li) == 0:
            date = sib.contents[0].string[-4:]
            if date != '':
                return date
            else: 
                logging.debug('cannot find release date in '+wiki)
                return "date not found"
        date = li[0].contents[0].string[-4:]
        return date
    
    def extract_movie_name(self, movies):
        '''
        This function converts list of movie object to list of movie title 
        :param movies:
        '''
        lst = []
        for i in range(len(movies)):
            lst.append(movies[i].string)
        return lst
    
    def find_title(self, soup, wiki):
        '''
        This function finds title of movie
        :param soup:
        :param wiki:
        '''
        h1 = soup.find('h1')
        li = h1.findAll('i')
        if len(li) !=0:  
            text = li[0].findAll(text=True, recursive=False)
            if len(text) != 0:
                return text[0]
        if h1.string is None:
            logging.debug('cannot find title in '+wiki)
        return h1.string
    
    def extract_actor_name(self, cast):
        '''
        This function converts list of actor object to list of actor names
        :param cast:
        '''
        lst = []
        for i in range(len(cast)):
            lst.append(cast[i].contents[0].string.split(' as')[0])
        return lst
    
    def append_href(self,lst):
        '''
        This function push new links to queue
        :param lst:
        '''
        for i in range(len(lst)):
            href_tag = lst[i].find('a', href=True)
            if href_tag is not None :
                exist = lst[i].find('a').get('title')
                if exist != None and exist[-6:] != 'exist)' :
                    self.q.put('https://en.wikipedia.org'+href_tag['href'])                
        return
    
    def dumper(self,obj):
        '''
        This function is from 
        https://stackoverflow.com/questions/36880065/how-to-serialize-python-dict-to-json
        :param obj:
        '''
        try:
            return obj.toJSON()
        except:
            return obj.__dict__