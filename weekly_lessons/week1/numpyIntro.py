#!/usr/local/bin/python2

import sys
import numpy as np

def numpyIntro(argv):
  '''
  '''

  # Create a dumy data set to run some functions on
  # arange and linspace are two very useful ways of creating arrays.

  myArray = np.arange(16)

  myArray = myArray.reshape(4,4)

  anotherArray = np.linspace(1,6,10).reshape(2,5)

  print anotherArray

  # Numpy provides easy to access parameters discribing the structure of an array.

  # Print the shape of the array
  print myArray.shape
  # Print the number of dimensions of the array.  In this case
  # a 2D array
  print myArray.ndim
  # 
  print myArray.dtype
  print myArray.size

if __name__ == "__main__":
  numpyIntro(sys.argv[1:]);
