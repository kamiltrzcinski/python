import csv
import pandas as pd


cerealFile = open('cereal.csv')
cerealReader = csv.reader(cerealFile)
cerealList = list(cerealReader)

df = pd.read_csv('cereal.csv')
for row in cerealList:
    print(row[0])

#print(df.info())
print(df['calories'].dtypes)

