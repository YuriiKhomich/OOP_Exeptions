from employee import Employee


class Recruiter(Employee):
    
    def work(self):
        return f'{super().work()[:-1]} and start hiring.'

    def __str__(self):
        return f'{self.name_person} the {self.__class__.__name__}.'
