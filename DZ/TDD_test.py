import unittest
import main_DZ


class Test(unittest.TestCase):
    def TestBot1(self):
        self.assertEqual(main_DZ.chose_good(), "видеокарта")
        self.assertEqual(main_DZ.chose_dost(), "москва")
        self.assertEqual(main_DZ.chose_size(), "4гб")
        

if __name__ == "__main__":
    unittest.main()