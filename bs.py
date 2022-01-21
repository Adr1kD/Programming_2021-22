class Person():
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

    def __str__(self):
        return 'Pers name is {self.name} and age is {self.age}'
