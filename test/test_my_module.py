from my_package.my_module import add
import pytest

@pytest.mar.parametrize(
  "x,y,result", [(1,2,3),(3,4,7),(5,6,11)]

def test_add(x,y,result):
  assert add(x,y) == result
