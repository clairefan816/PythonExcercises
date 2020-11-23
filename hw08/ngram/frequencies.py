class NgramFrequencies:
    def __init__(self, N):
        self.N = N
        self.map = {}
        self.total = 0

    def add_item(self, item):
        self.total += 1
        self.map[item] = 1 if item not in self.map else self.map[item] + 1
        return self.map[item]

    def top_n_counts(self):
        return sorted(
            self.map.items(), key=lambda x: x[1], reverse=True)[0:self.N]

    def frequency(self, item):
        return self.map[item] / self.total

    def top_n_freqs(self):
        return [(x[0], self.frequency(x[0])) for x in self.top_n_counts()]
