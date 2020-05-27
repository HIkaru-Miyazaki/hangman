import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/rucchi/Desktop/kyoto_5years.csv")

#print(df.drop(3))

#print(df.head())

for i in range(5):
	df=df.drop(i)

#print(df.columns[1])
#print(df.head())

df=df[1].astype(float)

#df=df.astype(float)

df.plot()

plt.show()