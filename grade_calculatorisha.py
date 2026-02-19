
name = input("Enter student name: ")
marks = int(input("Enter marks (0-100): "))
if 90 <= marks <= 100:
    grade = "A"
    message = "Excellent Work! "
elif 80 <= marks <= 89:
    grade = "B"
    message = "Very Good! Keep it up! "
elif 70 <= marks <= 79:
    grade = "C"
    message = "Good Job! "
elif 60 <= marks <= 69:
    grade = "D"
    message = "You Passed. Keep Improving!"
elif 0 <= marks <= 59:
    grade = "F"
    message = "Needs Improvement. Don't Give Up! "
else:
    grade = "Invalid"
    message = "Marks should be between 0 and 100."
print("\nRESULT FOR", name.upper() + ":")
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)
print("\n Grading Logic:")