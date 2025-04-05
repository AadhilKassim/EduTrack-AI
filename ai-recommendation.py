# Install required packages: pip install flask pandas
from flask import Flask, request, jsonify
import pandas as pd
import requests

app = Flask(__name__)

# Load the refined dataset
df = pd.read_csv("providers/Randomized_ResearchInformation3_.csv")

def get_student(student_id):
    student = df[df["student_id"] == student_id]
    return student.iloc[0] if not student.empty else None

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)