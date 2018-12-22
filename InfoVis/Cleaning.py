import pandas as pd
import numpy as np
import re
print("Running..")

path = "C:/Users/lexme/Desktop/Q1/DataVis/InfoVis/WorldMap/resources/c5fe9392-8421-43cc-b646-6b2d7879c3d8_Data.csv"
path2 = "C:/Users/lexme/Desktop/Q1/DataVis/InfoVis/WorldMap/resources/unhcr_popstats_export_persons_of_concern_all_data.csv"
path3 =  "C:/Users/lexme/Desktop/Q1/DataVis/InfoVis/WorldMap/resources/unhcr_popstats_export_persons_of_concern_2018_12_02_205924.csv"

def selectYear(columns, row):
    year = row['Year']
    select = ""
    for i in columns:
        if i == year:
            select = i
    row["GDP"] = row["select"]


gdp = pd.read_csv(path)
gdp = gdp.replace(r'[.]{2,}', np.nan, regex=True)
#gdp = gdp.fillna('0')
gdp.rename(columns={gdp.columns[0] : 'Country'}, inplace = True)
for i in gdp.columns:
    if re.match("[0-9]{4}", i):
        var = i[:4]
        gdp.rename(columns={i: var}, inplace=True)
    print(type(i))
    print(i)

gdp['GDP'] = ""

migration = pd.read_csv(path3,sep= ',(?!\s)', engine = 'python')
migration = migration.replace(r'\*', np.nan, regex=True)
#migration = migration.fillna(0)
migration.rename(columns={migration.columns[1]  : 'Country', migration.columns[3] : 'Refugees'}, inplace = True)

#migrationNew = migration.drop_duplicates(subset= {"Country", "Indicator"}, keep = False)
migrationNew = pd.pivot_table(migration, index=["Country", "Origin"], values=["Refugees"], columns=["Year"], aggfunc=np.sum).reset_index()
migrationNew["Origin"] =  migrationNew.iloc[:,2] + "_" + migrationNew["Origin"]
migrationNew.rename(columns={"Origin" : "Indicator"}, inplace = True)
migrationNew = migrationNew.drop(columns=['level_2'])
migrationNew.to_csv('migrationNew.csv', sep = "," , index = False)
test = migrationNew.append(gdp)
print(0)