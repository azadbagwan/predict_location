import pandas as pd
df1 = pd.read_csv('og.csv')
df2 = pd.read_csv('df_1.csv')
result = pd.concat([df1, df2], ignore_index=True)
result.to_csv('og2000.csv', index=False)