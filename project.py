import pandas as pd
import statistics

df = pd.read_csv("data.csv")
data = df["Weight(Pounds)"].tolist()
sum=0
for h in data:
    sum+=h
number=len(data)
mean=sum/number
print(mean)


#shotcut mode
a=statistics.mean(data)
print(a)
