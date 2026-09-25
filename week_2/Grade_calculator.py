name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

if marks >= 90:
    grade = "A"
    message = "Excellent! Keep it up! 👍"
elif marks >= 80:
    grade = "B"
    message = "Very Good! Keep it up! 👍"
elif marks >= 70:
    grade = "C"
    message = "Good job! Keep improving! 💪"
elif marks >= 60:
    grade = "D"
    message = "Good effort! You can do better! 💪"
else:
    grade = "F"
    message = "Don't give up! Keep practicing! 🌟"

print(f"\nRESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")