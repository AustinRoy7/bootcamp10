class PrimeChecker(object):
  #creating class constructor that initializes number value
    def __init__(self, number = ""):
        self.number = number
  
  #creating is_prime function to test if number is prime
    def is_prime(self):
        if self.number == "":
            return False
        for i in range(2, int((int(self.number)**0.5) + 1)):
            if int(self.number) % i == 0:
                return False
        return True
