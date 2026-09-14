# School Management System

A simple school management system built with **Python Object-Oriented Programming (OOP)**.

The project demonstrates important OOP concepts including **inheritance, encapsulation, properties, method overriding, class attributes, constructors, and object relationships**.

## Features

* Create students and teachers
* Store personal information such as name and email
* Assign grades to students
* Validate student grades between 0 and 100
* Add students to courses
* Assign teachers to courses
* Display enrolled students and their grades
* Track the total number of students
* Track the total number of courses
* Demonstrate inheritance and method overriding

## Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**

No external Python libraries are required.

## Project Structure

```text
school-management-oop/
│
├── main.py
├── requirements.txt
└── README.md
```

> Make sure to save the Python code as `main.py`.

## Object-Oriented Programming Concepts

### 1. Classes

The project contains four main classes:

* `Person`
* `Student`
* `Teacher`
* `Course`

Each class represents a different entity in the school management system.

---

### 2. Inheritance

`Student` and `Teacher` inherit from the `Person` class.

```python
class Student(Person):
```

```python
class Teacher(Person):
```

This allows both classes to reuse the attributes and methods defined in `Person`.

For example, both students and teachers have:

* Name
* Email
* Introduction functionality

---

### 3. Constructor and `super()`

The `Student` and `Teacher` classes use `super()` to call the constructor of the parent `Person` class.

```python
super().__init__(name, email)
```

This initializes the common `name` and `email` attributes without duplicating the code.

---

### 4. Encapsulation with Properties

The student's grade is managed using a Python property.

```python
@property
def grade(self):
    return self._grade
```

A setter is used to validate the grade:

```python
@grade.setter
def grade(self, value):
    if 0 <= value <= 100:
        self._grade = value
```

This prevents valid grades from being outside the range of 0 to 100.

---

### 5. Class Attributes

The `Student` class contains:

```python
total_students = 0
```

Every time a new student is created, the value increases:

```python
Student.total_students += 1
```

The `Course` class uses a similar class attribute:

```python
total_courses = 0
```

This keeps track of how many student and course objects have been created.

---

### 6. Method Overriding

The `Person` class has an `introduce()` method.

```python
def introduce(self):
    return f"Hello, my name is {self.name} and my email is {self.email}."
```

Both `Student` and `Teacher` override this method to provide their own implementation.

For example, `Student` includes the student's grade:

```python
def introduce(self):
    return f"Hello, my name is {self.name}, my email is {self.email}, and I am a student with a grade of {self.grade}."
```

The `Teacher` class includes the subject they teach:

```python
def introduce(self):
    return f"Hello, my name is {self.name}, my email is {self.email}, and I teach {self.subject}."
```

This demonstrates **polymorphism**, where different classes can provide different implementations of the same method.

---

### 7. Object Relationships

The project also demonstrates relationships between objects.

A `Course` has a teacher:

```python
c1 = Course("Algebra", t1)
```

A course also contains a list of students:

```python
self.students = []
```

Students can then be added to the course:

```python
c1.add_student(s1)
c1.add_student(s2)
```

Teachers also have a list of courses:

```python
self.courses = []
```

This creates relationships between:

```text
Teacher
   │
   ▼
Course
   │
   ├── Student
   └── Student
```

## Example

The program creates a teacher:

```python
t1 = Teacher(
    "Mr. Smith",
    "mr.smith@school.com",
    "Math"
)
```

Then creates an Algebra course:

```python
c1 = Course("Algebra", t1)
```

Two students are created:

```python
s1 = Student(
    "Alice",
    "alice@school.com",
    85
)

s2 = Student(
    "Bob",
    "bob@school.com",
    90
)
```

The students are then enrolled in the course:

```python
c1.add_student(s1)
c1.add_student(s2)
```

## Example Output

```text
Alice has been added to the course Algebra.
Bob has been added to the course Algebra.

Hello, my name is Mr. Smith, my email is mr.smith@school.com, and I teach Math.

Hello, my name is Alice, my email is alice@school.com, and I am a student with a grade of 85.

Hello, my name is Bob, my email is bob@school.com, and I am a student with a grade of 90.

Total students: 2

Students enrolled in Algebra:
- Alice (Grade: 85)
- Bob (Grade: 90)
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/school-management-oop.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Open the Project Folder

```bash
cd school-management-oop
```

### 3. Run the Program

Since the project does not require external packages, you can run it directly:

```bash
python main.py
```

## Validation

The project validates student grades.

Valid grades:

```text
0
50
85
100
```

Invalid grades:

```text
-10
101
150
```

An invalid grade produces:

```text
Invalid grade. Grade must be between 0 and 100.
```

## Possible Future Improvements

The project can be extended with:

* Student IDs
* Teacher IDs
* Unique course IDs
* Student enrollment management
* Removing students from courses
* Removing courses
* Assigning multiple teachers
* Student attendance
* Exam and assignment management
* Grade calculation
* Database integration using MySQL
* Graphical User Interface (GUI)
* Web interface using Flask or Django
* Automated testing

## Learning Objectives

This project was created to practice:

* Classes and objects
* Constructors
* Instance attributes
* Class attributes
* Inheritance
* Encapsulation
* Properties
* Getters and setters
* Method overriding
* Polymorphism
* `super()`
* Lists and object relationships
* Basic input validation
