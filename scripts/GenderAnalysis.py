import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('data/Mall_Customers.csv')
df.head()
plt.figure(1 , figsize = (15 , 6)) 
n = 0 
plt.figure(1 , figsize = (15 , 5))
sns.countplot(y = 'Gender' , data = df)
plt.show()