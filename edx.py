import pandas as pd

file_path = 'UpdatedResumeDataSet.csv'
data = pd.read_csv(file_path)

data.head(), data.info(), data.describe(include='all')
