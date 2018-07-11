import re
import  lib.search_api as nyt
import datetime as dt 
import time
from collections import OrderedDict
from fileio import fileio


class news_collect(object):
    def __init__(self, word):
        self.word = word;
        self.key = 'TOKEN OR SYS VAR'
        self.api = self.get_api()
        self.f = fileio('article')
        self.curr_date = dt.date.today()
        self.dft_dating = self.back_date()
        self.page_count = 0
        self.return_fields = ['web_url', 'snippet', 'pub_date','_id']
        self.srch_args = OrderedDict([('q',self.word), ('end_date',self.dft_dating),('page',self.page_count)])
        self.outputs = []
        self.max_outputs = 0
        self.output_total = 0

    def get_auth(self):
        return nyt.articleAPI(self.key)

    def get_api(self):
        return self.get_auth()

    def search(self, max_outputs=10000, page=0):
        #TODO:Set max outs as current_rate_lim * 10
        self.max_outputs = max_outputs 
        self.page_count = page
        self.srch_args['page'] = self.page_count 

        while (self.output_total < self.max_outputs):
            self.combine(self.api.search(self.srch_args))

            time.sleep(1) #temp sleep to prevent 429 
            self.page_count = self.page_count + 1
            self.srch_args['page'] = self.page_count
            print('Args Are : '+ str(self.srch_args))
            if(len(self.outputs) >= 40):
                self.store()

        self.store()
        print('Article collect Terminating') 
        self.outputs.clear()
        self.output_total = 0
        self.max_outputs = 0

    def combine(self, results):
        y = results['response']['docs']

        for result in y:
            temp = {}
            temp['url'] = result['web_url']
            temp['words'] = result['snippet']
            temp['time'] = result['pub_date']
            temp['key'] = result['_id']

            self.outputs.append(temp)
            self.output_total += 1
            if(self.output_total >= self.max_outputs):
                break

    def store(self):
        self.f.store(self.outputs)
        self.outputs.clear()

    def back_date(self, days=7):
        return re.sub('\D','', (str(self.curr_date - dt.timedelta(days=7)))) 

    def page_reset():
        self.page_count = 0

    def limit(self):
        self.api.rate_limit()

    def removeDups(self, mode, day):
        path = self.f.give_p() 
        """This needs to be modularized later
        open file and put into temp file 
        it all does the same thing in 10 lines
        """
        print('removing dups in news files')

        uniques = set()
        with open(path) as keyfile:
            for line in keyfile:
                line.rstrip('\n')
                uniques.add(line)

        with open(str(path), 'w') as f:
            for line in uniques:
               f.write(line)             
        uniques.clear()

        with open(str(path / 'time')) as keyfile:
            for line in keyfile:
                line.rstrip('\n')
                uniques.add(line)

        with open(str(path / 'time'), 'w') as f:
            for line in uniques:
               f.write(line)             
        uniques.clear()

        with open(str(path / 'url')) as keyfile:
            for line in keyfile:
                line.rstrip('\n')
                uniques.add(line)

        with open(str(path / 'url'), 'w') as f:
            for line in uniques:
               f.write(line)             
        uniques.clear()

        with open(str(path / 'words')) as keyfile:
            for line in keyfile:
                line.rstrip('\n')
                uniques.add(line)

        with open(str(path / 'words'), 'w') as f:
            for line in uniques:
               f.write(line)             
        uniques.clear()
