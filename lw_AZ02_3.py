import pandas as pd
import numpy as np

dates = pd.date_range(start='2022-07-26', periods=10, freq='D')

values = np.random.rand(10)

df = pd.DataFrame({'Data': dates, 'Value': values})
df.set_index('Data', inplace=True)

print(df)

month = df.resample('ME').mean()

print(f'\nСреднее значение по месяцам:\n{month}')


