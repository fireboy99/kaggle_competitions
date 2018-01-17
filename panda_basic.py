import pandas as pd
file_handle = pd.read_csv("Titanic:ML_from_a_disaster/train.csv")
print(file_handle.describe())
print(file_handle.columns[file_handle.isnull().any()])
pass_data = file_handle.PassengerId
print(pass_data)
