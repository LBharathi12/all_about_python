# Experience >= 5 years
# Performance Score >= 85
# Salary >= 50000
# Name must not be empty

name = input("Enter your name: ")
experience = int(input("Enter years of experience: "))
performance_score = float(input("Enter performance score: "))
salary = float(input("Enter salary: "))
if not name:
    print("Name cannot be empty")
elif experience < 5:
    print("Experience requirement not met")
elif performance_score < 85:
    print("Performance score requirement not met")
elif salary < 50000:
    print("Salary requirement not met")
else:
    print("Eligible for promotion")