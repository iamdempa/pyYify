import os
import json
import urllib3
import time;
from bs4 import BeautifulSoup
from requests import get
import re 


class yify():

    class torrent():
        def __init__(self , name='' , page = ''):
            self.name = name ;
            self.page = page ; #Link to the torrent page

        def __str__(self):
            return "Name : {}   |   Page : {}".format(self.name , self.page) ;
        def __repr__(self):
            return "Name : {}   |   Page : {}".format(self.name , self.page) ;
            

        def getinfo(self , quality='All' , minimum_rating = 0 , 
        query_term = '' , genre='' , sort_by='date_added' ,
        order_by = 'desc' , with_rt_ratings='false'):
            '''
            Gets all the info about the torrent and returns a dictionary containing all the info
            
            '''
            self.name = re.search("^[^\(]+" ,self.name).group(0).strip() ; 
            print(self.name) ; 
            url = "https://yts.ag/api/v2/list_movies.json" ;

            url = url+ '?' +  urllib3.request.urlencode({
                'quality' : quality , 
                'minimum_rating' : minimum_rating , 
                'query_term' : self.name, 
                'genre' : genre , 
                'sort_by' : sort_by , 
                'order_by' : order_by , 
                'with_rt_ratings' : with_rt_ratings
            })            

            resp = get(url , timeout = 3) ;
            data = json.loads(resp.text) ; 
            movie = data["movies"][0] ;

            self.id = movie.get('id')
            self.url = movie.get('url')
            self.imdb_code = movie.get('imdb_code')
            self.title = movie.get('title')
            self.title_long = movie.get('title_long')
            self.slug  = movie.get('slug')
            self.year = movie.get('year')
            self.rating = movie.get('rating')
            self.runtime = movie.get('runtime')
            self.genres = movie.get('genres') 
            self.summary = movie.get('summary')
            self.description = movie.get('description') 
            self.language = movie.get('language')
            self.mpa_rating = movie.get('mpa_rating')
            self.image_links = [movie.get('background_image'),
            movie.get('background_image_original'), 
            movie.get('small_cover_image'),
            movie.get('medium_cover_image'),
            movie.get('large_cover_image')]
            


            print(url) ;

            # resp = get(url) ;
            # print(resp.text) ;   



    # class topseed():
    #     def __init__(self):
    #         pass ; 

    #     def get_top_seeded_torrents(self):
    #         '''Returns the top seeded torrent objects'''
    #         raise NotImplementedError ;

        


    # def __init__(self):
    #     resp = '';
    #     while(not resp):
    #         try:
    #             resp = get('https://www.yify-torrent.org/', timeout=3);

    #         except Exception as e:
    #             print(e);
    #             print(
    #                 "\nServer refused connection . \nSleeping for 5 seconds .....\nZZZzzzzzzzzz\n\n");
    #             time.sleep(5);
    #     self.soup = BeautifulSoup(resp.text, 'html.parser');



    def get_top_seeded_torrents(self):
        '''Returns a list of Top Seeded Torrents which are listed in the Yify Website when the function is called '''
        soup = BeautifulSoup(get('https://www.yify-torrent.org/', timeout=3).text , 'html.parser') ;
        topseeds = soup.find(id="topseed").find_all('a');


        # topseeds_names =  [];
        # topseeds_links = [] ; 
        top_torrents = [] 

        for i in topseeds:
            movie = self.torrent(name=i.text , page = i.get('href')) ; 
            # movie.getinfo()
            top_torrents.append(movie) ; 
        #     # topseeds_names.append(i.text);
        #     # topseeds_links.append(i.get('href')) ;


        # # for i in range(len(topseeds)):
        # #     topseeds[i] = topseeds[i].strip('1080p').strip() ; 

        # # topseeds = list(set(topseeds)) ;

        # self.names = topseeds_names
        # self.links = topseeds_links 
        

 
        
if __name__=='__main__':
    obj = yify() ; 
    obj.get_top_seeded_torrents() ;