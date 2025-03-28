from joblib import load

def load_model(model_path):
    """Load the pre-trained model from a .pkl file."""
    return load(model_path)

def predict_marks(model, input_features):
    """Predict marks using the loaded model and input features."""
    return model.predict([input_features])[0]

def main():
    model_path = "student_performance_model.pkl"
    model = load_model(model_path)
    
    print("Enter the input features for prediction:")
    # Example: Replace these with actual feature names and types
    feature1 = float(input("Feature 1: "))
    feature2 = float(input("Feature 2: "))
    feature3 = float(input("Feature 3: "))
    
    input_features = [feature1, feature2, feature3]
    predicted_marks = predict_marks(model, input_features)
    
    print(f"Predicted Marks: {predicted_marks}")

if __name__ == "__main__":
    main()
