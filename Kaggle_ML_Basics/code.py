import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 

main_file_path = 'train.csv'
test_file_path = 'test.csv'
data = pd.read_csv(main_file_path)
test_data = pd.read_csv(test_file_path)
#print(data.describe())
print(data.columns)
count =0
for col in data.columns:
    count += 1
print("Count is",count)


#Printing sale price column
sale_price_data = data.SalePrice
print(sale_price_data.head())


#Printing two columns 
sale_price_lot_area = ['SalePrice', 'LotArea']
sp_la_data = data[sale_price_lot_area]
print(sp_la_data.describe())


#Fit and prediction
y = data.SalePrice

predictors = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath',
    'BedroomAbvGr', 'TotRmsAbvGrd']

X = data[predictors]

iowa_model = DecisionTreeRegressor()
iowa_model.fit(X,y)

print("Making predictions for following few houses", X.head())
print("Prediction is: ", iowa_model.predict(X.head()))


#Splitting the data
train_X, val_X, train_Y, val_Y = train_test_split(X,y, random_state = 0)

#Training the new model
new_model = DecisionTreeRegressor()
new_model.fit(train_X, train_Y)

#Computing the Mean Absolute Error
print("MAE is",mean_absolute_error(val_Y, new_model.predict(val_X)))

def get_mae(max_leaf_nodes, train_X,  train_Y, val_X, val_Y):
    new_model2 = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state = 0)
    new_model2.fit(train_X, train_Y)
    mae = mean_absolute_error(val_Y, new_model2.predict(val_X))
    return mae

for val in range(30,40,2):            
    print("For", val, "MAE is", get_mae(val, train_X , train_Y,val_X, val_Y))


ran_forest_model = RandomForestRegressor()
ran_forest_model.fit(train_X, train_Y)
print("forest MAE is",mean_absolute_error(val_Y, ran_forest_model.predict(val_X)))


#Final predictions 
ran_forest_model = RandomForestRegressor()
ran_forest_model.fit(X, y)

test_X = test_data[predictors]
test_y = ran_forest_model.predict(test_X)


sub_csv = pd.DataFrame({'Id': test_data.Id, 'SalePrice':test_y})
sub_csv.to_csv('final_submission.csv', index=False)
