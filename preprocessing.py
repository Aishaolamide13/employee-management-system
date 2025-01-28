import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Load the dataset
file_path = 'Student_Performance_and_Engagement.xlsx'
data = pd.ExcelFile(file_path)

# Load the "Engagement-Binary" sheet
engagement_binary = data.parse('Engagement-Binary')

# Selecting features and target
features = engagement_binary.drop(columns=['Student ID', 'Engagement Level'])
target = engagement_binary['Engagement Level']

# Encode the target variable (H -> 1, L -> 0)
label_encoder = LabelEncoder()
target_encoded = label_encoder.fit_transform(target)

# Scale the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target_encoded, test_size=0.2, random_state=42)

# Print dataset shapes
print(f"Training features shape: {X_train.shape}")
print(f"Testing features shape: {X_test.shape}")
print(f"Training target shape: {y_train.shape}")
print(f"Testing target shape: {y_test.shape}")
