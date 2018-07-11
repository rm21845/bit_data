import requests 
import ast 

"""
Originally sources from here:
https://github.com/MattDMo/NYTimesArticleAPI

It is modified under lisence 
"""

API_ROOT = 'http://api.nytimes.com/svc/search/v2/articlesearch'
API_SIGNUP_PAGE = 'http://developer.nytimes.com/docs/reference/keys'

class NoAPIKeyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class articleAPI(object):
    def __init__(self, key = None):
        self.key = key
        self.response_format = 'json'

        if self.key is None:
            raise NoAPIKeyException('Warning: Missing API Key. Please visit ' 
                    + API_SIGNUP_PAGE + ' to register for a key.')


    def format_returns(self,fl):
        for x in fl:
            self.returns += x + '%2C'
        self.returns = 'fl=' +  self.returns[:-3]
        
    def search(self,arguments):
        key = self.key

        url ='%s.json?api-key=%s' %  (
            API_ROOT, key
                )

        self.req = requests.get(url, params=arguments)
        return self.req.json()

