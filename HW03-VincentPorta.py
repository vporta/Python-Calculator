""" Created on Monday Sept 19 2017 

    @author: Vincent Porta

    Special Topics, Homework 03

        Implement a class for fractions that supports addition, subtraction, 
    multiplication, division, <, <=, !=, ==, >, and >=. 
"""
import unittest

class Fraction:
    """ A Fraction class calculator that prompts the user 
        for numeric input of two fractions and an operator, 
        and performs the appropriate mathematical operation. 
    """
    __slots__ = ['numerator', 'denominator']

    def __init__(self, numerator=0, denominator=1):
        """ Create new numerator and denominator"""
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator == 0: 
            raise(ValueError("Denominator cannot be 0"))


    def __add__(self, other):
        """ Return a Fraction with the sum of self """  
        
        greatest_common_denom = self.denominator * other.denominator
        fraction_one_numerator = self.numerator * other.denominator
        fraction_two_numerator = other.numerator * self.denominator
        sum_of_numerators = fraction_one_numerator + fraction_two_numerator
        # common = self.simplify(sum_of_numerators, greatest_common_denom)

        return Fraction(sum_of_numerators, greatest_common_denom)
        

    def __sub__(self, other):
        """ Return a Fraction with the difference of self """
        greatest_common_denom = self.denominator * other.denominator
        fraction_one_numerator = self.numerator * other.denominator
        fraction_two_numerator = other.numerator * self.denominator
        sum_of_numerators = fraction_one_numerator - fraction_two_numerator

        return Fraction(sum_of_numerators, greatest_common_denom)


    def __mul__(self, other):
        """ Return a Fraction with the product of self """  
        greatest_common_denom = self.denominator * other.denominator
        numerator = self.numerator * other.numerator

        return Fraction(numerator, greatest_common_denom)


    def __truediv__(self, other):
        """ Return a Fraction with the quotient of self """
        reciprocal = self.numerator * other.denominator
        greatest_common_denom = self.denominator * other.numerator

        return Fraction(reciprocal, greatest_common_denom) 


    def __eq__(self, other):
        """ Return True/False if the two fractions are equal """
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator

        return first_num == second_num


    def __ne__(self, other):
        """ Check if the fractions are not equal """
        first_num = self.numerator * other.denominator
        second_num = other.numerator * self.denominator

        return first_num != second_num


    def __lt__(self, other):
        """ Check if the fraction is less than """
        return (self.numerator/self.denominator) < (other.numerator/other.denominator)


    def __le__(self, other):
        """ Check if the fraction is less than or equal to """
        return (self.numerator/self.denominator) <= (other.numerator/other.denominator)


    def __gt__(self, other):
        """  Check if the fraction is greater than """
        return (self.numerator/self.denominator) > (other.numerator/other.denominator)


    def __ge__(self, other):
        """  Check if the fraction is greater than or equal to """
        return (self.numerator/self.denominator) >= (other.numerator/other.denominator)


    def __str__(self):
        """ Return a string to represent the Fraction """
        return str(self.numerator) +  '/' +  str(self.denominator)


    def operation_logic(self, fraction_one, fraction_two, operator):
        """ Performs arithmetic logic for each operator """
        if fraction_two == fraction_one:
            return print (fraction_one == fraction_two)
        elif operator == "+":
            return print(fraction_one + fraction_two)
        elif operator == "-":
            return print(fraction_one - fraction_two)
        elif operator == "*":
            return print(fraction_one * fraction_two)
        elif operator == "/":
            return print(fraction_one / fraction_two)
        elif operator == '!=':
            return print(fraction_one != fraction_two)
        elif operator == '<':
            return print(fraction_one < fraction_two)
        elif operator == '<=':
            return print(fraction_one <= fraction_two)
        elif operator == '>':
            return print(fraction_one > fraction_two)
        elif operator == '>=':
            return print(fraction_one >= fraction_two)
        else:
            return print("Invalid operator.")


    def simplify(self):
        """ Simplify the fraction by finding the greatest common factor """ 
        gcf = 1
        for i in range(min(abs(self.numerator), abs(self.denominator)), 1, -1):
            print(i)
            if self.numerator % i == 0 and self.denominator % i == 0:
                gcf = i
                num = int(self.numerator/gcf)
                denom = int(self.denominator/gcf)
                return Fraction(num, denom)
        return self


    def main(self):
        """ Ask the user for the first numerator and denominator,  
            the operator, and the second numerator and denominator, 
            then prints the result of applying the operator to the 
            two fractions """
        print("Welcome to the Fraction Calculator!") 
        
        try:
            numerator = int(input("Fraction 1 numerator: "))
            denominator = int(input("Fraction 1 denominator: "))

            operation_input = input("Operation (+, -, *, /, !=, ==, <, <=, >, >=): ")
            numerator_two = int(input("Fraction 2 numerator: "))
            denominator_two = int(input("Fraction 2 denominator: "))

            fraction_one = Fraction(numerator, denominator)
            fraction_two = Fraction(numerator_two, denominator_two)

            self.operation_logic(fraction_one, fraction_two, operation_input)

        except ValueError:
            return "Please enter a number."


