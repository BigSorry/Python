import pandas as pd
import numpy as np
from datetime import datetime, timedelta

path = "C:/Users/lexme/PycharmProjects/tutorial/tutorial/crawl.csv"
data = pd.read_csv(path)
data["Rank"] = 0
data["Rank_Change"] = 0
data["Market_Cap_Change"] = 0
data["Market_Cap_Change"] = data["Market_Cap_Change"].astype("int64")
print(data.columns)
data = data.drop(data[data["Market_Cap"] == "-"].index)
data.Date = data.Date.apply(lambda x: datetime.strptime(x, "%b %d, %Y"))
data["Market_Cap"] = data["Market_Cap"].apply(lambda x: x.replace(",", ""))
#data["Market_Cap"] = data["Market_Cap"].apply(lambda x: x.replace("-", "0"))
data["Market_Cap"] = data["Market_Cap"].astype("int64")
data = data.sort_values(["Name", "Date"])

dates = data.Date.unique()
# give rankings based on Market Cap
for date in dates:
    query = data.where(data.Date == date)
    data.loc[data["Market_Cap"] == query["Market_Cap"],"Rank"] = query["Market_Cap"].rank(ascending = False)

names = data.Name.unique()
# percentage growth Market Cap compared with one day before and same for rank
for name in names:
    data.loc[data.Name == name, "Market_Cap_Change"] = ((data.loc[data.Name == name, "Market_Cap"] - data.loc[data.Name == name, "Market_Cap"].shift(1)) / data.loc[data.Name == name, "Market_Cap"].shift(1)) * 100
    data.loc[data.Name == name, "Rank_Change"] =  data.loc[data.Name == name, "Rank"].shift(1) - data.loc[data.Name == name, "Rank"]

outputCol = ["Name", "Date", "Market_Cap", "Market_Cap_Change", "Rank", "Rank_Change"]
output = data[outputCol]
print(output.head())
output.to_csv("CryptoData.csv", index = False)
