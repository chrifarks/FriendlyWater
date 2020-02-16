import numpy as np
from app import condition as c

# import matplotlib.pyplot as plt

parameter = np.genfromtxt(fname='../data/parameters.txt', skip_header=1, delimiter=',', usecols=[1])
class Pm:
    def __init__(self):
        self.slope = parameter[1]
        self.con = parameter[0]

    @staticmethod
    def Con():
        if con == float("{0:.2f}".format(con)):
            print('value conveyance(km^3/s) its not valid.')
        if not con == float("{0:.2f}".format(con)):
            raise ValueError('conveyance(km^3/s) its not valid')

    def Slope(self):
        return slope(c)

    def delta_T(self):
        self.delta_t = parameter[2]
        return delta_t(c)
    def delta_x(self):
        self.delta_x = parameter[3]
        return delta_x


while True:
    try:
        con = float("{0:.2f}".format(con))
        if not con == float("{0:.2f}".format(con)):
            raise ValueError('con its not valid')
        break
    except ValueError as error:
        print(error)
        break

while True:
    try:
        slope = float("{0:.2f}".format(slope))
        if not slope == float("{0:.2f}".format(slope)):
            raise ValueError('slope its not valid')
        break
    except ValueError as error:
        print(error)
        break

while True:
    try:
        delta_t = float("{0:.2f}".format(delta_t))
        if not delta_t == float("{0:.2f}".format(delta_t)):
            raise ValueError('delta_t its not valid')
        break
    except ValueError as error:
        print(error)
        break

while True:
    try:
        delta_x = float("{0:.2f}".format(delta_x))
        if not delta_x == float("{0:.2f}".format(delta_x)):
            raise ValueError('delta_x its not valid')
        break
    except ValueError as error:
        print(error)
        break

print(parameter)

bcl = np.genfromtxt(fname='../data/boundaries_left.txt', skip_header=2, delimiter=',', usecols=(0, 1, 2))
Q_left: float = bcl[:, 0:2]

while True:
    try:
        Q_left = float("{0:.2f}".format(Q_left))
        if not Q_left == float("{0:.2f}".format(Q_left)):
            raise ValueError('boundaries_left its not valid')
        break
    except ValueError as error:
        print(error)
        break

print(Q_left)

bcr = np.genfromtxt(fname='../data/boundaries_right.txt', skip_header=2, delimiter=',', usecols=(0, 1, 2))

# ini = np.genfromtxt(fname='../dados/ini.txt', skip_header=2, delimiter=',', usecols=(0, 1, 2))
channel = np.genfromtxt(fname='../data/channel.txt', skip_header=1, delimiter=',', usecols=[1])
