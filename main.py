import sys
import pandas as pd
import numpy as np


def main(inputFileName):

    inputDF = pd.read_csv(inputFileName)
    outputDF = pd.DataFrame()
    columns = inputDF.columns

    for column in columns:
        outputDF[column] = inputDF[column].fillna(inputDF[column].mean())

    outputDF.to_csv('output_'+inputFileName, index=False)


try:
    main(sys.argv[1])
except IndexError:
    print('Please enter a csv file name')
except Exception as error:
    print(f'Error: {error}')
