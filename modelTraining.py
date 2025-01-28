# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

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

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(features_scaled, target_encoded, test_size=0.2, random_state=42)

# Model Training and Evaluation
# Initialize the Logistic Regression model
logistic_model = LogisticRegression(random_state=42)

# Train the model
logistic_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = logistic_model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

# Print the results
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", report)
