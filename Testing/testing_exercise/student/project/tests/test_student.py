import unittest
from Testing.testing_exercise.student.project.project.student import Student
# from project.student import Student


class StudentTests(unittest.TestCase):
    def setUp(self):
        name = "Peter"
        courses = None
        self.student = Student(name, courses)

    def test_init(self):
        self.assertEqual(self.student.name, "Peter")
        self.assertEqual(self.student.courses, {})

    def test_enroll_update_notes_when_course_existing(self):
        self.student.courses = {"MathForDevs": []}
        enroll_course = self.student.enroll("MathForDevs", ["Basic Algebra", "Linear Algebra", "Vectors"], "Math")
        self.assertEqual(enroll_course, "Course already added. Notes have been updated.")

    def test_enroll_add_course_and_notes_when_course_note_is_Y(self):
        enroll_course = self.student.enroll("DataScience", ["Statistics", "Combinatorics", "Hypothesis"], "Y")
        self.assertEqual(enroll_course, "Course and course notes have been added.")

    def test_enroll_add_course_and_notes_when_course_note_is_EmptyString(self):
        enroll_course = self.student.enroll("ML", ["Sentiment Analysis", "Abnormalities Detection"], "")
        self.assertEqual(enroll_course, "Course and course notes have been added.")

    def test_enroll_add_new_course(self):
        enroll_course = self.student.enroll("AI", ["TensorFlow.", "PyTorch", "Scikit Learn"], "AI")
        self.assertEqual(self.student.courses, {"AI": []})
        self.assertEqual(enroll_course, "Course has been added.")

    def test_add_notes_when_course_existing(self):
        self.student.courses = {"MathForDevs": []}
        notes_for_add = self.student.add_notes("MathForDevs", ["Calculus", "Statistics", "High School Math"])
        self.assertEqual(notes_for_add, "Notes have been updated")

    def test_add_notes_when_course_not_existing(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("MathForDevs", ["Calculus", "Statistics", "High School Mat"])
        expected_msg = str(context.exception)
        actual_msg = "Cannot add notes. Course not found."
        self.assertEqual(expected_msg, actual_msg)

    def test_leave_courses_when_course_existing(self):
        self.student.courses = {"MathForDevs": []}
        course_for_leaving = self.student.leave_course("MathForDevs")
        self.assertEqual(course_for_leaving, "Course has been removed")

    def test_leave_courses_when_course_not_existing(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("MathForDevs")
        expected_msg = str(context.exception)
        actual_msg = "Cannot remove course. Course not found."
        self.assertEqual(expected_msg, actual_msg)


if __name__ == "__main__":
    unittest.main()
