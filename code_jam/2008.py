#! /usr/bin/python3

import itertools

def saveWorld(infile):
    
    with open(infile) as f:
        ncases = f.readline()
        ncase = 0

        n_search_engines = f.readline()
        
        while n_search_engines:
    
            search_engines = itertools.cycle([ f.readline().strip() for i in range( int(n_search_engines) ) ])
            n_searches = int(f.readline())
            searches = [ f.readline().strip() for i in range( n_searches ) ]
            n_search_engines = f.readline()

            switch = 0
            engine = next(search_engines)
            
            while searches:
                search = searches.pop(0)
                if search == engine:
                    switch += 1
                    engine = next(search_engines)

            ncase += 1
            print("Case #%s: %s" % (ncase, switch))

if __name__ == "__main__":
    import sys
    saveWorld(sys.argv[1])
            
    
        
