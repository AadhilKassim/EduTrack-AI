async function fetchAIRecommendations() {
    try {
        const studentId = localStorage.getItem('studentId');
        if (!studentId) {
            document.getElementById("ai-recommendations").innerHTML = 
                '<div class="text-red-500">Please login first to see recommendations.</div>';
            return;
        }

        const response = await fetch("http://127.0.0.1:5000/api/chatbot", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ student_id: studentId }),
        });

        const data = await response.json();
        const recommendations = data.response.recommendations;
        
        let html = '<div class="space-y-4">';
        recommendations.forEach(rec => {
            const confidence = (rec.confidence * 100).toFixed(1);
            html += `
                <div class="bg-white p-4 rounded-lg shadow">
                    <h3 class="text-lg font-semibold text-[#5A4033]">${rec.course}</h3>
                    <p class="text-gray-600 mt-1">${rec.description}</p>
                    <div class="mt-2">
                        <div class="w-full bg-gray-200 rounded-full h-2.5">
                            <div class="bg-[#5A4033] h-2.5 rounded-full" style="width: ${confidence}%"></div>
                        </div>
                        <p class="text-sm text-gray-500 mt-1">Match: ${confidence}%</p>
                    </div>
                </div>`;
        });
        html += '</div>';
        
        document.getElementById("ai-recommendations").innerHTML = html;
    } catch (error) {
        document.getElementById("ai-recommendations").innerHTML = 
            '<div class="text-red-500">Failed to load recommendations. Please try again later.</div>';
        console.error("Error fetching AI recommendations:", error);
    }
}

// Auto-fetch recommendations when page loads
document.addEventListener('DOMContentLoaded', fetchAIRecommendations);
