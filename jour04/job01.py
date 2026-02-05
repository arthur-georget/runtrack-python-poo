class People:
    
    def __init__(self, age: int=14):
        self._age = age

    def display_age(self):
        print(f"{self._age} ans")

    def hello(self):
        print("Hello")

    def update_age(self, age: int):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            print("update_age(): The age provided is not an int > 0")

class Student(People):

    def __init__(self, age: int=14):
        super().__init__(age)

    def go_in_class(self):
        print("Je vais en cours.")

    def display_age(self):
        print(f"J'ai {self._age} ans.")

class Teacher(People):

    def __init__(self, discipline: str, age: int=30):
        super().__init__(age)
        self.__discipline = discipline

    def teach(self):
        print(f"Le cours de {self.__discipline} va commencer.")

henry = People()

theo = Student()
theo.display_age()
