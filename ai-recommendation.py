# Install required packages: pip install flask pandas flask-cors
from flask import Flask, request, jsonify
import pandas as pd
import os  # Added for file existence check
from flask_cors import CORS  # Add this import

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the refined dataset
dataset_path = "providers/prototype_student_data_v3.csv"
if not os.path.exists(dataset_path):
    raise FileNotFoundError(f"Dataset not found at {dataset_path}. Please check the file path.")
df = pd.read_csv(dataset_path)

def get_student(student_id):
    student_id = str(student_id)  # Ensure student_id is treated as a string
    student = df[df["student_id"].astype(str) == student_id]  # Convert dataset column to string
    if student.empty:
        return None
    return student.iloc[0]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the AI Recommendation API. Use the /api/chatbot endpoint to interact."})

@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    student_id = data.get("student_id")
    query = data.get("query", "").lower()
    student = get_student(student_id)
    
    if student is None:
        return jsonify({"response": "Student not found."})
    
    try:
        if "weakness" in query:
            subject_scores = {
                "Mathematics_I": student["Mathematics_I"],
                "Physics_I": student["Physics_I"],
                "Chemistry": student["Chemistry"],
                "Programming_Fundamentals": student["Programming_Fundamentals"],
                "English": student["English"],
                "Mathematics_II": student["Mathematics_II"],
                "Physics_II": student["Physics_II"],
                "Data_Structures": student["Data_Structures"],
                "Digital_Logic": student["Digital_Logic"]
            }
            weakest_subject = min(subject_scores, key=subject_scores.get)
            response = f"Your weakest subject is {weakest_subject} with a score of {subject_scores[weakest_subject]}."
        elif "improve" in query:
            response = (f"To improve, increase your study time (current: {student['studytime']} hrs/week) "
                        f"and reduce absences (current: {student['absences']}).")
        elif "recommendations" in query:
            response = ("Based on your data, focus on improving your weakest subjects, "
                        "maintaining consistent attendance, and allocating more time to study.")
        else:
            response = "I'm analyzing your data... Check your dashboard for more insights."
    except KeyError as e:
        response = f"Error processing data: Missing column {e} in the dataset."

    return jsonify({"response": response})

@app.route("/api/student", methods=["GET"])
def get_student_data():
    student_id = request.args.get("student_id")
    student = get_student(student_id)
    
    if student is None:
        return jsonify({"error": "Student not found."}), 404
    
    return jsonify({
        "student_id": student["student_id"],
        "studytime": student["studytime"],
        "absences": student["absences"],
        "Mathematics_I": student["Mathematics_I"],
        "Physics_I": student["Physics_I"],
        "Chemistry": student["Chemistry"],
        "Programming_Fundamentals": student["Programming_Fundamentals"],
        "English": student["English"],
        "Mathematics_II": student["Mathematics_II"],
        "Physics_II": student["Physics_II"],
        "Data_Structures": student["Data_Structures"],
        "Digital_Logic": student["Digital_Logic"]
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)  # Debug mode should be disabled in production