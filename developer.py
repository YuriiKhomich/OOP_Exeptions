"""
the Developer class with the ability to add Developer class objects. The result is a new object
In which name = name1 + ‘ ’ + name2, a tech_stack is a list of technologies of two objects
(only unique values), salary is the larger of the two.

"""

from employee import Employee

class Developer(Employee):
    
    def __init__(self, name_person, salary, email, tech_stack=None):
        super().__init__(name_person, salary, email)
        if tech_stack is None:
            tech_stack = ['Batman']
        self.tech_stack = tech_stack

    def work(self):
        return f'{super().work()[:-1]} and start coding.'

    def __str__(self):
        return f'{self.name_person} the {self.__class__.__name__}.'
        
    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)
    """
    The operation of adding objects of the Developer class.
    
    In which name = name1 + ‘ ’ + name2, a tech_stack is a list of technologies
    of two objects (only unique values), the salary is greater than the two.
    """

    def __add__(self, other):
        name_person1 = self.name_person + ' ' + other.name_person
        tech_stack1 = list(set(self.tech_stack + other.tech_stack))
        salary1 = max(self.salary, other.salary)
        email1 = 'Not'
        person_new = Developer(name_person1, salary1,email1, tech_stack1)
        return person_new
