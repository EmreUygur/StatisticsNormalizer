import sys
import pandas as pd
import numpy as np


def main(inputFileName):
    print(inputFileName)

    dataset = pd.read_csv(inputFileName)
    print(dataset.to_string())


try:
    main(sys.argv[1])
except IndexError:
    print('Please enter a csv file name')
except Exception as error:
    print(f'Error: {error}')
