# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression

# Load the dataset
file_path = 'Student_Performance_and_Engagement.xlsx'  # Update the path if necessary
data = pd.ExcelFile(file_path)

# Load the "Engagement-Binary" sheet
engagement_binary = data.parse('Engagement-Binary')

# Data Preprocessing
# Selecting features and target
features = engagement_binary.drop(columns=['Student ID', 'Engagement Level'])
target = engagement_binary['Engagement Level']

# Encode the target variable (H -> 1, L -> 0)
label_encoder = LabelEncoder()
target_encoded = label_encoder.fit_transform(target)

# Scale the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target_encoded, test_size=0.2, random_state=42)

# Model Training
logistic_model = LogisticRegression(random_state=42)
logistic_model.fit(X_train, y_train)

# Feature Importance Analysis
# Get feature names and corresponding coefficients
feature_names = features.columns
coefficients = logistic_model.coef_[0]

# Pair feature names with coefficients
feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': coefficients
})

# Sort by absolute coefficient value (importance)
feature_importance['Absolute_Coefficient'] = np.abs(feature_importance['Coefficient'])
feature_importance = feature_importance.sort_values(by='Absolute_Coefficient', ascending=False)

# Display feature importance
print("Feature Importance (Logistic Regression Coefficients):")
print(feature_importance[['Feature', 'Coefficient']])
