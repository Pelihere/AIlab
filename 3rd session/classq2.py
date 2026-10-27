
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}

    def add_grade(self, course, grade):
        if grade < 0 or grade > 20:
            print("Invalid grade")
            return

        self.grades[course] = grade

    def average(self):
        if not self.grades:
            return 0

        return sum(self.grades.values()) / len(self.grades)

    def best_course(self):
        if not self.grades:
            return None

        return max(self.grades, key=self.grades.get)

    def failed_courses(self):
        return [
            course
            for course, grade in self.grades.items()
            if grade < 10
        ]

    def status(self):
        avg = self.average()

        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probation"

    def report(self):
        print(f"Student: {self.name} (ID: {self.student_id})")
        print()

        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
            print()

        print(f"Average: {self.average():.2f}")
        print(f"Best course: {self.best_course()}")
        print(f"Failed courses: {self.failed_courses()}")
        print(f"Status: {self.status()}")


# Testing
student1 = Student("Sara Ahmadi", "40312345")
student1.add_grade("Math", 18)
student1.add_grade("Physics", 9)
student1.add_grade("Programming", 20)
student1.add_grade("English", 15)

student2 = Student("Ali Rezaei", "40312346")
student2.add_grade("Math", 12)
student2.add_grade("Physics", 16)
student2.add_grade("Programming", 14)
student2.add_grade("English", 18)

print("=== Student 1 ===")
student1.report()

print("\n=== Student 2 ===")
student2.report()

print("\n=== Invalid Grade Test ===")
student1.add_grade("Chemistry", 25)
