from socket import sethostname
import numpy as np
import pandas as pd
data=pd.read_csv('iris.csv',header=0)
print(data.shape)
print(data[10:21])
p=data[["sepal.length","variety"]]
print(p.head(10))
c=data.loc[data["variety"]=="Setosa"]
print(c)