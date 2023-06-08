student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score >= 90:
    grade = "A"
  elif score >= 80:
    grade = "B"
  elif score >= 70:
    grade = "C"
  elif score >= 60:
    grade = "D"
  else:
    grade = "F"
  
  student_grades[student] = grade

print(student_grades)