class FractionTest(unittest.TestCase):
    def test_init(self):
        """ Verify that the numerator and denominator args are set properly """
        fraction = Fraction(3, 4)
        fraction_default_args = Fraction()

        self.assertIsInstance(fraction, Fraction)
        self.assertEqual(fraction.numerator, 3)
        self.assertEqual(fraction.denominator, 4)
        self.assertIsInstance(fraction_default_args, Fraction)
        self.assertEqual(fraction_default_args.numerator, 0)
        self.assertEqual(fraction_default_args.denominator, 1)


    def test_zero_denominator(self):
        """ Verify that an exception is raised when the denominator is 
            equal to 0
        """
        fraction = Fraction(1, 1)
        self.assertRaises(ValueError, Fraction.__init__, fraction, 1, 0)


    def test_str(self):
        """ Verify that __str__() works properly """
        fraction = Fraction(3, 4)

        self.assertEqual(str(fraction), '3/4')
    

    def test_eq(self):
        """ Test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        f4 = Fraction(3, 4)
        f5 = Fraction(123456782345, 1234567892343)
        f6 = Fraction(123456782345, 1234567892343)

        self.assertEqual(f1, f4)
        self.assertAlmostEqual(f5, f6)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 == f3)
        self.assertFalse(f1 == Fraction(3, 5))


    def test_plus(self):
        """ Test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)

        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))


    def test_subtract(self):
        """ Test fraction subtraction """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(-2, 3)
        f5 = Fraction(-2, -5)

        self.assertTrue((f1 - f1) == Fraction(0, 16))
        self.assertTrue((f1 - f2) == Fraction(1, 4))
        self.assertTrue((f1 - f3) == Fraction(5, 12))
        self.assertTrue((f1 - f4) == Fraction(17, 12))


    def test_divide(self):
        """ Test fraction divide """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(-2, 3)
        f5 = Fraction(-2, -5)

        self.assertTrue((f1 / f1) == Fraction(1, 1))
        self.assertTrue((f1 / f2) == Fraction(3, 2))
        self.assertTrue((f1 / f3) == Fraction(9, 4))


    def test_multiply(self):
        """ Test fraction multiply """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(-2, 3)
        f5 = Fraction(-2, -5)

        self.assertTrue((f1 * f1) == Fraction(9, 16))
        self.assertTrue((f1 * f2) == Fraction(3, 8))
        self.assertTrue((f1 * f3) == Fraction(1, 4))
        self.assertTrue((f1 * f4) == Fraction(-1, 2))


    def test_ne(self):
        """ Test fraction not equal """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(-2, 3)
        f5 = Fraction(-2, -5)
        f6 = Fraction(2, 3)

        self.assertNotEqual(f1, f4)
        self.assertNotEqual(f6, f4)
        self.assertFalse((f1 != f1) == True)
        self.assertTrue((f1 != f2) == True)
        self.assertTrue((f1 != f3) == True)
        self.assertTrue((f1 != f4) == True)


    def test_lt(self):
        """ Test fraction less than """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(2, 3)
        f5 = Fraction(-2, -5)

        self.assertLess(f3, f1)
        self.assertLess(f5, f1)
        self.assertFalse((f1 < f2) == True)
        self.assertFalse((f4 < f2) == True)
        self.assertTrue((f3 < f2) == True)
        self.assertTrue((f3 < f1) == True)
        self.assertTrue((f5 < f2) == True)


    def test_le(self):
        """ Test fraction less than or equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(3, 4)
        f5 = Fraction(-2, -5)

        self.assertLessEqual(f5, f1)
        self.assertLessEqual(f1, f4)
        self.assertLessEqual(f2, f4)


    def test_gt(self):
        """ Test fraction greater than """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        f4 = Fraction(0, 4)

        self.assertGreater(f1, f2)
        self.assertGreater(f1, f3)
        self.assertGreater(f1, f4)


    def test_ge(self):
        """ Test fraction greater than or equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)

        self.assertGreaterEqual(f1, f1)
        self.assertGreaterEqual(f1, f2)
        self.assertGreaterEqual(f1, f3)


    def test_operation_logic(self):
        """ Test for correct logic and operators """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 2)
        operators = { 
            'plus': '+',
            'minus': '-',
            'multiply': '*',
            'divide': '/',
            'equal': '==',
            'notequal': '!=',
            'lessthan': '<',
            'lessthan_equal': '<=',
            'greaterthan': '>',
            'greaterthan_equal': '>='
        }
        self.assertEqual(operators['plus'], '+')
        self.assertEqual(operators['minus'], '-')
        self.assertEqual(operators['multiply'], '*')
        self.assertEqual(operators['divide'], '/')
        self.assertEqual(operators['equal'], '==')
        self.assertEqual(operators['notequal'], '!=')
        self.assertEqual(operators['lessthan'], '<')
        self.assertEqual(operators['lessthan_equal'], '<=')
        self.assertEqual(operators['greaterthan'], '>')
        self.assertEqual(operators['greaterthan_equal'], '>=')


    def test_simplify(self):
        f1 = Fraction(10, 8).simplify()
        f2 = Fraction(20, 5).simplify()
        f3 = Fraction(9, 27).simplify()
        f4 = Fraction(-10, 20).simplify()
        f5 = Fraction(10, -20).simplify()
        f6 = Fraction(-10, -20).simplify()
        self.assertEqual(str(f1), '5/4')
        self.assertEqual(str(f2), '4/1')
        self.assertEqual(str(f3), '1/3')
        self.assertEqual(str(f4), '-1/2')
        self.assertEqual(str(f5), '1/-2')
        # self.assertEqual(str(f6), '1/2')


if   __name__ ==   '__main__':
    fraction = Fraction()
    unittest.main(exit=False, verbosity=2)
    # print(fraction.main())

