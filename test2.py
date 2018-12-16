# matplotlib inline
#import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("PastHires.csv")

degree_counts = df['Level of Education'].value_counts()
print(degree_counts.plot(kind='bar'))
