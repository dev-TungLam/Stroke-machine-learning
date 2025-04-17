# %%
# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# For handling imbalanced data with SMOTE
from imblearn.over_sampling import SMOTE

# Load dataset (adjust the path if needed)
df = pd.read_csv('/home/tunglam/Downloads/healthcare-dataset-stroke-data.csv')

# Preview the first few rows
print("Data preview:")
print(df.head())

# ---------- Data Preprocessing ----------

# Impute missing values for 'bmi' using the median
imputer = SimpleImputer(strategy='median')
df['bmi'] = imputer.fit_transform(df[['bmi']])

# Convert categorical features to dummy variables
# Categorical columns: 'gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'
df = pd.get_dummies(df, columns=['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'], drop_first=True)

# Drop the 'id' column
if 'id' in df.columns:
    df.drop('id', axis=1, inplace=True)

# Define features (X) and target (y)
X = df.drop('stroke', axis=1)
y = df['stroke']

# ---------- Splitting and Scaling ----------

# Split data into training and test sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------- Handling Class Imbalance with SMOTE ----------

# SMOTE oversampling on the training data
smote = SMOTE(random_state=42)
X_train_res, y_train_res = smote.fit_resample(X_train_scaled, y_train)
print("After SMOTE, counts of label '1':", sum(y_train_res == 1))
print("After SMOTE, counts of label '0':", sum(y_train_res == 0))

# ---------- Logistic Regression Modeling with SMOTE ----------

# Create an instance of LogisticRegression and train on resampled data
logreg_smote = LogisticRegression(max_iter=1000, random_state=42)
logreg_smote.fit(X_train_res, y_train_res)

# Predict on the test set
y_pred_smote = logreg_smote.predict(X_test_scaled)

# ---------- Evaluation ----------

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred_smote)
print("\n--- Logistic Regression with SMOTE Oversampling ---")
print("Accuracy:", round(accuracy * 100, 2), "%")

# Display Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred_smote))

# Display Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred_smote))

# %%
