import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# save filepath to variable for easier access
path = 'C:/Users/lexme/OneDrive/Documenten/train.csv'
data = pd.read_csv(path)
#print(data.columns)
def get_mae(max_leaf_nodes, predictors_train, predictors_val, targ_train, targ_val):
    model = RandomForestRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(predictors_train, targ_train)
    preds_val = model.predict(predictors_val)
    mae = mean_absolute_error(targ_val, preds_val)
    return(mae)

predictors = ['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd']
# X are the variables we use to predict y
X = data[predictors]
# we try to estimate y
y = data.SalePrice

train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

for max_leaf_nodes in range(30, 100):
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

forestModel = RandomForestRegressor()
forestModel.fit(train_X, train_y)
predictions = forestModel.predict(val_X)
error = mean_absolute_error(val_y, predictions)
print(error)