# Student Grade Evaluation Program (with average calculation)

# Accept marks for 5 subjects
marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)

# Calculate average
average = sum(marks) / 5

# Determine grade based on average marks
if average >= 90:
    grade = 'A'
elif average >= 75:
    grade = 'B'
elif average >= 50:
    grade = 'C'
elif average >= 35:
    grade = 'D'
else:
    grade = 'Fail'

# Display results
print("Average Marks:", round(average))
print("Grade:", grade)