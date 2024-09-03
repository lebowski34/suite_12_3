import unittest
from tests_12_3 import RunnerTest, TournamentTest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTest))
    suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TournamentTest))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
