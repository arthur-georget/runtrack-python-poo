class People:
    
    def __init__(self, name: str, age: int=14):
        self._name = name
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise Exception("People.__init__(): The age provided is not an int > 0")

    def display_age(self):
        print(f"Age de {self._name}: {self._age} ans")

    def hello(self):
        print(f"{self._name}: Hello")

    def update_age(self, age: int):
        if isinstance(age, int) and age > 0:
            self._age = age
        else:
            raise Exception("update_age(): The age provided is not an int > 0")

class Student(People):

    def __init__(self, age: int=14):
        super().__init__(age)

    def go_in_class(self):
        print(f"{self._name}: Je vais en cours.")

    def display_age(self):
        print(f"{self._name}: J'ai {self._age} ans.")

class Teacher(People):

    def __init__(self, name: str, discipline: str, age: int=30):
        super().__init__(name, age)
        self.__discipline = discipline

    def teach(self):
        print(f"{self._name}: Le cours de {self.__discipline} va commencer.")

student = Student("Théo")

student.hello()
student.go_in_class()
student.update_age(15)
student.display_age()

teacher = Teacher("M. Durand","mathématique",40)
teacher.hello()
teacher.teach()