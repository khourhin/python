#! /usr/bin/python

import progressbar
from time import sleep
bar = progressbar.ProgressBar(maxval=20,
                              widgets=[progressbar.Bar('=', '[', ']'),
                                       ' ', progressbar.Percentage()])
for i in xrange(20):
    bar.update(+1)
    sleep(3)
bar.finish()