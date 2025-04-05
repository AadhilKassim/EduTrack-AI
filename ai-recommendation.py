# Install required packages: pip install flask pandas flask-cors
from flask import Flask, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the refined dataset
df = pd.read_csv("providers/Randomized_ResearchInformation3_.csv")

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
    student = get_student(student_id)
    
    if student is None:
        return jsonify({"response": "Student not found."})

    # Format student data for recommendation
    student_data = {
        'Department': student['Department'],
        'Gender': student['Gender'],
        'Income': student['Income'],
        'Hometown': student['Hometown'],
        'Gaming': student['Gaming'],
        'Attendance': student['Attendance'],
        'Job': student['Job'],
        'English': float(student['English']),
        'Overall': float(student['Overall'])
    }

    try:
        response = requests.post("http://127.0.0.1:5000/recommend", json=student_data)
        if response.status_code == 200:
            return jsonify({"response": response.json()})
        else:
            return jsonify({"response": "Error getting recommendations"})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

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