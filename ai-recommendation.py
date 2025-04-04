# Install required packages: pip install flask pandas
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the refined dataset
df = pd.read_csv("providers/Randomized_ResearchInformation3.csv")

def get_student(student_id):
    student = df[df["student_id"] == student_id]
    return student.iloc[0] if not student.empty else None

@app.route("/api/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    student_id = data.get("student_id")
    query = data.get("query", "").lower()
    student = get_student(student_id)
    
    if student is None:
        return jsonify({"response": "Student not found."})
    
    if "weakness" in query:
        subject_scores = student.iloc[2:].to_dict()
        weakest_subject = min(subject_scores, key=subject_scores.get)
        response = f"Your weakest subject is {weakest_subject} with a score of {subject_scores[weakest_subject]}."
    elif "improve" in query:
        response = (f"To improve, increase your study time (current: {student['studytime']} hrs/week) "
                    f"and reduce absences (current: {student['absences']}).")
    else:
        response = "I'm analyzing your data... Check your dashboard for more insights."
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)