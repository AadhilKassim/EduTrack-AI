async function fetchAIRecommendations(studentId) {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/chatbot", { // Ensure correct backend URL
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ student_id: studentId, query: "recommendations" }),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById("ai-recommendations").innerText = data.response;
    } catch (error) {
        document.getElementById("ai-recommendations").innerText = "Failed to load recommendations.";
        console.error("Error fetching AI recommendations:", error);
    }
}

// Dynamically fetch recommendations for the logged-in student
const studentId = "1"; // Replace with a valid student_id from the dataset (e.g., "1")
fetchAIRecommendations(studentId);

async function fetchStudentData(studentId) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/api/student?student_id=${studentId}`);
        const data = await response.json();

        if (data.error) {
            document.getElementById("student-data").innerText = "Student not found.";
        } else {
            document.getElementById("student-data").innerText = JSON.stringify(data, null, 2);
        }
    } catch (error) {
        document.getElementById("student-data").innerText = "Failed to load student data.";
        console.error("Error fetching student data:", error);
    }
}

// Fetch and display student data for the logged-in student
fetchStudentData(studentId);
