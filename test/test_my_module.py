from my_package.my_module import add

import numpy as np

def test_add():
  assert add(3,4) == 7
  
def show_printing():
  matrix=np.random.rand(3,3)
  print(matrix)
  assert False
