import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")

    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    def test_run(self):
        self.assertTrue(True)

    def test_walk(self):
        self.assertFalse(False)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        if self.is_frozen:
            self.skipTest("Тесты в этом кейсе заморожены")

    def test_first_tournament(self):
        self.assertEqual("abc".upper(), "ABC")

    def test_second_tournament(self):
        self.assertIn(3, [1, 2, 3])

    def test_third_tournament(self):
        self.assertRaises(ValueError, int, "string")
