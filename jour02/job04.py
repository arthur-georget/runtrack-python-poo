class Student:

    def __init__(self, surname, name, student_id):
        self.__surname = surname
        self.__name = name
        self.__student_id = student_id
        self.__credits = 0
        self.__level = self.__studentEval()
    
    def get_surname(self):
        return self.__surname
    
    def set_surname(self, surname):
        self.__surname = surname

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_student_id(self):
        return self.__student_id
    
    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_credits(self):
        return self.__credits
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__studentEval()
        else:
            print(f"Le nombre de crédits à ajouter à {self.__name} doit être supérieur à 0.")

    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        
    def studentInfo(self):
        print(f"Nom = {self.__surname}")
        print(f"Prénom = {self.__name}")
        print(f"id = {self.__student_id}")
        print(f"Niveau = {self.__level}")

student1 = Student("Doe", "John", 145)
student1.add_credits(23.4)
student1.add_credits(30)
student1.add_credits(-101)
student1.add_credits(101)

print(f"Le nombre de credits de {student1.get_name()} {student1.get_surname()} est de {student1.get_credits()} points")

student1.studentInfo()