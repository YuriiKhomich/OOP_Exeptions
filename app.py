import datetime
import traceback

from employee import Employee
from employee import EmailAlreadyExistsException
from developer import Developer
from recruiter import Recruiter


def main():
    person = Employee('John', 300, 'John@gmail.com')
    person1 = Employee('Jim', 305, 'Jim@gmail.com')
    print(person.work())
    print(person1.work())
    person2 = Recruiter('Bob', 303, 'Bob@gmail.com')
    person3 = Developer('Niki', 320, 'Nikki@gmail.com')
    print(person2.work())
    print(person3.work())
    print(person3)
    print(person)
    person4 = Developer('Johny', 300, 'Johny@gmail.com', ['Basic', 'C+'])
    person5 = Developer("Bobi", 305, 'Bob1@gmail.com', ['Python', 'Pascal', 'Cobol'])
    print(f"{person1} You salary for {person1.check_salary(10)} hrn")
    print(f"{person}, total salary to date:  {person.check_salary()} hrn")
    print(person4 < person5)
    person_new = person4 + person5
    print(f'ADD two personas: {person_new} Max salary: {person_new.salary}'
          f' Total skill: {person_new.tech_stack}')
        
if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        err = traceback.format_exc()
        with open('logs.txt', 'a') as ft:
            ft.write(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | {err}\n')
    