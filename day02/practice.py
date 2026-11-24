employee_name = input("Enter employee name: ")
employee_salary = float(input("Enter employee salary: "))

if employee_salary >= 40000:
    print("Eligible for bonus")
else:
    print("Not eligible for bonus")

salary = 60000

print(salary >= 40000)
print(salary <= 50000)
print(salary != 70000)


print(5 < 10 < 20)
print(5 < 10 > 20)


#check if eligible for promotion based on years of experience
years_of_experience = int(input("Enter years of experience: "))
if years_of_experience >= 3:
    print("Eligible for promotion")
else:
    print("Not eligible for promotion")

#student performance evaluation based on score
student_score = float(input("Enter student score: "))
if student_score >= 90:
    print("Outstanding")
elif student_score >= 75:
    print("Good")
elif student_score >= 50:
    print("Average")
else:
    print("Needs Improvement")

experience = int(input("Enter years of experience: "))
performance_score = float(input("Enter performance score: "))
if experience >= 5 and performance_score >= 80:
    print("Eligible for promotion")

salary = 60000

if salary >= 50000:

    if salary >= 100000:
        print("Level A")

print("Done")

salary = 120000

if salary >= 50000:

    if salary >= 100000:
        print("Level A")

print("Done")

name = ""

if name:
    print("Valid")

else:
    print("Invalid")

name = "Bharathi"

if name:
    print("Valid")

else:
    print("Invalid")