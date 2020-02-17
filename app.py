import pandas as pd
import conf
import yaml
from friendlywater.water_stream import *
from importlib.resources import open_text
from typing import TextIO
from pandas import DataFrame


def load_csv(file: TextIO, cols) -> DataFrame:
    try:
        return pd.read_csv(file, delimiter=';', header=0, names=cols,
                           dtype={
                               cols[0]: "float64",
                               cols[1]: "float64",
                               cols[2]: "float64"
                           })

    except (TypeError, ValueError) as ex:
        print("Invalid data on {file}: Columns must not contain strings".format(file=file.name))
        exit(1)


data = yaml.load(open_text(conf, 'application.yaml'), Loader=yaml.FullLoader)

water_stream = WaterStream(
    slope=data.get('stream').get('slope'),
    conveyance=data.get('stream').get('conveyance'),
    delta_t=data.get('stream').get('delta_t'),
    delta_x=data.get('stream').get('delta_x')
)
water_channel = WaterChannel(
    length_in_meters=data.get('channel').get('length'),
    height_in_meters=data.get('channel').get('height'),
    width_in_meters=data.get('channel').get('width')
)

initial = load_csv(file=open_text(conf, 'initial_conditions.csv'),
                   cols=['time', 'q0', 'h0'])

bound_left = load_csv(file=open_text(conf, 'boundaries_left.csv'),
                      cols=['time', 'q_left', 'h_left'])

bound_right = load_csv(file=open_text(conf, 'boundaries_right.csv'),
                       cols=['time', 'q_right', 'h_right'])

boundaries = pd.DataFrame({
    'time': bound_left['time'],
    'q_left': bound_left['q_left'],
    'q_right': bound_right['q_right'],
    'h_left': bound_left['h_left'],
    'h_right': bound_right['h_right']
})
