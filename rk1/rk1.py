class Teacher:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class EducationalCourse:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.teachers = []

# Creating instances of teachers and educational courses
teacher1 = Teacher(1, "Teacher A")
teacher2 = Teacher(2, "Teacher B")
teacher3 = Teacher(3, "Teacher C")

course1 = EducationalCourse(101, "Course X")
course2 = EducationalCourse(102, "Course Y")
course3 = EducationalCourse(103, "Course Z")

# Associating teachers with educational courses
course1.teachers = [teacher1, teacher2]
course2.teachers = [teacher2, teacher3]
course3.teachers = [teacher1, teacher3]

# Query 1: List of all teachers and educational courses sorted by courses
teacher_course_pairs = [(teacher.name, course.name) for course in [course1, course2, course3] for teacher in course.teachers]
teacher_course_pairs.sort(key=lambda pair: pair[1])

# Query 2: List of educational courses with the total number of teachers in each course
course_teacher_counts = [(course.name, len(course.teachers)) for course in [course1, course2, course3]]
course_teacher_counts.sort(key=lambda pair: pair[1], reverse=True)

# Print the results
print("Query 1: List of all teachers and educational courses sorted by courses:")
for pair in teacher_course_pairs:
    print(f"Teacher: {pair[0]}, Course: {pair[1]}")

print("\nQuery 2: List of educational courses with the total number of teachers in each course:")
for pair in course_teacher_counts:
    print(f"Course: {pair[0]}, Total Teachers: {pair[1]}")
