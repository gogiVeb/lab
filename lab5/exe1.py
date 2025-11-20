class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"


class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department

    def manage_project(self,):
        return f"Менеджер {self.name} управляет отделом: {self.department}."

class Technician(Employee):
    def __init__(self, name, id, specialization):
        Employee.__init__(self, name, id)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник {self.name} работает в отделе: {self.specialization}."


class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Manager.__init__(self, name, id, department)
        Technician.__init__(self, name, id, specialization)
        self.subordinates = []

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        info = [f"Команда технического менеджера {self.name} (ID: {self.id}, Отдел: {self.department}, Специализация: {self.specialization}):"]
        if not self.subordinates:
            info.append("  Нет подчиненных.")
        else:
            for i, emp in enumerate(self.subordinates, 1):
                info.append(f"  {i}. {emp.get_info()}")
        return "\n".join(info)


#Демонстрация работы класса Employee
print("\n         Список сотрудников")
person_1 = Employee("Воронцова Алиса", "103F")
person_2 = Employee("Балкин Георгий", "1A32")
person_3 = Employee("Смирнов Андрей", "T242")
person_4 = Employee("Козлов Дмитрий", "00N1")
print(person_1.get_info(), person_2.get_info(), person_3.get_info(), person_4.get_info(), sep='\n')

print("")

#Демонстрация работы класса Manager
mgr = Manager(person_1.name, person_1.id, "Клиенских обращений ГП")
print(mgr.manage_project())

print("")

#Демонстрация работы класса Technician
tech = Technician(person_2.name, person_2.id, "Solar")
print(tech.perform_maintenance())

print("")

#Демонстрация работы класса TechManager (Добавление сотрудников в одну команду)
print(f"    Проверка команды {person_3.name}    ")
tech_mgr_empty = TechManager(person_3.name, person_3.id, "Мониторинга", "Zabbix")
print(tech_mgr_empty.get_team_info())

print("")

print(f"    Проверка команды {person_4.name}    ")
tech_mgr = TechManager(person_4.name, person_4.id, "Внедрения", "ALT Linux")
tech_mgr.add_employee(person_1)
tech_mgr.add_employee(person_2)
print(tech_mgr.get_team_info())