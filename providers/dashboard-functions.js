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

/**
 * Updates the attendance section dynamically.
 * @param {number} present - Number of days present.
 * @param {number} absent - Number of days absent.
 */
function updateAttendance(present, absent) {
    const total = present + absent;
    const percentage = ((present / total) * 100).toFixed(2);

    document.getElementById('attendance-percentage').textContent = `${percentage}%`;
    document.getElementById('attendance-present').textContent = `Present: ${present}`;
    document.getElementById('attendance-absent').textContent = `Absent: ${absent}`;
}

// Example usage: Update the GPA Tracker with a dynamic value
// updateGPATracker(9.6);

// Example usage: updateAttendance(19, 1);
