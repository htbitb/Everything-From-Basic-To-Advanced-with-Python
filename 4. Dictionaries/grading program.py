student_scores ={
    "Harry": 81,
    "Ron": 79,
    "Hermione": 90,
    "Draco": 74,
    "Neville": 62
}

for key in student_scores:
    score = student_scores[key]
    if score >= 90:
        student_scores[key] = "Outstanding"
    elif score >= 80:
        student_scores[key] = "Exceeds expectation"
    elif score >= 70:
        student_scores[key] = "Acceptable"
    else:
        student_scores[key] = "fail"

print(student_scores)