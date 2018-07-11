from pathlib import Path

class fileio(object):
    def __init__(self, mode=''):
        self.mode = mode #either 'tweet' or 'article', 'map', 'reduce' 
        self.p = self.__setp(mode)

    def store(self, data):
        if self.mode == 'tweet':
           self.__tstore(data)
        else:
           self.__astore(data)

    def __tstore(self, data):
        """Mapping:(data -> file)
            id -> key
            <id, time> -> time 
            <id, location> -> location 
            <id, words> -> words 
        """
        print('Storing Tweets' + '\n')

        for item in data:
            if not self.__id_exists(item['key']):
                #store all data in files
                self.ins_f(item, 'key')
                self.ins_f(item, 'time')
                self.ins_f(item, 'location')
                self.ins_f(item, 'words')
                      
    def __astore(self, data):
        """Mapping:
            id -> key 
            <id,time> -> time
            <id, url> -> url 
            <id, words> -> words
        """
        print('Storing Articles' + '\n')

        for item in data:
            if not self.__id_exists(item['key'],data):
                self.ins_f(item, 'key')
                self.ins_f(item, 'time')
                self.ins_f(item, 'url')
                self.ins_f(item, 'words')

    def ins_f(self, item, f_type):
        """Safely insert item into correct file type"""
        with open(str(self.p / f_type),'a') as f:
            try:
                if f_type == 'key':
                    f.write(item[f_type] + '\n')
                else: #handle <key,value> insert
                    pair = item['key'] + ':' + item[f_type]
                    f.write(pair + '\n') 
            finally:
                    f.close()

    def __id_exists(self, key, data={}):
        #TODO: search is foobar lol
        with open(str(self.p / 'key'), 'r') as foo:
            try:
                for bar in foo:
                    if (bar == key): 
                        return True 
            finally:
                foo.close()
        return False

    def __setp(self, mode):
        """set directory path based on mode"""
        if self.mode == 'tweet':
            return  Path('./TwitterData/')
        elif self.mode == 'article':
            return Path('./NewsData/')
        else:
            return Path('')

    def give_p(self):
        return self.p

    def keysort():
       #TODO:sort keys in a given file for search optimization
        print('in fileio.keysort')

    def removeDups(self, mode, day, filename):
        """
            Remove duplicate occurences in dataset
            Arguments: 
                Mode: [TwitterData,NewsData]
                Day: [Day1, Day2, Day3,...,DayN]
                Filename: [key,time,words,location,etc]
        """

        f = '/home/cam/Documents/dev/courses/cse487/bit_data/src/part2/%s/%s/%s' % (mode,day,filename)
        uniques = set()
        #Key file
        with open(f) as keyfile:
            for line in keyfile:
                line.rstrip('\n')
                uniques.add(line)

        with open(f, 'w') as j:
            for line in uniques:
               j.write(line)             
        uniques.clear()

    def removeTwitterDups(self, day):
        f = '/home/cam/Documents/dev/courses/cse487/bit_data/src/part2/TwitterData/%s/words' % (day)
        uniques = set()
        words = []
        #Key file
        with open(f) as keyfile:
            for line in keyfile:
                line.rstrip('\n')
                key = line[:line.find(':')+1]
                word = line[line.find(':')+1:]
                if key not in uniques: 
                    uniques.add(line)
                    words.append(word)

        with open(f, 'w') as j:
            for line in words:
               j.write(line)             
        uniques.clear()