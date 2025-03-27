async function fetchAIRecommendations(studentId) {
    try {
        const response = await fetch("http://127.0.0.1:5000/api/chatbot", { // Ensure correct backend URL
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ student_id: studentId, query: "recommendations" }),
        });

        const data = await response.json();
        document.getElementById("ai-recommendations").innerText = data.response;
    } catch (error) {
        document.getElementById("ai-recommendations").innerText = "Failed to load recommendations.";
        console.error("Error fetching AI recommendations:", error);
    }
}

// Replace '12345' with the actual student ID dynamically if needed
fetchAIRecommendations("12345");
