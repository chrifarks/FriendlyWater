import numpy as np

parameter = np.genfromtxt(fname='../data/parameters.txt', skip_header=1, delimiter=',', usecols=[1], dtype=float)
con = parameter[0]
slope = parameter[1]
delta_t = parameter[2]
delta_x = parameter[3]

for item in con:
    print(con)
if type(con) == str:
    print('value conveyance(km^3/s) its not valid.')
else:
    print('Correct value.')

if type(slope) == str:
    print('value slope its not valid.')
else:
    print('Correct value.')

if type(delta_t) == str:
    print('value delta_t(seconds) its not valid.')
else:
    print('Correct value.')

if type(delta_x) is str:
    print('value delta_x(m) its not valid.')
else:
    print('Correct value.')

print(parameter)
