from list_primes import PrimeGenerator


def test_primes_to_max():
    pg = PrimeGenerator(10)
    prime_list = pg.primes_to_max()
    assert prime_list == [2, 3, 5, 7]

    pg = PrimeGenerator(20)
    prime_list = pg.primes_to_max()
    assert prime_list == [2, 3, 5, 7, 11, 13, 17, 19]
