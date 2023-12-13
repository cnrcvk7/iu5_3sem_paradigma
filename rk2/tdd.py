import unittest

class TestEducationalSystem(unittest.TestCase):

    def test_get_teacher_course_pairs(self):
        courses = [EducationalCourse(101, "Course X"), EducationalCourse(102, "Course Y")]
        teacher1 = Teacher(1, "Teacher A")
        teacher2 = Teacher(2, "Teacher B")
        courses[0].teachers = [teacher1, teacher2]

        pairs = get_teacher_course_pairs(courses)
        self.assertEqual(pairs, [('Teacher A', 'Course X'), ('Teacher B', 'Course X'), ('Teacher A', 'Course Y'), ('Teacher B', 'Course Y')])

    def test_sort_teacher_course_pairs(self):
        pairs = [('Teacher B', 'Course X'), ('Teacher A', 'Course Z'), ('Teacher C', 'Course Y')]
        sorted_pairs = sort_teacher_course_pairs(pairs)
        self.assertEqual(sorted_pairs, [('Teacher A', 'Course Z'), ('Teacher B', 'Course X'), ('Teacher C', 'Course Y')])

    def test_get_course_teacher_counts(self):
        courses = [EducationalCourse(101, "Course X"), EducationalCourse(102, "Course Y")]
        teacher1 = Teacher(1, "Teacher A")
        teacher2 = Teacher(2, "Teacher B")
        courses[0].teachers = [teacher1, teacher2]

        counts = get_course_teacher_counts(courses)
        self.assertEqual(counts, [('Course X', 2), ('Course Y', 0)])

if name == 'main':
    unittest.main()