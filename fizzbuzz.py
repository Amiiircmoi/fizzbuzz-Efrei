def fizzbuzz(n):
    """
    Renvoie la chaîne correspondant à la valeur FizzBuzz pour le nombre n selon les règles suivantes :
      - Ajoute "Fizz" si n est divisible par 3.
      - Ajoute "Fizz" si n contient le chiffre 3.
      - Ajoute "Buzz" si n est divisible par 5.
      - Ajoute "Buzz" si n contient le chiffre 5.
    Si aucune de ces conditions n'est remplie, renvoie n sous forme de chaîne.
    """
    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if "3" in str(n):
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    if "5" in str(n):
        result += "Buzz"
    return result if result else str(n)
