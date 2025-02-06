import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_valeur_1(self):
        # Pour 1, aucune règle ne s'applique, on doit obtenir "1"
        self.assertEqual(fizzbuzz(1), "1")

    def test_valeur_3(self):
        # Pour 3, il est divisible par 3 ET contient le chiffre 3 :
        # On attend "Fizz" (divisible par 3) + "Fizz" (contient le 3) = "FizzFizz"
        self.assertEqual(fizzbuzz(3), "FizzFizz")

    def test_valeur_5(self):
        # Pour 5, il est divisible par 5 ET contient le chiffre 5 :
        # On attend "Buzz" (divisible par 5) + "Buzz" (contient le 5) = "BuzzBuzz"
        self.assertEqual(fizzbuzz(5), "BuzzBuzz")

    def test_valeur_15(self):
        # Pour 15, il est divisible par 3 et par 5, et contient le chiffre 5 (mais pas 3) :
        # On attend "Fizz" (divisible par 3) + "Buzz" (divisible par 5) + "Buzz" (contient le 5) = "FizzBuzzBuzz"
        self.assertEqual(fizzbuzz(15), "FizzBuzzBuzz")
    
    def test_intentional_failure(self):
        # Ce test est volontairement erroné pour vérifier que l'échec des tests bloque le merge.
        self.fail("Test échoué délibérément")


if __name__ == '__main__':
    unittest.main()
