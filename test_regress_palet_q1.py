
import pytest
from palet import calculator





@pytest.mark.parametrize("how_much, size", [
    (0,0),
    (12,0),
    (0,13)
    ])
def test_negative_Zero_and_spec_symbols_regress_out__case_0001(how_much, size):
                with pytest.raises(TypeError):
                        calculator(how_much, size)
                        myError = TypeError('fun considers zero')
                        raise myError


@pytest.mark.parametrize("how_much, size", [
    ("d",12),
    (12,"d")
    ])
def test__negative_char_regress_out__case_0002(how_much, size):
        with pytest.raises(TypeError):
                calculator(how_much, size)
                myError = TypeError('fun considers string')
                raise myError


@pytest.mark.parametrize("how_much, size", [
    (123, 0.45),
    (0.45, 0.45),
    (0.45, 45)
    ])
def test_negative_float_regress_out__case_0003(how_much, size):
        with pytest.raises(TypeError):
                calculator(how_much, size)
                myError = TypeError('fun considers float')
                raise myError


@pytest.mark.parametrize("how_much, size", [
    (-23,-23),
    (23,-23),
    (-24,25),
    (-24,25)
    ])
def test_negative_int_regress_out__case_0004(how_much, size):
        with pytest.raises(ZeroDivisionError):
                calculator(how_much, size)
                myError = ZeroDivisionError('fun considers negative int')
                raise myError


@pytest.mark.parametrize("how_much, size", [
    (125, 5),
    (123, 5)
    ])
def test_positive_int_regress_out__case_0005(how_much, size):
        with pytest.raises(ValueError):
                if how_much and size > 0:
                        myError = ValueError('fun is incorect with possitive int')
                        raise myError
                        print(show_much, size)

@pytest.mark.parametrize("how_much, size", [
    (126, 5),
    (123, 7),
    ])
def test_positive_int_regress_out__case_0007(how_much, size):
        a = 0
        b = calculator(how_much, size)
        assert a == b, "fun is incorect considers"


@pytest.mark.parametrize("how_much, size", [
    (125, 5),
    (200, 5),
    ])
def test_positive_int_regress_out__case_0008(how_much, size):
    a =( how_much / size)
    b = calculator(how_much, size)
    assert a == b, "fun is incorect considers"


@pytest.mark.parametrize("how_much, size", [
    (25,23),
    (129, 128)
    ])
def test_pallet_too_big_regress_out__case_0009(how_much, size):
        with pytest.raises(ZeroDivisionError):
                calculator(how_much, size)
                myError = ZeroDivisionError('fun considers negative int')
                raise myError
