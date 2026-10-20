
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def top_student(self):
        if not self.students:
            return None

        return max(self.students, key=lambda student: student.average())

    def class_average(self):
        if not self.students:
            return 0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)


# Testing
classroom = Classroom()

classroom.add_student(student1)
classroom.add_student(student2)

top = classroom.top_student()

if top is not None:
    print(f"Top student: {top.name}")
    print(f"Top student's average: {top.average():.2f}")

print(f"Class average: {classroom.class_average():.2f}")
