#! /usr/bin/python

import matplotlib.pyplot as plt

def make_graphs2():
    xs = range(11)
    ys = range(11)

    plt.close()
    f = plt.figure()

def make_graphs():

    x = range(11)
    y = range(11)

    # set axis setup:
    plt.axis([0, 10, 0, 10])

    # ticks With characters
    plt.xticks([3,6,9],["Groupe 1","Groupe 2","..."])
    # trick using list comprehensions (range does not give floats !)
    plt.yticks([ z * 0.1 for z in range(0,100,5) ])

    # title (with TeX integrated):
    plt.title(" This is the title with a power: $x^{3}/3$")

    # axis labels:
    plt.xlabel('x axis')
    plt.ylabel('y axis')

    # plot
    plt.plot(x,y)
    
    # add line with legend and with normal distribution:

    import math # only for sqrt
    import numpy as np # to get lots of points 
    import matplotlib.mlab as mlab # for the norm distrib

    i = np.linspace(0,10,100)
    mean = 5

    for v in [ x/100.0 for x in [5,50,500] ]:
        variance = v
        sigma = math.sqrt(variance)
        plt.plot(i, mlab.normpdf(i, mean, sigma), label="v="+str(v))
        
    plt.legend()

    # different line style:
    from itertools import cycle # cool stuff to cycle through

    lines = ["-","--","-.",":"]
    l_cycler = cycle(lines)

    for i in range(-2,3):
        x = range(i, i+10)
        plt.plot(range(10), x, next(l_cycler))

    # scatter plot:
    x = [ i * 0.25 for i in range(0,200)]
    y = [ i**2 for i in x ]
    ymin = [0.25] * 200
    ymax = [0.5] * 200

    plt.scatter(x, y)

    # same with line and errors
    plt.errorbar(x,y,yerr=(ymin,ymax), ecolor="green")
        
    # the interactive viewer
    #plt.show()

    # to save plot to a file
    plt.savefig('example01.png')

    plt.close()
    
def inv_cum_hist():

    """ Make an inverse cumulated histogram  """

    import pickle
    import math as m

    data = pickle.load(open("data/seq_len_dict.pick", "rb"))
    seq_lens = data.values()

    # Get the rounded max value for max bin:
    len_max = int( ( m.ceil(max(seq_lens)/1000.0 )) * 1000 )

    bins = range(0, len_max, 500)

    
    cum_freq = []
    for i in bins:
        cum_freq.append( len([ x for x in seq_lens if x >= i]) )

    plt.bar(bins, cum_freq, 500)
    plt.title("Reverse cumulative frequencies")
    plt.xlabel("length in bp")
    plt.ylabel("Number of sequences")
    plt.savefig('example01.png')

def subplots():
    """ Making several plots on one figure
    For more:
    http://matplotlib.org/examples/pylab_examples/subplots_demo.html
    """
    x = range(10)
    y = range(10)
    f, ax =  plt.subplots(2,1,sharex=True)
    ax[0].plot(x,y)
    ax[1].scatter(x,y)
    plt.savefig('example01.png')


def plot_GO_freq(infile):
    """ TO check for real working function, check GO_lib"""
    import matplotlib.pyplot as plt
    import numpy as np

    go_freq = get_GO_freq(infile)
    go_freq_sort = sorted(go_freq, key=lambda tup: -tup[1])

    #filtering out GO appearing only once:
    go_freq_sort = [ (g, f) for g, f in go_freq_sort if f > 1 ]
    
    print go_freq_sort

    go_dict = make_GO_dict("/home/tiennou/Downloads/gene_ontology_ext.obo")
    go_ids = [ x[0] for x in go_freq_sort ]
    go_names = [ go_dict[x][0] for x in go_ids ]
    
    h = plt.bar(range(len(go_freq_sort)),[ x[1] for x in go_freq_sort ])
    ticks_pos = [0.6*patch.get_width() + patch.get_xy()[0] for patch in h]
    plt.tick_params(bottom='off',top='off',right='off')
    plt.xticks(ticks_pos, go_names, rotation=45, ha='right',size=8)
    
    plt.tight_layout()
    
    plt.savefig("/home/tiennou/Desktop/test.png")
    plt.close()

    
#-------------------------------------------------------------------------------
if __name__ == "__main__":

#    make_graphs()
#    inv_cum_hist()
#    subplots()
    make_graphs2()
