import numpy as np


class Condition:
    def __init__(self):
        self.delta_t = float("{0:.2f}".format(self.delta_t))
        self.delta_x = float("{0:.2f}".format(self.delta_x))
        self.slope = float("{0:.2f}".format(self.slope))
        self.con = float("{0:.2f}".format(self.con))

    def condition_con_parameter(self):
        while True:
            try:
                if not self.con == float("{0:.2f}".format(self.con)):
                    raise ValueError('con its not valid')
                break
            except ValueError as error:
                print(error)
                break
        return self.con

    def condition_slope_parameter(self):
        while True:
            try:
                if not self.slope == float("{0:.2f}".format(self.slope)):
                    raise ValueError('slope its not valid')
                break
            except ValueError as error:
                print(error)
                break
        return self.slope

    def condition_delta_t_parameter(self):
        while True:
            try:
                if not self.delta_t == float("{0:.2f}".format(self.delta_t)):
                    raise ValueError('delta_t its not valid')
                break
            except ValueError as error:
                print(error)
                break
        return self.delta_t

    def condition_delta_x_parameter(self):
        while True:
            try:
                if not self.delta_x == float("{0:.2f}".format(self.delta_x)):
                    raise ValueError('delta_x its not valid')
                break
            except ValueError as error:
                print(error)
                break
        return self.delta_x
