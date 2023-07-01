salary, grade = input().split()

basic_salary = int(salary)
hra = 20 * basic_salary / 100
da = 50 * basic_salary / 100
pf = 11 * basic_salary / 100

if grade == 'A':
    total_salary = round(basic_salary + hra + da + 1700 - pf)
    print(total_salary)
elif grade == 'B':
    total_salary = round(basic_salary + hra + da + 1500 - pf)
    print(total_salary)
else:
    total_salary = round(basic_salary + hra + da + 1300 - pf)
    print(total_salary)