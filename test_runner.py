import unittest
import importlib

class TestAssignmentFour(unittest.TestCase):
    def test_01(self):
        self.assertFalse(answers.answer_01)
    def test_02(self):
        self.assertEqual(answers.answer_02, 4)
    def test_03(self):
        the_first_and_last_element = answers.answer_03([2, 3, 5, 7, 11])
        self.assertEqual(the_first_and_last_element[0], 2)
        self.assertEqual(the_first_and_last_element[1], 11)
        the_first_and_last_element = answers.answer_03([2, 3, 5])
        self.assertEqual(the_first_and_last_element[0], 2)
        self.assertEqual(the_first_and_last_element[1], 5)
        the_first_and_last_element = answers.answer_03(["Python", "Reticulate", "Anaconda"])
        self.assertEqual(the_first_and_last_element[0], "Python")
        self.assertEqual(the_first_and_last_element[1], "Anaconda")
        the_first_and_last_element = answers.answer_03(["Python", "Reticulate", "Anaconda", "Skywalker"])
        self.assertEqual(the_first_and_last_element[0], "Python")
        self.assertEqual(the_first_and_last_element[1], "Skywalker")
    def test_04(self):
        self.assertEqual(answers.answer_04([2, 3, 5, 7, 11]), [3, 5, 7])
        self.assertEqual(answers.answer_04(["Python", "Reticulate", "Anaconda"]), ["Reticulate"])
    def test_05(self):
        self.assertEqual(answers.answer_05("Python"), "Pyt")
        self.assertEqual(answers.answer_05("Reticulate"), "Ret")
        self.assertEqual(answers.answer_05("Anaconda"), "Ana")
        self.assertEqual(answers.answer_05("Skywalker"), "Sky")
        self.assertEqual(answers.answer_05("Anakin"), "Ana")
    def test_06(self):
        self.assertEqual(answers.answer_06([2, 3, 5]), 3)
        self.assertEqual(answers.answer_06([2, 3, 5, 7, 11]), 5)
        self.assertEqual(answers.answer_06([2, 3, 5, 7, 11, 13, 17]), 7)
        self.assertEqual(answers.answer_06([1, 2, 3]), 2)
        self.assertEqual(answers.answer_06([-1, 0, 1]), 0)
    def test_07(self):
        self.assertEqual(answers.answer_07("Steve"), "tev")
        self.assertEqual(answers.answer_07("Stark"), "tar")
        self.assertEqual(answers.answer_07("Natasha"), "tas")
        self.assertEqual(answers.answer_07("Skywalker"), "wal")
        self.assertEqual(answers.answer_07("Hawkeye"), "wke")
    def test_08(self):
        self.assertEqual(answers.answer_08("Taiwan"), {'alpha2': 'TW', 'alpha3': 'TWN'})
        self.assertEqual(answers.answer_08("Japan"), {'alpha2': 'JP', 'alpha3': 'JPN'})
        self.assertEqual(answers.answer_08("United States"), {'alpha2': 'US', 'alpha3': 'USA'})
        self.assertEqual(answers.answer_08("Czech Republic"), {'alpha2': 'CZ', 'alpha3': 'CZE'})
        self.assertEqual(answers.answer_08("Lithuania"), {'alpha2': 'LT', 'alpha3': 'LTU'})
        self.assertEqual(answers.answer_08("Slovakia"), {'alpha2': 'SK', 'alpha3': 'SVK'})
        self.assertEqual(answers.answer_08("Poland"), {'alpha2': 'PL', 'alpha3': 'POL'})
    def test_09(self):
        self.assertEqual(answers.answer_09([5, 5, 6, 6]), [5, 6])
        self.assertEqual(answers.answer_09([2, 2, 6, 6]), [2, 6])
        self.assertEqual(answers.answer_09([9, 9, 8, 1]), [1, 8, 9])
        self.assertEqual(answers.answer_09([7, 7, 4, 9]), [4, 7, 9])
    def test_10(self):
        self.assertEqual(answers.answer_10({5, 5, 6, 6}, {5, 6, 7, 8}), 2)
        self.assertEqual(answers.answer_10({1, 3, 5, 7, 9}, {2, 3, 5, 7}), 3)
        self.assertEqual(answers.answer_10({1, 3, 5, 7, 9}, {1, 3, 5, 7, 9}), 5)
        self.assertEqual(answers.answer_10({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}), 0)

chapter_name = "使用資料結構類別管理資料"
answers = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFour)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"您在「{chapter_name}」章節的 {number_of_test_runs} 道練習題中答對了 {number_of_successes} 題。")