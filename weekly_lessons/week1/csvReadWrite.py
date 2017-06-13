#!/usr/local/bin/Python3

import sys
import csv
import numpy as np

def csvReadWrite(argv):
    '''
    Read in data from a CSV file and compute discriptive statistics.
    Write a CSV file from a 2D array.
    '''

    # Create a list in the function level namespace
    li = []

    # It is best to use the 'with' construct when working with functions
    # that involve file I/O
    with open(argv[0], 'r') as csvfile:
        dataReader = csv.reader(csvfile)
        # Converts each line in the CSV file to a Python list.
        for row in dataReader:
            # We are creating a 2D list
            li.append(row)
            #print(row)

    # Now convert to a numpy array
    myArray = np.array(li)

    print(myArray)
    # The ndarray.flatten() method returns the array
    # converted to a 1D array.
    print(myArray.flatten())
    # This removes the first row and first column
    # then casts the data to float type
    # The first row of a CSV file is usually the titles of
    # the columns.  The first column of the data I am
    # using is names and cannot be cast to floats
    # Numpy has more flexible numeric data types than regular python types.
    newArray = myArray[1:,1:].astype(np.float64)
    # Find the median points per game and assists per game.
    # 'axis=0' tells median to compute for each column
    # 'axis=1' would compute for the rows.
    #
    print(np.median(newArray, axis=0))
    # The axis parameter is common to most of the discriptive
    # statistical methods.
    print(np.average(newArray, axis=0))
    print(np.std(newArray, axis=0))
    # More stats methods are documented at:
    # https://docs.scipy.org/doc/numpy-dev/reference/routines.statistics.html

    # arange method is like the python range method, but gives an Numpy array.
    # reshape converts the 16 element 1D array to a 4x4 2D array.
    outArray = np.arange(16).reshape(4,4)

    # Write this data out to a csv file.
    with open('myOutput.csv', 'w') as newCSV:
        csvWriter = csv.writer(newCSV)
        for row in outArray:
            csvWriter.writerow(row)

if __name__ == "__main__":
    csvReadWrite(sys.argv[1:])
