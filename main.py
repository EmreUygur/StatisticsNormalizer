import sys
import pandas as pd


def fillColumns(df, column):

    return df[column].fillna(df[column].mean())


def getNormalizedDF(df):

    return (df - df.min())/(df.max() - df.min())


def main(inputFileName):

    inputDF = pd.read_excel(inputFileName)
    filledDF = pd.DataFrame()
    columns = inputDF.columns

    for column in columns:
        filledDF[column] = fillColumns(inputDF, column)

    getNormalizedDF(filledDF).to_excel('output_'+inputFileName, index=False)


main(sys.argv[1])
