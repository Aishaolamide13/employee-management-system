# Import necessary libraries
import pandas as pd

# Load the dataset
file_path = 'Student_Performance_and_Engagement.xlsx'  # Update the path if necessary
data = pd.ExcelFile(file_path)

# Load the "Engagement-Binary" sheet
engagement_binary = data.parse('Engagement-Binary')

# Define thresholds for low engagement
# Define low engagement thresholds dynamically based on percentiles
low_engagement_thresholds = {
    '# Logins': engagement_binary['# Logins'].quantile(0.2),  # Bottom 20%
    '# Content Reads': engagement_binary['# Content Reads'].quantile(0.2),
    '# Forum Reads': engagement_binary['# Forum Reads'].quantile(0.2),
    '# Forum Posts': engagement_binary['# Forum Posts'].quantile(0.2)
}

print("Updated Low Engagement Thresholds:")
print(low_engagement_thresholds)


# Identify students with low engagement in specific features
# Identify students with low engagement using updated thresholds
low_engagement_students = engagement_binary.loc[
    (engagement_binary['# Logins'] < low_engagement_thresholds['# Logins']) |
    (engagement_binary['# Content Reads'] < low_engagement_thresholds['# Content Reads']) |
    (engagement_binary['# Forum Reads'] < low_engagement_thresholds['# Forum Reads']) |
    (engagement_binary['# Forum Posts'] < low_engagement_thresholds['# Forum Posts'])
].copy()

# Add recommendations
low_engagement_students['Recommendation'] = "Encourage participation via interactive content and peer engagement."

# Display updated low engagement students
print("Recommendations for Low Engagement Students:")
print(low_engagement_students[['Student ID', 'Recommendation']])
