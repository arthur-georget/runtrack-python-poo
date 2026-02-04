class Task:

    def __init__(self, title, description):
        self.__title = title
        self.__description = description
        self.__status = "to do"

    def get_title(self):
        return self.__title
    
    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status    
    
    def set_status(self, status):
        self.__status = status

class TasksList:

    def __init__(self, tasks):
        self.__tasks = tasks

    def addTask(self, task):
        self.__tasks.append(task)

    def deleteTask(self, task):
        self.__tasks.remove(task)

    def endTask(self, task):
        task.set_status("over")

    def getTaskList(self):
        taskList = []
        for task in self.__tasks:
            taskList.append(task.get_title())
        return taskList
    
    def getFilteredTaskList(self, filter):
        filteredTaskList = []
        for task in self.__tasks:
            if task.get_status() == filter:
                filteredTaskList.append(task.get_title())
        return filteredTaskList

task1 = Task("Vaisselle", "Nettoyer et ranger la vaisselle.")
task2 = Task("Projet perso","Développer projet perso.")
task3 = Task("Fruit Slicer","Continuer à développer le Fruit Slicer.")
task4 = Task("Alternance","Préparer campagne de mail pour l'alternance.")
task5 = Task("Sport", "Faire 6 minutes de gainage et 50 squats.")
task6 = Task("Runtrack", "Faire les exercice de Runtrack d'aujourd'hui")

taskList1 = TasksList([task1,task2,task3,task4,task5])

print(f"Tâches: {taskList1.getTaskList()}")

taskList1.addTask(task6)
taskList1.deleteTask(task1)
taskList1.endTask(task3)

print(f"A faire: {taskList1.getFilteredTaskList("to do")}")
print(f"Terminé: {taskList1.getFilteredTaskList("over")}")