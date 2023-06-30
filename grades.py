class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def get_grade(self):
        return self.grade    
    
class Course:
    
    def __init__(self, c_title, max_students):
        self.c_title = c_title
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
        
    def average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            
        return value / len(self.students)            
    
    
