def analysis():
    import os
    import pandas as pd
    import numpy as np
    from datetime import datetime, timedelta
    from sqlalchemy import create_engine
    import MySQLdb as mySQL

    path = "C:/Users/lexme/PycharmProjects/CryptoUpdate/tutorial/crawlUpdate.csv"
    fileEmpty = os.stat(path).st_size == 0
    if fileEmpty:
        return
    else:
        data = pd.read_csv(path)
        # data["Rank"] = 0
        # data["Rank_Change"] = 0
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
        # for date in dates:
        #     query = data.where(data.Date == date)
        #     data.loc[data["Market_Cap"] == query["Market_Cap"],"Rank"] = query["Market_Cap"].rank(ascending = False)

        names = data.Name.unique()
        # percentage growth Market Cap compared with one day before and same for rank
        for name in names:
            data.loc[data.Name == name, "Market_Cap_Change"] = ((data.loc[data.Name == name, "Market_Cap"] - data.loc[data.Name == name, "Market_Cap"].shift(1)) / data.loc[data.Name == name, "Market_Cap"].shift(1)) * 100
            #data.loc[data.Name == name, "Rank_Change"] =  data.loc[data.Name == name, "Rank"].shift(1) - data.loc[data.Name == name, "Rank"]

        lowestDate = dates[0]
        data = data.drop(data[data["Date"] == lowestDate].index)
        db = mySQL.connect(host="localhost",
                           user="root",
                           passwd="",
                           db="cryptocurrency")
        cursor = db.cursor(mySQL.cursors.DictCursor)
        # Check if we dont have new names
        cursor.execute("SELECT Name FROM coinname ORDER BY Name")
        dbNames = [item["Name"] for item in cursor.fetchall()]
        for name in names:
            if name in dbNames:
                continue
            else:
                print(name)
                query = "INSERT INTO coinname(Name, Name_Id) VALUES ('{}', null)".format(name)
                cursor.execute(query)
        db.commit()

        cursor.execute("SELECT * FROM coinname ORDER BY Name_Id")
        dbNamesAndId = cursor.fetchall()
        nameIdLookUp = {}
        for item in dbNamesAndId:
            nameIdLookUp[item["Name"]] = item["Name_Id"]
        db.close()
        def nameToId(name):
            if nameIdLookUp[name]:
                return  nameIdLookUp[name]
            else:
                return name
        data.Name = data.Name.apply(lambda x: nameToId(x))

        financeTable = ["Name", "Date", "Market_Cap", "Market_Cap_Change"]
        outputFinance = data[financeTable]
        outputFinance["Finance_Id"] = None
        outputFinance = outputFinance.rename(columns={'Name': 'Name_Id'})
        print(outputFinance.head())
        #outputFinance.to_csv("C:/Users/lexme/PycharmProjects/CryptoUpdate/tutorial/CryptoData.csv", index = False)
        engine = create_engine('mysql+mysqldb://root:@localhost/cryptocurrency')
        outputFinance.to_sql(con=engine, name='coinfinance', if_exists='append',  index = False)


