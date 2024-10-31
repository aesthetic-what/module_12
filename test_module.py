import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        mod = runner.Runner('Timur')
        for _ in range(10):
            mod.walk()
        self.assertEqual(mod.distance, 50)

    def test_run(self):
        mod = runner.Runner('Timur')
        for _ in range(10):
            mod.run()
        self.assertEqual(mod.distance, 100)

    def test_challenge(self):
        mod_1 = runner.Runner('Timur')
        mod_2 = runner.Runner('Denis')
        for _ in range(10):
            mod_1.walk()
            mod_2.run()
        self.assertNotEqual(mod_1.distance, mod_2.distance)


if __name__ == '__main__':
    unittest.main()
