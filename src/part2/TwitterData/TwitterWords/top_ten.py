#!/usr/bin/python

import re
import math

def main():
    MAX_NUMBER = 10
    topTen = []# list of
    # <key,value> # pairs where key is word and value is #

    mapping = [] #items will be key, value: number, word respectively`
    nonLatin = re.compile('[^a-zA-Z]')
    nonNumerical = re.compile('[^0-9]') 
    keys = [] 

    topTenNumbers = []
    with open('./t1', 'rb') as f:        #t1 will be paired with n1 ie smallest ds
        for word in f:

            nonLatin = re.compile('[^a-zA-Z]')
            nonNumerical = re.compile('[^0-9]') 

            #This is the word 
            value = re.sub(nonLatin,"", word) #remove all non-latin charactersi 

            #This is the number(key)
            key = re.sub(nonNumerical,"",word)

            #number, value dictionary
            temp = {key, value}

            #list of keys for searching
            keys.append(key)

            #Collects all the maps
            mapping.append(temp) 
    f.close()
def ok(): 
    while(len(topTen) != MAX_NUMBER+1):
        topTenNumbers.append(max(keys))
        keys.remove(max(keys)        
     #   for x in topTenNumbers:
      #      topTen.append(keys[x])    
       #     print(topTen)
if __name_ == '__main__':

main()
