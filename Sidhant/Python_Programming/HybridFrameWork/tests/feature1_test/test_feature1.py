import pytest


class TestFeature1:
    @pytest.mark.smoke
    def test_addition(self):
        n1 = 8
        n2 = 90
        assert n1 + n2 == 98

    @pytest.mark.smoke
    def test_multiplication(self):
        n1 = 8
        n2 = 90
        assert n1 * n2 == 720

    @pytest.mark.smoke
    def test_divison(self):
        n1 = 40
        n2 = 10
        assert n1 // n2 == 4

    @pytest.mark.sanity
    def test_subtraction(self):
        n1 = 98
        n2 = 90
        assert n1 - n2
