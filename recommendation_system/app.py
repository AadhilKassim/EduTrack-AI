from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from pathlib import Path

# Setup proper paths
current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.append(str(current_dir))

from course_recommender import CourseRecommender

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize recommender
try:
    recommender = CourseRecommender()
    data_path = project_root / "providers" / "Randomized_ResearchInformation3_.csv"
    
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset not found at: {data_path}")
        
    recommender.train(str(data_path))
    print(f"Recommender system initialized successfully!")
    print(f"Using dataset: {data_path}")
    
except Exception as e:
    print(f"Error initializing recommender: {str(e)}")
    sys.exit(1)

@app.route('/')
def home():
    return "Course Recommendation System is running!"

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    student_data = request.json
    try:
        recommendations = recommender.recommend_courses(student_data)
        return jsonify({
            'status': 'success',
            'recommendations': [
                {
                    'course': course,
                    'confidence': conf,
                    'description': get_course_description(course)
                }
                for course, conf in recommendations
            ]
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

def get_course_description(course):
    descriptions = {
        'Advanced Programming': 'Learn advanced software development concepts and patterns.',
        'Data Science': 'Master data analysis, visualization, and machine learning.',
        'AI & ML': 'Explore artificial intelligence and machine learning algorithms.',
        'Cybersecurity': 'Study network security and ethical hacking.',
        'Digital Marketing': 'Learn modern marketing strategies and tools.',
        'Entrepreneurship': 'Develop business planning and startup skills.',
        'Finance': 'Study financial management and investment strategies.',
        'Business Analytics': 'Master business data analysis and decision making.',
        'Technical Writing': 'Develop professional documentation skills.',
        'Public Speaking': 'Master presentation and communication skills.',
        'Digital Media': 'Learn multimedia content creation and management.',
        'Content Creation': 'Study content strategy and development.',
        'Psychology': 'Understand human behavior and mental processes.',
        'Philosophy': 'Explore critical thinking and ethical reasoning.',
        'World History': 'Study global historical events and their impact.',
        'Literature': 'Analyze classical and contemporary writings.'
    }
    return descriptions.get(course, 'Course description not available.')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
