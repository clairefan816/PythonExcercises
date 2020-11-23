from prime_generator import PrimeGenerator

TEST_NUMBER = 10000


def main():

    pl = PrimeGenerator(TEST_NUMBER)
    primes = pl.primes_to_max()
    print(primes)


main()
