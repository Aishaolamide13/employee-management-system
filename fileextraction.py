import pandas as pd

# Load the dataset
file_path = 'Student_Performance_and_Engagement.xlsx'
data = pd.ExcelFile(file_path)

# Load the "Engagement-Binary" sheet
engagement_binary = data.parse('Engagement-Binary')

# Display the first few rows
print(engagement_binary.head())

# Display basic information about the dataset
print(engagement_binary.info())
