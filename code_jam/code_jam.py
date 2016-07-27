#! /usr/bin/python3

import itertools

def getData(infile):
    with open(infile, "r") as f:
        ncases = int(f.readline().strip())
        
        data = []

        line = f.readline().strip()
        while line:
            ncredit = int(line)
            nitems = int(f.readline().strip())
            items_price = [ int(x) for x in f.readline().strip().split()]
            data.append((ncredit, nitems, items_price))
            line = f.readline().strip()

        if len(data) != ncases:
                raise IOError("Not correct number of cases in the input file")
        return data

def getItems(data):
    count = 0
    for shop in data:
        count += 1
        
        for i in itertools.combinations(shop[2], 2):
            if sum(i) == shop[0]:
                indexes = " ".join(sorted([ str(shop[2].index(x) + 1) for x in i ]))

        print("Case #{0}: {1}".format( count, indexes) )

if __name__ == "__main__":

    import sys
    data = getData(sys.argv[1])
    getItems(data)
