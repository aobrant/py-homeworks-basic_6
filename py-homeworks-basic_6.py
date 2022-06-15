class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lt(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and grade in range(10) :
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_grade(self):
        count = 0
        sum = 0
        for key in self.grades:
            for i in (self.grades[key]):
                count += 1
                sum += i
        res = round( sum/count ,1 )
        return res
    
    def __str__(self):
        res = f'''
        Имя: {self.name} 
        Фамилия: {self.surname}
        Средняя оценка за домашние задания: {self.average_grade()}
        Курсы в процессе изучения:{self.courses_in_progress} 
        Завершенные курсы:{self.finished_courses} 
        '''
        return res
    def __lt__(self,other):
        return self.average_grade < other.average_grade

    



         
        
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

       
        
   
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}
    def average_grade(self):
        count = 0
        sum = 0
        for key in self.grades:
            for i in (self.grades[key]):
                count += 1
                sum += i
        res = round( sum/count ,1 ) 
        return res
    def __str__(self):
        res = f'''
        Имя: {self.name} 
        Фамилия: {self.surname} 
        Средняя оценка за лекции: {self.average_grade()}
        '''
        return res
    def __lt__(self,other):
        return self.average_grade() < other.average_grade()


        
    
class Reviewer(Mentor):
    def __str__(self):
        res = f'''
        Имя: {self.name} 
        Фамилия: {self.surname} 
        '''
        return res
    def __init__(self, name, surname):
        super().__init__(name,surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return ('Ошибка')
    


def average_lectours(course,lectour):
    count = 0
    sum = 0
    for lect in lectour:
        if course in lect.grades: 
            for i in (lect.grades[course]):
                count += 1
                sum += i
            else:
                continue

    res = round( sum/count ,1 )
    return res
def average_students(course,student):
    count = 0
    sum = 0
    for stud in student:
        for i in (stud.grades[course]):
                count += 1
                sum += i
    res = round( sum/count ,1 )
    return res    


Ivanov = Student('Sergey','Ivanov','male')
Petrova = Student('Larisa','Petrova','female') 
Sidorov = Lecturer('Anton','Sidorov')
Grigorjev = Lecturer('Alexander','Grigorjev')
Kochenev = Reviewer('Alexander','Kochenev')
Strelnikova = Reviewer('Violetta',"Strelnikova")
Strelnikova.courses_attached = ['Python','Java']
Ivanov.courses_in_progress = ['Python']
Ivanov.finished_courses = ['Java']
Petrova.courses_in_progress = ['Java','Python']
Petrova.finished_courses = ['Python']
Ivanov.grades = {'Python':[4,3,2,4,5],'Java':[3,5,7]}
Petrova.grades  = {'Python':[5,4],'Java':[3,3,3]}
Sidorov.courses_attached = ['Python','Java']
Grigorjev.courses_attached = ['Python']
Sidorov.grades = {'Python':[5,5],'Java':[2,5]}
Grigorjev.grades = {'Python':[5,5,4,5]}
students = [Ivanov,Petrova]
lectours = [Sidorov,Grigorjev]
studyis = []
studyis = ['Java','Python']
print(Ivanov)
print(Grigorjev)
print(Kochenev)
st = Ivanov
lct = Sidorov
Strelnikova.rate_hw(st,'Python',9)
Petrova.rate_lt(lct,'Java',7)
# print (lct.grades )
# print (st.grades )

if Grigorjev > Sidorov :
    print('Григорьев как лектор лучше Сидорова') 
else:
   print('Сидорова как лектор лучше Григорьева') 
name = input('Введите название курса:')
if name not in studyis:
    print('Ошибка')
else:
    print(f'Средняя оценка лекторов по курсу {average_lectours(name,lectours)} \n Средняя оценка студентов по курсу {average_students(name,students)}')


