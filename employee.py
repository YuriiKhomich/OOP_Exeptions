"""
The Employee class determines the salary of an employee for
a certain number of days or wages for the period from 01
current month to today. Compares the salary of two employees.

"""
import datetime
from datetime import timedelta


class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name_person, salary, email):
        self.name_person = name_person
        self.salary = salary
        self.email = email
        self.validate()
        self.save_email()
    
    def save_email(self):
        with open('emails.txt', 'a') as fp:
            fp.write(self.email + '\n')
    
    def validate(self):
        with open('emails.txt', 'r') as f:
            emails = f.read().splitlines()
        for email in emails:
            if email.strip() == self.email:
                raise EmailAlreadyExistsException(f"Email '{self.email}' already exists.")

    def __str__(self):
        return f'{self.name_person} the {self.__class__.__name__}.'
    
    def work(self):
        return f'{self.name_person}: I come to the office.'
    
    def check_salary(self, days: int = None):
        
        if days:
            return self.salary * days
        start_day = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month, 1)
        finish_day = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month,
                                   datetime.datetime.now().day)
        delta_days = finish_day - start_day
        total_salary = (sum(1 for day in (start_day + timedelta(x) for x in range(delta_days.days))
                            if day.isoweekday() < 6)) * self.salary
        return total_salary
    
    """
    Comparison of Employee by level of salary.
    """
    
    def __lt__(self, other):
        return self.salary < other.salary
    
    def __le__(self, other):
        return self.salary <= other.salary
    
    def __gt__(self, other):
        return self.salary > other.salary
    
    def __ge__(self, other):
        return self.salary >= other.salary
    
    def __eq__(self, other):
        return self.salary == other.salary
    
    def __ne__(self, other):
        return self.salary != other.salary
