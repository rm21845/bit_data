"""Bit Data 
MIT license 
Copyright (c) 2018 Ronald Davis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from twit_collect import twit_collect 
from news_collect import news_collect
from fileio import fileio 
#from mapper import mapper
#from reducer import reducer 
import argparse as ag 

"""TODO:

    tweet_collect TODO:
       - find (lat,long) of tweets)
       - filter out non-us outs and restrict to us    

    news_collect TODO:
    multi-threading for both nyt collect and twitter collect
    multi-threading for collection and mr 
    implement automation to hadoop server
    
    required arguments: query string
    optional arguments: # of tweets, # of articles

    Words used:
        bitcoin, btc, crypto, cryptocurrency, blockchain
"""

def arg_handler():
    parse = ag.ArgumentParser()
    parse.add_argument('bitcoin', type=str)
    parse.add_argument('tweets', type=int)
    parse.add_argument('articles', type=int)
    parse.add_argument('page', type=int)
    arguments = parse.parse_args() 

    word = arguments.bitcoin 
    tweets = arguments.tweets 
    articles = arguments.articles
    page = arguments.page 
    
    return [word,tweets,articles,page]

def collect(arg):
    t_collect = twit_collect(arg[0])
    t_collect.search(arg[1])    
    
    nyt_collector = news_collect(arg[0])
    nyt_collector.search(arg[2], arg[3])

def main():
    print('Bit Data by Ron Davis 2018')
    #input: python main.py bitcoin 2000 1000
    arg = arg_handler()
    collect(arg)

if __name__ == '__main__':
    main()
