import dateutil.parser as p
import pandas as pd
import re 

class ch4():
    def one(self):
        print('Snippet 1')
        print('ABC\t'.strip())
        print('ABC\t'.lstrip())
        print('ABC\t'.rstrip())
        print('ABC'.strip('C'))
        print('\n')

    def two(self):
        print('Snippet 2')
        s = 'abc\xFF'  
        print(type(s))
        print(s)
        print('Python3 omits decode ' + s + 'is already unicode')
        print('\n')

    def three(self):
        print('Snippet 3')
        print(p.parse('August 13, 1985'))
        print(p.parse('2013-8-13'))
        print(p.parse('2018-8-13 4:15am'))
        print('\n')

    def get_first_last_name(self, s):
        INVALID_NAME_PARTS = ['mr', 'ms', 'mrs',
                              'dr', 'jr', 'sir']
        
        parts = s.lower().replace('.', '').strip().split()
        parts = [p for p in parts 
                 if p not in INVALID_NAME_PARTS]
        if len(parts)==0:
            raise ValueError(
                'Name %s is formatted wrong' % s)
        first, last = parts[0], parts[-1]
        first = first[0].upper() + first[1:]
        last = last[0].upper() + first[1:]
        return first, last

    def format_age(self, s):
        chars = list(s) #list of characters
        digit_chars = [c for c in chars if c.isdigit()]
        return int(''.join(digit_chars))

    def format_date(self, s):
        MONTH_MAP = { 'jan': '01', 'feb': '02', 'may': '03'} #may == 03? lol
        s = s.strip().lower().replace(',', '')
        m, d, y = s.split()
        if len(y) == 2: y = '19' + y
        if len(d) == 1: '0' + d
        return y + '-' + MONTH_MAP[m[:3]] + '-' + d

    def four(self):
        print('Snippet 4')
        df = pd.read_csv('~/Documents/dev/courses/cse487/bit_data/src/part1/sample_data/format_script.tsv', sep='|')
        df['First Name'] = df['Name'].apply(
            lambda s: self.get_first_last_name(s) [0])
        df['Last Name'] = df['Name'].apply(
            lambda s: self.get_first_last_name(s) [1])
        df['Birthdate'] = df['Birthdate'].apply(
            self.format_date).astype(pd.datetime)
        print(df)
        print('\n')

    def five(self):
        print('Snippet 5')
        street_pattern = r"^[0-9]\s[A-Z] [a-z]*" + \
            r"(Street|St|Rd|Road|Ave|Avenue|Blvd|Way|Wy)\.?$"
        city_pattern = r"^[A-Z] [a-z]*,\s[A-Z]{2}, [0-9] {5}$"
        address_pattern = street_pattern + r"\n" +  city_pattern
        adress_re = re.compile(address_pattern)
        #text = open('../sample_data/xml_data.txt', 'r').read()
        #matches = re.findall(adress_re, text)

        #open('../sample_data/addresses_w_space_between.txt',
        #     'w').write('\n\n'.join(matches))

       # print('Matches: ' + matches + '\n')

    def six(self):
        print('Snippet 6')
        pattern = '\n'

        my_re = re.compile(pattern)
        print(my_re)

        pattern = '\\n'
        newline_re = re.compile(pattern)
        print(newline_re)
        print('\n')

    def main(self):
        print('Chapter 4 Results')
        self.one()
        self.two()
        self.three()
        #self.four() #create to files for addresses
        self.five()
        self.six()
        print('Chapter 4 results complete!' + '\n')
