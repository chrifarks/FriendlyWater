from dataclasses import dataclass
from dataclass_type_validator import dataclass_type_validator, TypeValidationError


@dataclass(frozen=False)
class WaterStream:
    slope: float
    conveyance: float
    delta_t: float
    delta_x = float

    def __post_init__(self):
        dataclass_type_validator(self)
