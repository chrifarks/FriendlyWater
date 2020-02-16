from dataclasses import dataclass
from dataclass_type_validator import dataclass_type_validator, TypeValidationError


@dataclass(frozen=False)
class WaterStream:
    slope: float
    conveyance: float
    delta_t: int
    delta_x: float

    def __post_init__(self):
        dataclass_type_validator(self)


@dataclass(frozen=False)
class WaterWay:
    length_in_meters: int
    height_in_meters: int
    width_in_meters: int

    def __post_init__(self):
        dataclass_type_validator(self)
