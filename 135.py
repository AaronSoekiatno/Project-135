import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("C:/Users/aaron/Downloads/final-data-C130-main/final-data-C130-main/output.csv")
nameList = df["Name"].tolist()
radiusList = df["Radius"].tolist()
massList = df["Mass"].tolist()
distList = df["Distance"].tolist()

plt.bar(nameList,massList,color = "green")
plt.bar(nameList,radiusList,color = "red")
plt.bar(nameList,distList,color = "blue")
plt.show()