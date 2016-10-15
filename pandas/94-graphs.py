

import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv("titanic_after.csv")

print(df.head())
df['Fare'].plot()
plt.show()