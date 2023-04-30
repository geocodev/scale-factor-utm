import pytest

from scale_factor_utm_gui.scale_factor_utm import Position
from scale_factor_utm_gui.scale_factor_utm import ScaleFactorUtm
from scale_factor_utm_gui.scale_factor_utm import WGS84


class TestPosition:

    def test_init_position_when_is_successful(self):
        """Test init position when is successful."""
        position = Position(
            easting_m=645182.25,
            northing_m=989187.79,
            ellipsoidal_height_m=90.144,
            latitude_decimal_degree=8.88363
        )
        assert 645182.25 == position.easting_m
        assert 989187.79 == position.northing_m
        assert 90.144 == position.ellipsoidal_height_m
        assert 8.88363 == position.latitude_decimal_degree

    def test_init_position_when_is_failed(self):
        """Test init position when is failed."""
        with pytest.raises(Exception):
            Position(
                easting_m="test",
                northing_m=989187.79,
                ellipsoidal_height_m=90.144,
                latitude_decimal_degree=8.88363
            )

    def test_init_position_when_value_is_changed(self):
        """Test init position when value is changed."""
        with pytest.raises(Exception):
            position = Position(
                easting_m=645182.25,
                northing_m=989187.79,
                ellipsoidal_height_m=90.144,
                latitude_decimal_degree=8.88363
            )
            assert 5 == position.easting_m


class TestWGS84:

    def test_WGS84_when_is_successful(self):
        """Test init WSG84 when is successful."""
        assert 6378137 == WGS84.semi_major_axis
        assert 6356752.31424 == WGS84.semi_minor_axis
        assert 298.257223563 == WGS84.flattening

    def test_WGS84_when_value_is_changed(self):
        """Test init WSG84 when value is changed."""
        with pytest.raises(Exception):
            assert 3 == WGS84.semi_major_axis


class TestScaleFactorUtm:

    def test_init_scale_factor_utm_when_is_successful(self):
        """Test init scale factor UTM when is successful."""
        position = Position(
            easting_m=645182.25,
            northing_m=989187.79,
            ellipsoidal_height_m=90.144,
            latitude_decimal_degree=8.88363
        )
        scale_factor_utm = ScaleFactorUtm(position=position)
        assert position == scale_factor_utm.position

    @pytest.mark.parametrize(
        "easting_m, northing_m, ellipsoidal_height_m, latitude_decimal_degree, expected",
        [
            (645182.25, 989187.79, 90.144, 8.88363, 0.9998746489732164),
            (644867.10, 988436.60, 90.75, 8.88364, 0.999873614192414),
            (648408.397, 990164.792, 124.026, 8.88352, 0.9998916670697315),
            (830245.43, 951382.66, 39.12, 8.87388, 1.0009539641672356)
        ]
    )
    def test_calcul_when_is_successful(
        self,
        easting_m,
        northing_m,
        ellipsoidal_height_m,
        latitude_decimal_degree,
        expected
    ):
        """Test calcul of scale factor UTM when is successful."""
        position = Position(
            easting_m=easting_m,
            northing_m=northing_m,
            ellipsoidal_height_m=ellipsoidal_height_m,
            latitude_decimal_degree=latitude_decimal_degree
        )
        scale_factor_utm = ScaleFactorUtm(position=position)
        assert expected == scale_factor_utm.calcul()
