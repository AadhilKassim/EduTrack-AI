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

// Example usage: Update the GPA Tracker with a dynamic value
// updateGPATracker(9.6);
