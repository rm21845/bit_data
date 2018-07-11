#!/usr/bin/env python
import re 
import enchant
import sys
from nltk.corpus import stopwords


def parse(data,d,stops):
    """filters out unwanted characters
            Remove Key and ':'
            Remove special characters
            Remove stop words
            This is either repeating words or there are copies of tweets
    """
    data = data[data.find(':')+1:]
    data = data.split()
    exp = re.compile('[^a-zA-Z]')
    temp = []

    for word in data:
        word = re.sub(exp,"", word)
        word = word.lower()
        if word and word not in stops:
            if d.check(word) and len(word) >= 3:
                temp.append(word)
    return temp

def reader(file,d,stops): 
    for line in file:
        yield parse(line, d, stops)

def main(separator='\t'):
    d = enchant.Dict('en_US') 
    d.add('bitcoin')
    d.add('btc')
    d.add('ethereum')
    d.add('blockchain')
    d.add('trump')
    d.add('crypto')
    d.add('crpytocurrency')
    d.add('satoshi')
    d.add('blockchain')
    stops = set(stopwords.words('english'))
    data = reader(sys.stdin,d,stops)  

    for x in data:
        for that in x:
            print('%s%s%d' % (that, separator, 1))
    print('complete')

if __name__ == '__main__':
    main()
