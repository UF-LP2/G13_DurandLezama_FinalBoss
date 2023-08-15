""" trying to test our methods"""

import pytest
from src.cFinalBoss import Ship
from src.cFinalBoss import Cruise
from src.cFinalBoss import Cargo


def test_ship():
    penero_obj = Ship(30, 5)
    assert penero_obj.is_worth_it() == True


def test_cargo():
    cargo_obj = Cargo(0, 0, 30, 5)
    with pytest.raises(ValueError):
        cargo_obj.is_worth_it()


def test_Cruise():
    crucero = Cruise(0, 30, 5)
    assert crucero.is_worth_it() == True
