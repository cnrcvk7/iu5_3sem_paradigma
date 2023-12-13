class Teacher:
    def init(self, id, name):
        self.id = id
        self.name = name


class EducationalCourse:
    def init(self, id, name):
        self.id = id
        self.name = name
        self.teachers = []


def get_teacher_course_pairs(courses):
    return [(teacher.name, course.name) for course in courses for teacher in course.teachers]


def sort_teacher_course_pairs(pairs):
    return sorted(pairs, key=lambda pair: pair[1])


def get_course_teacher_counts(courses):
    return [(course.name, len(course.teachers)) for course in courses]


def sort_course_teacher_counts(counts):
    return sorted(counts, key=lambda pair: pair[1], reverse=True)