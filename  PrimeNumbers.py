class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def is_prime(num: int):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def generate_primes(self):
        primes = []
        for num in range(self.start, self.end + 1):
            if self.is_prime(num):
                primes.append(num)
        return primes


prime_generator = PrimeNumbers(1, 100)
prime_list = prime_generator.generate_primes()
print(prime_list)
