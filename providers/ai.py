import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample dataset
df = pd.read_csv("providers/prototype_student_data_v3.csv")  # Contains student data

# Select features and target
X = df[["studytime", "absences", "Mathematics_I", "Physics_I", "Chemistry", 
        "Programming_Fundamentals", "English", "Physics_II", "Data_Structures", "Digital_Logic"]]
y = df["Mathematics_II"]  # Target column

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "student_performance_model.pkl")
