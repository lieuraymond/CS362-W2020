from unittest import TestCase
import classroom_manager


class TestStudent(TestCase):
    def setUp(self):
        self.student_id = 1
        self.first_name = 'Raymond'
        self.last_name = 'Lieu'
        self.rl = classroom_manager.Student(self.student_id, self.first_name, self.last_name)
        self.assignment1 = classroom_manager.Assignment('assignment1', 17)
        self.assignment2 = classroom_manager.Assignment('assignment2', 19)

    def test_student(self):
        self.setUp()
        self.assertEqual(self.rl.last_name, self.last_name)
        self.assertEqual(self.rl.first_name, self.first_name)
        self.assertEqual(self.rl.id, self.student_id)

    def test_get_full_name(self):
            self.setUp()
            self.assertEqual(self.first_name + " " + self.last_name, self.rl.get_full_name())

    def test_submit_assignment(self):
        self.setUp()
        self.assertEqual([], self.rl.assignments)
        self.rl.submit_assignment(self.assignment1)
        self.assertEqual(self.assignment1, self.rl.assignments[0])
        self.rl.submit_assignment(self.assignment2)
        self.assertEqual(self.assignment2, self.rl.assignments[1])

    def test_get_assignments(self):
        self.setUp()
        self.assertEqual([], self.rl.get_assignments())
        self.rl.submit_assignment(self.assignment1)
        self.rl.submit_assignment(self.assignment2)
        rl_assignments = [self.assignment1, self.assignment2]
        self.assertEqual(rl_assignments, self.rl.get_assignments())

    def test_get_assignment(self):
        self.setUp()
        self.assertEqual(None, self.rl.get_assignment('assignment1'))
        self.rl.submit_assignment(self.assignment1)
        self.assertEqual(self.assignment1, self.rl.get_assignment('assignment1'))
        self.assertEqual(None, self.rl.get_assignment('assignment2'))


    def test_get_average(self):
        self.setUp()
        self.assertEqual([], self.rl.get_assignments())
        self.assignment1.assign_grade(14)
        self.assignment2.assign_grade(16)
        self.rl.submit_assignment(self.assignment1)
        self.rl.submit_assignment(self.assignment2)
        self.assertEqual(15, self.rl.get_average())

    def test_remove_assignment(self):
        self.setUp()
        self.assertEqual(None, self.rl.get_assignment('assignment1'))
        self.rl.submit_assignment(self.assignment1)
        self.assertEqual(self.assignment1, self.rl.get_assignment('assignment1'))
        self.rl.remove_assignment('assignment1')
        self.assertEqual(None, self.rl.get_assignment('assignment1'))

class TestAssignment(TestCase):
    def setUp(self):
        self.max_score = 11
        self.name = 'assignment7'
        self.assignment7 = classroom_manager.Assignment(self.name, self.max_score)

    def test_assignment(self):
        self.setUp()
        self.assertEqual(self.assignment7.name, self.name)
        self.assertEqual(self.assignment7.max_score, self.max_score)
        self.assertEqual(self.assignment7.grade, -1)

    def test_assign_grade(self):
        self.setUp()
        self.assertEqual(self.assignment7.grade, -1)
        self.assignment7.assign_grade(9)
        self.assertEqual(self.assignment7.grade, 9)
        self.assignment7.assign_grade(12)
        self.assertEqual(-1, self.assignment7.grade)
