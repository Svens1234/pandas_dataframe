import numpy as np
import pandas as pd

my_df = pd.DataFrame(np.random.randn(4,5), [1,2,3,4], ['red', 'orange', 'yellow', 'green', 'blue'])
print(my_df)
print(my_df['orange'])
print(my_df['red'])
print(type(my_df['red']))
print(type(my_df))
print(my_df[['yellow', 'blue']])
print(type(my_df[['yellow', 'blue']]))
my_df['indigo'] = my_df['blue']
print(my_df)
my_df['violet'] = my_df['blue'] + my_df['indigo']
print(my_df)
print(my_df.loc[2])
print(my_df.iloc[1])
my_df.iloc[2] = my_df.iloc[1]
print(my_df.iloc[2])
print(my_df.loc[2, 'orange'])
print(my_df.loc[[1,3], ['blue', 'violet']])
print(my_df.drop(3))
print(my_df)
print(my_df.drop(3, inplace=True))
print(my_df)
print(my_df.drop('indigo', axis=1))
print(my_df)
my_df.drop('indigo', axis=1, inplace=True)
print(my_df)
print(my_df.shape) #показывает сколько строк, сколько столбцов
