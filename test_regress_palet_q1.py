# -*- coding: cp1251 -*-
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
    (123, 0.45),
    ])
    
def test_regress_out__case_0001(how_much, size):
        result = calculator(how_much, size)
        assert 0 != size and how_much


#def test_regress_out__case_0002(how_much, size):
 #       try:
  #             result = how_much / size
   #     except ZeroDivisionError:
    #            print 'На ноль делить нельзя'
	
def test_regress_out__case_0003(how_much, size):
        result = calculator(how_much, size)
        assert type(result) != type(size) and type(how_much)

def test_regress_out__case_0004(how_much):
        assert isinstance(how_much, float)
        assert isinstance(size, float)
