import tweepy as tpy
from fileio import fileio

class twit_collect(object):
    def __init__(self, word):
        self.word = word;
        self.key = 'ADD'
        self.secret = 'ADD'
        self.auth = self.get_auth() 
        self.api = self.get_api()
        self.tweets = [] 
        self.tweet_total = 0
        self.max_tweets = 0
        self.f = fileio('tweet')

    def get_auth(self):
        return tpy.AppAuthHandler(self.key, self.secret)

    def get_api(self):
        return tpy.API(self.auth, wait_on_rate_limit= True, 
                wait_on_rate_limit_notify = True)

    def search(self, max_tweets=50000):
        self.max_tweets = max_tweets 
        while(self.tweet_total < self.max_tweets):
            self.combine(self.api.search(self.word,rpp=100, show_user = True))
            if(len(self.tweets) >= 40):
                self.store()

        self.store()
        print('Tweet collect Terminating')
        print('Tweets collected' + str(self.tweet_total))
        self.tweets.clear()
        self.tweet_total = 0
        self.max_tweets = 0

    def combine(self, results):
        for result in results:
            location = self.find_locale(result.user)
            if (location != 'NONE'):
                temp = {}
                temp['time'] = str(result.created_at)
                temp['key'] = result.id_str
                temp['location'] = result.user.location 
                temp['words'] = result.text 
                self.tweet_total += 1
                self.tweets.append(temp)
                
                if(self.tweet_total >= self.max_tweets):
                    break

    def store(self):
        self.f.store(self.tweets)
        self.tweets.clear() 

    def find_locale(self, user):
        located = self.api.get_user(user.screen_name).location
        if not located.strip():
            return 'NONE'
        else:
            return located