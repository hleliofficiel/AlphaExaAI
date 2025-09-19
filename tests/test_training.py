import unittest
import src.train as train

class TestTraining(unittest.TestCase):
    def test_main_runs(self):
        try:
            train.main()
            success = True
        except Exception as e:
            success = False
        self.assertTrue(success)

if __name__ == "__main__":
    unittest.main()
