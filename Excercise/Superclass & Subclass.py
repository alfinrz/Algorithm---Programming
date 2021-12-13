#Person
class person:
    def __init__(self, name, adress):
        self.name = name
        self.adress = adress

    def getname(self):
        return self.name

    def getadress(self):
        return self.adress
    
    def setadress(self):
        self.adress

    def __str__(self):
        return f"Name: {self.name}\n Adress: {self.adress}"

#Student
class student:
    def __init__(self, name, adress):
        person.__init__(name,adress)
        self.grade = 0.0
    
    def setgrade(self, grade):
        if grade > 70.0
            self.grade = grade
            return grade
        else:
            self.grade = "Void"

    def printgrade(self,setgrade):
        if setgrade = True
            print("You've passed")
        else:
            print("void")

    def __str__(self):
        return f"Name: {person.__init__(name)}\n Adress: {person.__init__(adress)}\n Grade: {self.grade}"

#Teacher
class teacher:
    def __init__(self, name, adress, numCourses, Courses):
        person.__init__(name,adress)
        self.set_NumCourses(numCourses) 
        self.courses = Courses
    
    def set_NumCourses(self, numCourses):
        while True:
            if numCourses > 0
                print("you have exceeded number of courses")
            else:
                break

    def set_Courses(self, Courses):
        if self.courses.lower() == ""
            print("Course does not exist")
        else:
            break

    def getcourses(self):
        return self.courses

    def get_Numcourses(self):
        return self.set_NumCourses()
    
    def __str__(self):
        return f"Name & Adress: {person.__init__(name)}\n Adress: {person.__init__(adress)}\n Courses: {self.courses}\n Number of Courses: {self.set_NumCourses(numCourses)}"
