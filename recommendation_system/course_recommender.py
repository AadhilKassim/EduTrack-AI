import pandas as pd
import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

__all__ = ['CourseRecommender']  # Explicitly define what to export

class CourseRecommender:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.label_encoders = {}
        self.features = ['Department', 'Gender', 'Income', 'Hometown', 'Gaming', 'Attendance', 
                        'Job', 'English', 'Overall']
        
    def preprocess_data(self, df):
        # Create copies of encoders for each categorical column
        for column in ['Department', 'Gender', 'Income', 'Hometown', 'Gaming', 'Attendance', 'Job']:
            self.label_encoders[column] = LabelEncoder()
            df[column] = self.label_encoders[column].fit_transform(df[column])
        return df
    
    def train(self, data_path):
        # Verify file exists
        if not os.path.exists(data_path):
            raise FileNotFoundError(f"Dataset not found at: {data_path}")
            
        # Read and preprocess the data
        try:
            df = pd.read_csv(data_path)
        except Exception as e:
            raise Exception(f"Error reading dataset: {str(e)}")
            
        df = self.preprocess_data(df)
        
        # Define elective courses based on departments
        elective_courses = {
            'Technical': ['Advanced Programming', 'Data Science', 'AI & ML', 'Cybersecurity'],
            'Business': ['Digital Marketing', 'Entrepreneurship', 'Finance', 'Business Analytics'],
            'Communication': ['Technical Writing', 'Public Speaking', 'Digital Media', 'Content Creation'],
            'Liberal Arts': ['Psychology', 'Philosophy', 'World History', 'Literature']
        }
        
        # Create synthetic training data based on student profiles
        X = df[self.features]
        
        # Assign synthetic labels based on student characteristics
        y = []
        for _, row in X.iterrows():
            if row['Department'] in [0, 2]:  # CSE and EEE
                y.append('Technical')
            elif row['Department'] in [1]:    # Business Administration
                y.append('Business')
            elif row['English'] >= 4 and row['Overall'] >= 3.5:
                y.append('Communication')
            else:
                y.append('Liberal Arts')
        
        # Train the model
        self.model.fit(X, y)
        
    def recommend_courses(self, student_data):
        # Preprocess student data
        student_features = []
        for feature in self.features:
            if feature in self.label_encoders:
                encoded_value = self.label_encoders[feature].transform([student_data[feature]])[0]
                student_features.append(encoded_value)
            else:
                student_features.append(float(student_data[feature]))
        
        # Get prediction
        category = self.model.predict([student_features])[0]
        
        # Define course recommendations based on category
        recommendations = {
            'Technical': [
                ('Advanced Programming', 0.9),
                ('Data Science', 0.85),
                ('AI & ML', 0.8),
                ('Cybersecurity', 0.75)
            ],
            'Business': [
                ('Digital Marketing', 0.9),
                ('Entrepreneurship', 0.85),
                ('Finance', 0.8),
                ('Business Analytics', 0.75)
            ],
            'Communication': [
                ('Technical Writing', 0.9),
                ('Public Speaking', 0.85),
                ('Digital Media', 0.8),
                ('Content Creation', 0.75)
            ],
            'Liberal Arts': [
                ('Psychology', 0.9),
                ('Philosophy', 0.85),
                ('World History', 0.8),
                ('Literature', 0.75)
            ]
        }
        
        return recommendations[category]

# Remove the example usage from the module level
if __name__ == "__main__":
    print("Course Recommender module loaded successfully")
