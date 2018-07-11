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
    #Remove key and ':'
    data = data[data.find(':')+1:]
    
    #break up line into words
    data = data.split()
    
    #Representsset of  all non-latin characters
    exp = re.compile('[^a-zA-Z]')
    temp = []
    for word in data:
        word = re.sub(exp,"", word) #remove all non-latin characters 

        word = word.lower()
        if word and word not in stops:
            if d.check(word) and len(word) >= 3: #if it is not an english word
                temp.append(word)
    return temp

def reader(file,d,stops): 
    for line in file:  #data will be file also
        yield parse(line,d,stops)
       # line = parse(line)
   # return line 

def main(separator='\t'):
    data = []
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


    knownTopTen = set(['trump','years','year','like','president','companies','last','business','bitcoin','billion'])
    #for twitter
  #  knownTopTen = set(['bitcoin','blockchain','people','crypto','ethereum','check','price','airdrop','amp','btc']) #this will be predetermined to add into correct list.
    for line in data:
        topTenFound = [] 
        nonTopTen = []

        for word in line: 
            if word not in knownTopTen: #if the word is not a top ten word
                nonTopTen.append(word)      #mark word is not top ten
            else:                       #Otherwise, the word is a top ten word.
                topTenFound.append(word) 

        for topWord in topTenFound:
            for nonTopWord in nonTopTen: 
                print('%s%s%s%s' % (topWord,  nonTopWord, separator, 1)) #pairs all top words and nontop words together for reducer i

        alreadyMatchedTops = []
        #Now we must deal with case where both are top words: each word must igore itself lol 
        topTenAlt = topTenFound 
        for topWord in topTenFound: 
            for topWordChild in topTenFound:
                try:
                    if topWord != topWordChild and alreadyMatchedTops.index([topWord,topWordChild]) == ValueError:
                        alreadyMatchedTops.append([topWord,topWordChild])
                        print('%s%s' % (topWord,'\t'  ,topWordChild, separator, 1)) #pairs all top words and nontop words together for reducer i
                except ValueError as e:
                    print(e)

if __name__ == '__main__':
    main()
