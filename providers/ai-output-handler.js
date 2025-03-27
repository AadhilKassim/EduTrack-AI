// Function to update AI output text dynamically
function updateAIOutput(responseText) {
    const outputElement = document.getElementById("ai-output");
    if (outputElement) {
        outputElement.textContent = responseText;
    } else {
        console.error("AI output element not found on the page.");
    }
}

// Example usage: Call this function with the AI response text
// updateAIOutput("Your weakest subject is Math with a score of 45.");
