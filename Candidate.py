"""
Створити @classmethod generate candidates, який приймає в якості аргументу шлях до файлу
Метод generate candidates має повертати список об’єктів класу Candidate
Файл тут (тиць)
"""
import csv
import urllib.request


class Candidate:
    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skil = main_skill
        self.main_skil_grade = main_skill_grade
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def generate_candidates(cls, path_to_file):
        """
        Прочитати файл.
        Для кожного рядку в файлі створити словник:
            ключі: атрибути класу
            значення: дані з рядку
        Згенерувати список об'єктів.
       """
        with open(path_to_file) as source_file:
            reader = csv.DictReader(source_file)
            cand_data_prepared = []
            for record in reader:
                candidate = dict(
                    first_name=record['Full Name'].split(maxsplit=1)[0],
                    last_name=record['Full Name'].split(maxsplit=1)[1],
                    email=record['Email'],
                    tech_stack=record['Technologies'].split('|'),
                    main_skill=record['Main Skill'],
                    main_skill_grade=record['Main Skill Grade']
                )
                cand_data_prepared.append(candidate)
            return [cls(**x) for x in cand_data_prepared]
    
    @classmethod
    def generate_candidates_url(cls, url: str):
        """
        Отримувати в якості аргументу URL на файл та генерувати кандидатів з нього
        Для кожного рядку в файлі створити словник:
            ключі: атрибути класу
            значення: дані з рядку
        Згенерувати список об'єктів.
       """
        with urllib.request.urlopen(url) as source_file:
            reader = csv.DictReader(source_file.read().decode('utf-8').splitlines())
            cand_data_prepared = []
            for record in reader:
                candidate = dict(
                    first_name=record['Full Name'].split(maxsplit=1)[0],
                    last_name=record['Full Name'].split(maxsplit=1)[1],
                    email=record['Email'],
                    tech_stack=record['Technologies'].split('|'),
                    main_skill=record['Main Skill'],
                    main_skill_grade=record['Main Skill Grade']
                )
                cand_data_prepared.append(candidate)
            return [cls(**x) for x in cand_data_prepared]

if __name__ == '__main__':
    candidates = Candidate.generate_candidates('candidates_csv.csv')
    print([x.full_name for x in candidates])
    url = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
    candidates_url = Candidate.generate_candidates_url(url)
    print([x.full_name for x in candidates_url])
