from ch3.ch3 import ch3
from ch4.ch4 import ch4 
from ch5.ch5 import ch5

"""TODO & FIXES:
Do ch3 if there is time

ch4.five -> create proper text files, four has the same problem

ch5.seven() has no labels found
ch5.five() have to print properly 
ch5.twelve -> link is discontinued by Yahoo, foo.csv does not exist
Make sure images are exported to subdirectory
"""

class main():
    def run(self):
        ch3().main()
        ch4().main()
        ch5().main()

if __name__ == '__main__':
    main().run()
