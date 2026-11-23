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