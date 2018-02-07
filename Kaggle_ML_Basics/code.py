import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 
from sklearn.preprocessing import Imputer 
from xgboost import XGBRegressor

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


predictors = ['PoolArea','GrLivArea','YrSold','KitchenAbvGr','MiscVal',
        'OverallCond', 'OverallQual','LotArea', 'YearBuilt', '1stFlrSF',
        '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = data[predictors]
print X

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

#Predictions with an imputer
#Trial cols_with_missing = data.columns[data.isnull().any()]  
#Trial print (cols_with_missing)
my_imputer = Imputer()
imputed_train_X = my_imputer.fit_transform(train_X)
imputed_val_X = my_imputer.fit_transform(val_X)
impute_forest_model = RandomForestRegressor()
impute_forest_model.fit(imputed_train_X, train_Y)
print("Impute forest MAE is",mean_absolute_error(val_Y, impute_forest_model.predict(imputed_val_X)))


#Imputation with new columns
new_train_X = train_X.copy()
cols_with_missing = new_train_X.columns[new_train_X.isnull().any()]  
new_val_X = val_X.copy()
cols_with_missing = new_val_X.columns[new_val_X.isnull().any()]  

for col in cols_with_missing:
    new_train_X[col + "is_missing"] = new_train_X[col].isnull()
    new_val_X[col + "is_missing"] = new_val_X[col].isnull()

my_imputer = Imputer()
imputed_train_X = my_imputer.fit_transform(new_train_X)
imputed_val_X = my_imputer.fit_transform(new_val_X)
new_impute_forest_model = RandomForestRegressor()
new_impute_forest_model.fit(imputed_train_X, train_Y)
print("Modified Impute forest MAE is",mean_absolute_error(val_Y, new_impute_forest_model.predict(imputed_val_X)))

#Final predictions 
predictors = ['PoolArea','GrLivArea','YrSold','KitchenAbvGr','MiscVal',
        'OverallCond', 'OverallQual','LotArea', 'YearBuilt', '1stFlrSF',
        '2ndFlrSF', 'FullBath', 'BedroomAbvGr',
        'TotRmsAbvGrd','MSZoning','Street', 'Alley', 'LotShape', 'LandContour',
         'LandSlope' , 'Neighborhood', 'Condition1', 'BldgType']#,'GarageArea']
#data.reset_index()
#df = data['GarageArea']

#with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
#    print("Sachin ", df)
# np.nan_to_num(df)
#with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
#    print("Sachin 2", df)
#ran_forest_model = RandomForestRegressor()
##Train data
#X = data[predictors]
#new_X = X.copy()
#new_X = pd.get_dummies(new_X)
#cols_with_missing = new_X.columns[X.isnull().any()]  
#
#test_X = test_data[predictors]
#new_test_X = test_X.copy()
#new_test_X = pd.get_dummies(new_test_X)
#cols_with_missing = new_test_X.columns[new_test_X.isnull().any()]  
#
#for col in cols_with_missing:
#    new_X[col + "is_missing"] = new_X[col].isnull()
#     new_test_X[col + "is_missing"] = new_test_X[col].isnull()
#
#new_X, new_test_X = new_X.align(new_test_X, join='left', axis=1)
#
#my_imputer = Imputer()
#imputed_train_X = my_imputer.fit_transform(new_X)
#imputed_test_X = my_imputer.fit_transform(new_test_X)
#
#ran_forest_model.fit(new_X, y)
#test_y = ran_forest_model.predict(new_test_X)
#
#sub_csv = pd.DataFrame({'Id': test_data.Id, 'SalePrice':test_y})
#sub_csv.to_csv('final_submission.csv', index=False)

# XGboost gradient boosted trees final predictions
#XG data.dropna(axis=0, subset=['SalePrice'], inplace=True)
#XG y = data.SalePrice
#XG X_train = data.drop(['SalePrice'], axis=1).select_dtypes(exclude=['object']) 
#XG X_test = test_data.select_dtypes(exclude=['object']) 
#XG print("Sachin", X_train.describe)
#XG print(X_test.columns)
##Train data
X = data[predictors]
new_X = X.copy()
new_X = pd.get_dummies(new_X)
cols_with_missing = new_X.columns[X.isnull().any()]  

test_X = test_data[predictors]
new_test_X = test_X.copy()
new_test_X = pd.get_dummies(new_test_X)
cols_with_missing = new_test_X.columns[new_test_X.isnull().any()]  

for col in cols_with_missing:
    new_X[col + "is_missing"] = new_X[col].isnull()
    new_test_X[col + "is_missing"] = new_test_X[col].isnull()

new_t_X, new_te_X = new_X.align(new_test_X, join='left', axis=1)

my_imputer = Imputer()
X_train = my_imputer.fit_transform(new_t_X)
X_test = my_imputer.fit_transform(new_te_X)

my_model = XGBRegressor(n_estimators = 3000, learning_rate = 0.06)
my_model.fit(X_train, y, verbose= False)
test_y = my_model.predict(X_test)
#print("Sachin", test_data.Id)
#print("Sachin 2", test_y.size)
sub_csv = pd.DataFrame({'Id': test_data.Id, 'SalePrice':test_y})
sub_csv.to_csv('final_submission.csv', index=False)

