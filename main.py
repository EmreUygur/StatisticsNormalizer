import sys
import pandas as pd


def fillColumns(df, column):

    return df[column].fillna(df[column].mean())


def getNormalizedDF(df):

    return (df - df.min())/(df.max() - df.min())


def main(inputFileName):

    inputDF = pd.read_csv(inputFileName)
    filledDF = pd.DataFrame()
    columns = inputDF.columns

    for column in columns:
        filledDF[column] = fillColumns(inputDF, column)

    filledDF.to_excel('output_'+inputFileName+'.xlsx',
                      index=False, header=False)

    getNormalizedDF(filledDF.transpose()).to_excel(
        'output_normalized-and-trasnpozed_'+inputFileName+'.xlsx', index=False, header=False)


main(sys.argv[1])
