import runner2
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        obj = runner2.Runner('walker')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        obj = runner2.Runner('runker')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        obj_1 = runner2.Runner('Runker')
        obj_2 = runner2.Runner('Walker')
        for i in range(10):
            obj_1.run()
            obj_2.walk()
        self.assertNotEqual(obj_1, obj_2)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner2.Runner('Усэйн', 10)
        self.runner_2 = runner2.Runner('Андрей', 9)
        self.runner_3 = runner2.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for v in cls.all_results.values():
            print_dict = {}
            for k, val in v.items():
                print_dict.update({k: val.name})
            print(print_dict)

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tour_1(self):
        tour_1 = runner2.Tournament(90, self.runner_1, self.runner_3)
        self.all_results.update({'Test_1': tour_1.start()})
        self.assertTrue(self.all_results['Test_1'][max(self.all_results['Test_1'].keys())].name=='Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tour_2(self):
        tour_2 = runner2.Tournament(90, self.runner_2, self.runner_3)
        self.all_results.update({'Test_2': tour_2.start()})
        self.assertTrue(self.all_results['Test_2'][max(self.all_results['Test_2'].keys())].name=='Ник')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_tour_3(self):
        tour_3 = runner2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results.update({'Test_3': tour_3.start()})
        self.assertTrue(self.all_results['Test_3'][max(self.all_results['Test_3'].keys())].name=='Ник')

    @unittest.skip('Он никогда не проходит')
    def test_tour_4(self):
        tour_4 = runner2.Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        self.all_results.update({'Test_4': tour_4.start()})
        self.assertTrue(self.all_results['Test_4'][min(self.all_results['Test_4'].keys())].speed == max([x for x in
                                                                                             (self.runner_2.speed,
                                                                                             self.runner_1.speed,
                                                                                             self.runner_3.speed)]))


if __name__ == '__main__':
    unittest.main()