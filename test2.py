# matplotlib inline
#import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")

print("columns name of DataFrame:",df.columns)

print("single column show from DataFrame:\n",df['Hired'])

print("range of rows:\n",df['Hired'][:5])

print("specified column / row:\n",df['Hired'][5])

print("more then one column:\n",df[["Years Experience","Hired"]])

print("specific renges of row:\n",df[['Years Experience','Hired']][:5])

print("DataFrame by a specific:\n",df.sort_values(['Years Experience']))

degree_counts = df['Level of Education'].value_counts()
print("break down the number of unique values in a given column:\n",degree_counts)
