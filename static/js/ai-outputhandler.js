class RecommendationSystem {
    constructor() {
        this.apiUrl = 'http://localhost:5000/recommend';
    }

    async getRecommendations(studentData) {
        try {
            const response = await fetch(this.apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(studentData)
            });

            const data = await response.json();
            if (data.status === 'success') {
                return data.recommendations;
            } else {
                throw new Error(data.message);
            }
        } catch (error) {
            console.error('Error fetching recommendations:', error);
            throw error;
        }
    }

    displayRecommendations(recommendations) {
        const container = document.getElementById('ai-recommendations');
        container.innerHTML = `
            <div class="mt-8 space-y-6">
                ${recommendations.map(rec => `
                    <div class="bg-white rounded-lg shadow-md p-6">
                        <div class="flex justify-between items-start">
                            <div>
                                <h3 class="text-xl font-semibold text-[#5A4033]">${rec.course}</h3>
                                <p class="text-gray-600 mt-2">${rec.description}</p>
                            </div>
                            <div class="bg-green-100 text-green-800 px-3 py-1 rounded-full">
                                ${(rec.confidence * 100).toFixed(1)}% Match
                            </div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }

    async initialize() {
        // Example student data - replace with actual student data
        const studentData = {
            'Department': 'Computer Science and Engineering',
            'Gender': 'Male',
            'Income': 'High (Above 50,000)',
            'Hometown': 'City',
            'Gaming': 'Yes',
            'Attendance': '80%-100%',
            'Job': 'No',
            'English': 4.0,
            'Overall': 3.75
        };

        try {
            const recommendations = await this.getRecommendations(studentData);
            this.displayRecommendations(recommendations);
        } catch (error) {
            document.getElementById('ai-recommendations').innerHTML = `
                <div class="mt-8 text-red-600">
                    Error loading recommendations. Please try again later.
                </div>
            `;
        }
    }
}

// Initialize the recommendation system
document.addEventListener('DOMContentLoaded', () => {
    const recommender = new RecommendationSystem();
    recommender.initialize();
});
