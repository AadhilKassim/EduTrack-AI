import pandas as pd
import numpy as np

def preprocess_dataset(input_file_path, output_file_path):
    # Read the dataset
    df = pd.read_csv(input_file_path)
    
    # Generate student IDs
    num_students = len(df)
    student_ids = [f'STU{str(i).zfill(6)}' for i in range(1, num_students + 1)]
    
    # Add student IDs as the first column
    df.insert(0, 'student_id', student_ids)
    
    # Convert binary columns to proper binary format
    binary_columns = df.select_dtypes(include=['object']).columns
    for col in binary_columns:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
    
    # Save the preprocessed dataset
    df.to_csv(output_file_path, index=False)
    
    return df

def create_recommendation_matrix(df):
    # Create a sparse matrix for recommendation system
    student_item_matrix = df.set_index('student_id')
    
    # Convert to binary sparse matrix if needed
    sparse_matrix = student_item_matrix.sparse.to_coo()
    
    return sparse_matrix

if __name__ == "__main__":
    input_file = "path/to/your/input/dataset.csv"
    output_file = "path/to/your/processed/dataset.csv"
    
    processed_df = preprocess_dataset(input_file, output_file)
    recommendation_matrix = create_recommendation_matrix(processed_df)
    print("Dataset preprocessing completed successfully!")
