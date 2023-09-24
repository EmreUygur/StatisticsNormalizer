# Statistics Normalizer

This python script is designed to filling empty values on .csv file by aggregating value and export the normalized table and generate 2 .xlsx files which are

- Dataset with empty columns are filled
- Normalized and transposed dataset

## Requirements

- [Python v3.7+](https://www.python.org/downloads/)
- [Pip](https://pypi.org/)
- [Pandas](https://pandas.pydata.org/)

## To Run

```sh
python .\main.py <filename.csv>
```

## Export

If the process successfully finished it will generate 2 .xlsx files

- File for data with empty spaces are filled: `output_<filename.csv>.xlsx`
- File for normalized and transposed data `'output_normalized-and-trasnpozed_<filename.csv>.xlsx`
