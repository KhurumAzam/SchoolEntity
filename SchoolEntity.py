class SchoolEntity:
    
    directory = {}
    
    def __init__(self):
        pass
    
    def __init__(self, name, age, role):
        self.__add_entry(name, age, role)

    def add_entry(self, name, age, role):
        self.directory[name] = {age, role}

    def add_entry(self, name, age, role, gpa):
        self.directory[name] = {age, role, gpa}

    def name(self): return str(input("Student Name: "))
    def age(self): return int(input("Student Age: "))


class Student(SchoolEntity):
    def __init__(self):
        name = super().name()
        age = super().age()
        role = "Student"
        gpa = self.GPA()
        super().add_entry(name, age, role, gpa)

    def GPA(self): return float(input("Student GPA: "))

class Faculty(SchoolEntity):
    def __init__(self):
        name = super().name()
        age = super().age()
        role = "Teacher"
        super().add_entry(name, age, role, gpa)

if __name__ == "__main__":
    try:
        directory_entry = SchoolEntity()
        while True:
            choice = int(input("What to you want to do:/n1. Add a student entry/n2.Add a teacher entry"))
            if choice == 1:
                student = Student()
                directory_entry.directory.update(student.directory)
            elif choice == 2:
                teacher = Teacher()
                directory_entry.directory.update(teacher.directory)
            else:
                print("Invalid Choice, please enter a valid entry")

            print(directory_entry.directory)
            exit_value = input("Do you want to exit ('Yes' or 'No'): ")
            if exit_value == "Yes":
                break
    except Exception as e:
        print("Error issue with program:", e)
