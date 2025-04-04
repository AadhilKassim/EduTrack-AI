import requests
import json

def test_recommendation():
    url = "http://localhost:5000/recommend"
    
    # Example student data
    student_data = {
        'Department': 'Computer Science and Engineering',
        'Gender': 'Male',
        'Income': 'High (Above 50,000)',
        'Hometown': 'City',
        'Gaming': 'Yes',
        'Attendance': '80%-100%',
        'Job': 'No',
        'English': 4.0,
        'Overall': 3.75
    }

    # Send POST request
    response = requests.post(url, json=student_data)
    
    # Print results
    print("\nRecommendation Results:")
    print("-" * 50)
    if response.status_code == 200:
        data = response.json()
        recommendations = data['recommendations']
        print("Recommended courses:")
        for rec in recommendations:
            print(f"- {rec['course']}: {rec['confidence']*100:.1f}% match")
    else:
        print("Error:", response.json()['message'])

if __name__ == "__main__":
    test_recommendation()
