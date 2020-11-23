from math import sqrt as s


class PrimeGenerator:
    def __init__(self, num):
        self.num = num

    def primes_to_max(self):
        mark_set = set()
        prime_list = []
        for v in range(2, self.num+1):
            if v not in mark_set:
                prime_list.append(v)
            if v <= s(self.num):
                time = 2
                while v * time <= self.num:
                    mark_set.add(v * time)
                    time += 1
        return prime_list
