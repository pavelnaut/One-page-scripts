import sys
 
 
class Human:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{self.first_name} {self.last_name}"
 
 
class Teacher(Human):
    def __init__(self, first_name, last_name, intelligence, competence):
        Human.__init__(self, first_name, last_name)
        self.intelligence = intelligence
        self.competence = competence
 
 
class DreamTeacher(Teacher):
    def __init__(self, first_name, last_name, intelligence, competence, empathy, charm):
        Teacher.__init__(self, first_name, last_name, intelligence, competence)
        self.empathy = empathy
        self.charm = charm
 
    def __str__(self):
        return f"Thank you for being the best, {self.first_name}!"
 
 
student = {'fun': 0, 'knowledge': 0, 'inspiration': 0}
 
my_teacher = DreamTeacher('Ines', 'Ivanova', sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize)
 
while my_teacher.full_name == 'Ines Ivanova':
 
    for quality in student.keys():
        student[quality] += 1
 
    try:
        print(my_teacher)
    except:
        print("Stop kidding me. There is no way to raise exception in this case!")
 
    next_lesson = eval(input())
    # TODO MORE LESSONS!
