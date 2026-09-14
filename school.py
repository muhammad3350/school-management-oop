class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        return f"Hello, my name is {self.name} and my email is {self.email}."


class Student(Person):

    total_students = 0

    def __init__(self, name, email, grade):
        super().__init__(name, email)
        self.grade = grade
        Student.total_students += 1
        self.courses = []

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if 0 <= value <= 100:
            self._grade = value
        else:
            print("Invalid grade. Grade must be between 0 and 100.")

    def add_course(self, course):
        self.courses.append(course)

    def introduce(self):
        return f"Hello, my name is {self.name}, my email is {self.email}, and I am a student with a grade of {self.grade}."

class Teacher(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
        self.courses = []       

    def introduce(self):
        return f"Hello, my name is {self.name}, my email is {self.email}, and I teach {self.subject}."

    def add_course(self, course):
        self.courses.append(course)

class Course:
    total_courses = 0
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []
        Course.total_courses += 1

    def add_student(self, student):
            if student not in self.students:
                self.students.append(student)
                print(f"{student.name} has been added to the course {self.course_name}.")

            else:
                print(f"{student.name} is already enrolled in the course {self.course_name}.")

    def show_students(self):
        print(f"Students enrolled in {self.course_name}: ")
        if len(self.students) == 0:
            print("No students enrolled.")
            return
        for student in self.students:
            print(f"- {student.name} (Grade: {student.grade})")


t1 = Teacher("Mr. Smith", "mr.smith@school.com", "Math")
c1 = Course("Algebra", t1)

t1.add_course(c1)

s1 = Student("Alice", "alice@school.com", 85)
s2 = Student("Bob", "bob@school.com", 90)

c1.add_student(s1)
c1.add_student(s2)

print(t1.introduce())
print(s1.introduce())
print(s2.introduce())
print(f"Total students: {Student.total_students}")
print()
c1.show_students()
