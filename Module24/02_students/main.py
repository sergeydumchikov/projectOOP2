
class Student:
    surname = 'Ivanov'
    name = 'Ivan'
    group = '000'
    progress = 0

    def __init__(self, surname, name, group, progress):
        self.surname = surname
        self.name = name
        self.group = group
        self.progress = progress

    def info(self):
        print(
            'Family: {}\nName: {}\nNumber group: {}\nProgress: {}\n'.format(
            self.surname, self.name, self.group, self.progress
        ))

students = []
for i in range(10):
    information = input('Введите Фамилию, Имя, номер группы и успеваемость (ЧЕРЕЗ ПРОБЕЛ): ').split()
    if len(information) == 4:
        i_Student = Student(information[0], information[1], information[2], int(information[3]))
        students.append(i_Student)

sort_list_stud = students.sort(key=lambda x: x.progress, reverse=True)
newlist = sorted(students, key=lambda x: x.progress, reverse=True)

for i in newlist:
    i.info()