import unittest
import runner_and_tournament as runner_and_tournament
from pprint import pprint

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)


    def test_tournament1(self):
        tour1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    def test_tournament2(self):
        tour1 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    def test_tournament3(self):
        tour1 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[3] == 'Ник')

    def test_tournament4(self):
        tour1 = runner_and_tournament.Tournament(150, self.runner2, self.runner1, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[3] == 'Ник')

    def test_tournament4(self):
        tour1 = runner_and_tournament.Tournament(8, self.runner2, self.runner3)
        TournamentTest.all_results = tour1.start()
        self.assertTrue(TournamentTest.all_results[2] == 'Ник')

    def tearDown(self):
        # print(TournamentTest.all_results.items())
        for key, value in TournamentTest.all_results.items():
            print(key, value, ' ', end='')
        print()



if __name__ == '__main__':
    unittest.main()
