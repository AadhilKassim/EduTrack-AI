// Function to update the GPA Tracker dynamically
function updateGPATracker(gpa) {
    const maxGPA = 10.0;
    const percentage = (gpa / maxGPA) * 100;
    const circle = document.getElementById("progress-circle");
    const gpaValue = document.getElementById("gpa-value");

    // Update the stroke-dashoffset to reflect the GPA percentage
    circle.style.strokeDashoffset = 100 - percentage;

    // Update the displayed GPA value
    gpaValue.textContent = gpa.toFixed(2);
}

// Function to fetch and parse CSV data
async function fetchCSVData(filePath) {
    const response = await fetch(filePath);
    const csvText = await response.text();
    const rows = csvText.split("\n").map(row => row.split(","));
    const headers = rows[0];
    const data = rows.slice(1).map(row => {
        const obj = {};
        headers.forEach((header, index) => {
            obj[header.trim()] = row[index]?.trim();
        });
        return obj;
    });
    return data;
}

// Function to display GPA and attendance details
async function displayDashboardDetails() {
    const data = await fetchCSVData("../providers/ResearchInformation3.csv");
    const student = data.find(d => d.Name === "John Student"); // Replace with dynamic student name if needed

    if (student) {
        // Update GPA Tracker
        const gpa = parseFloat(student.Overall);
        updateGPATracker(gpa);

        // Update Attendance
        const attendanceElement = document.querySelector("#attendance-percentage");
        if (attendanceElement) {
            attendanceElement.textContent = student.Attendance;
        }

        // Update other metrics (e.g., AI Insights, Course Progress) as needed
        // Example: Update AI Insights
        const insightsElement = document.querySelector("#ai-insights");
        if (insightsElement) {
            insightsElement.textContent = `📚 You're excelling in ${student.Department}!`;
        }
    }
}

// Call the function to display details on page load
document.addEventListener("DOMContentLoaded", displayDashboardDetails);
