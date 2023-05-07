import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """Class for Geographic Position."""

    easting_m: float = 0.0
    northing_m: float = 0.0
    ellipsoidal_height_m: float = 0.0
    latitude_decimal_degree: float = 0.0

    def __post_init__(self):
        try:
            float(self.easting_m)
            float(self.northing_m)
            float(self.ellipsoidal_height_m)
            float(self.latitude_decimal_degree)
        except ValueError:
            raise Exception("The parameters must be float.")


@dataclass(frozen=True)
class WGS84:
    """Class for WGS84 Ellipsoid."""

    semi_major_axis: float = 6378137
    semi_minor_axis: float = 6356752.31424
    flattening: float = 298.257223563


class ScaleFactorUtm:
    """ Class for Scale Factor UTM Calculation."""

    def __init__(self, position: Position):
        self.position = position

    def calcul(self):
        """Calcul scale factor UTM."""
        x = self.position.easting_m - 500000
        q = 0.000001 * x
        k = 0.9996
        t = 0.006739497
        s = 6399593.626
        a = 1 + t * (math.cos(self.position.latitude_decimal_degree)) ** 2
        e = s / math.sqrt((1 + t * (math.cos(self.position.latitude_decimal_degree)) ** 2))
        b = (2 * e ** 2) * k
        p = (a/b) * pow(10, 12)
        d = (WGS84.semi_major_axis+self.position.ellipsoidal_height_m)/WGS84.semi_major_axis
        result = (k * (1 + p * (q ** 2) + 0.00003 * (q ** 2))) * d
        return result
