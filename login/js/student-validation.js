const studentIds = [
    "STU000001", "STU000002", "STU000003", "STU000004", "STU000005",
    // ...add more IDs as needed from the CSV
];

function validateStudentId(studentId) {
    return studentIds.includes(studentId);
}
