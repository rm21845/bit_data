#!/usr/bin/env python
import re 
import enchant
import sys
from nltk.corpus import stopwords

def parse(data):
    data = data.split()
    exp = re.compile('[^a-zA-Z]')
    
    temp = []
    for word in data:
        word = re.sub(exp,"", word)
        temp = word
    return temp

def reader(file): 
    for line in file:
        yield parse(line)

def main(separator='\t'):
    data = reader(sys.stdin)

    """
        let ds == smallest ds -- data
        let topTenFound be {list of top ten words found}
        Let a co-occurence be a single co-occurent mapping ie <"toptenfound '\t' cooccuring word" '\t' 1>
        Let nonTopTen be a list of words that co-occur with a top ten word but are not a top 10 word
    """
    knownTopTen = set()
    for line in data:
        topTenFound = [] 
        nonTopTen = []

        for word in line: 
            if word not in knownTopTen:
                nonTopTen.append()
            else:
                topTenFound.add(word) 

        for topWord in topTenFound:
            for nonTopWord in nonTopTen: 
                print('%s%s%s%s' % (topWord, nonTopWord, separator, 1))

        alreadyMatchedTops = []
        topTenAlt = topTenFound
        for topWord in topTenFound: 
            for topWordChild in topTenFound: 
                if topWord != topWordChild and alreadyMatchedTops.index([topWord,topWordChild]) == ValueError:
                    alreadyMatchedTops.append([topWord,topWordChild])
                    print('%s%s%s%s' % (topWord, topWordChild, separator, 1))

if __name__ == '__main__':
    main()