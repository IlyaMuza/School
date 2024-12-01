import runner2
import unittest
import tests_12_3

testST = unittest.TestSuite()
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runers = unittest.TextTestRunner(verbosity=2)
runers.run(testST)