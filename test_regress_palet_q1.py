import pytest
from palet import calculator

@pytest.mark.parametrize("how_much, size", [
    ("d",12),
    ([12],3),
    (0,0),
    (12,0),
    (0,13),
    (23,-23),
    (-24,-25),
    (123, 0.45)
    ])
    
def test_regress_out__case_0001(how_much, size):
    result = calculator(how_much, size)
    return
