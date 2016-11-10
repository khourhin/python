import numpy as np
import matplotlib.pyplot as plt

# Working on dataframes in python ! So exciting !
# This is an ugly stub

bed="demo_data/HP1G_CTCF_closest.weirdbed"

bed_closest_res = np.genfromtxt(bed, dtype=None,
                                names="chrA, startA, endA, nameA, scoreA, chrB, startB, endB, misteryB1, scoreB, misteryB2, misteryB3, misteryB4, misteryB5, distance")


res_d = bed_closest_res['distance']
print res_d
print np.mean(res_d)
#plt.hist(res_d, range(0, max(res_d), 100))
#plt.show()
