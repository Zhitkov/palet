import pytest
from palet import calculator
    
def test_regress_out__case_0001():
    result = calculator(20,5)
    assert result == 4
