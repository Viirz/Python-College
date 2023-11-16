# q: is there a library for bisection function in python?
# a: yes, it's called scipy.optimize.bisect

import scipy.optimize as opt
f = lambda x: 5*x**2 + 2*x
result = opt.bisect(f, 0, 5)
# print with 3 decimal places
print('%.3f' % result)