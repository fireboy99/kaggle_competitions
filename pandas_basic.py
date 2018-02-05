import pandas as pd
file_handle = pd.read_csv("Titanic:ML_from_a_disaster/train.csv")
print(file_handle.describe())
print(file_handle.columns[file_handle.isnull().any()])
pass_data = file_handle.PassengerId
print(pass_data.head())
pass_data_copy = pass_data
pass_data_copy = 0
print(pass_data_copy.head())

