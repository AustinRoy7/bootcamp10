import unittest

from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_1(self):
        self.assertEqual(fizz_buzz(3), 'Fizz', msg='should return `Fizz` for number divisible by 3')
    
    def test_fizz_2(self):
        self.assertEqual(fizz_buzz(81), 'Fizz', msg='should return `Fizz` for number divisible by 3')
    
    def test_buzz_1(self):
        self.assertEqual(fizz_buzz(5), 'Buzz', msg='should return `Buzz` for number divisible by 5')
    
    def test_buzz_2(self):
        self.assertEqual(fizz_buzz(55), 'Buzz', msg='should return `Buzz` for number divisible by 5')

    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(75), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')
    
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(135), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')
        
    def test_indivisible_1(self):
        self.assertEqual(fizz_buzz(107), 107, msg='should return the number if its in divisible by neither 3 or 5')
        
    def test_indivisible_2(self):
        self.assertEqual(fizz_buzz(7), 7, msg='should return the number if its in divisible by neither 3 or 5')

    def test_fizz_3(self):
        self.assertEqual(fizz_buzz(99), 'Fizz', msg='should return `Fizz` for number divisible by 3')

    def test_fizz_buzz_3(self):
        self.assertEqual(fizz_buzz(150), 'FizzBuzz', msg='should return `FizzBuzz` for number divisible by 3 and 5')





if __name__ = '__main__':
	unittest.main()