import unittest
import RK2_BKIT

class RK_Test(unittest.TestCase):
    def test_E1(self):
        self.assertEqual(RK2_BKIT.E1(), [('компьютер HP', 'Samsung'), ('компьютер HP', 'WD gold'), ('компьютер MSI', 'Seagate'), ('компьютер Alienware', 'Toshiba'), ('компьютер Alienware', 'Seagate Baracuda'), ('компьютер Asus', 'WD blue'), ('компьютер Asus', 'Toshiba')])
    def test_E2(self):    
        self.assertEqual(RK2_BKIT.E2(), [('MacBook Air', 512.0), ('MacBook Pro', 1024.0), ('компьютер HP', 2048.0), ('компьютер Alienware', 3584.0), ('компьютер Asus', 4096.0), ('компьютер MSI', 5120.0)])
    def test_E3(self):    
        self.assertEqual(RK2_BKIT.E3(), [('Seagate', 'компьютер HP'), ('Samsung', 'компьютер HP'), ('Seagate Baracuda', 'компьютер HP'), ('Seagate', 'компьютер MSI'), ('Seagate', 'компьютер Alienware'), ('Samsung', 'компьютер Asus')]) 
if __name__ == '__main__':
    unittest.main()