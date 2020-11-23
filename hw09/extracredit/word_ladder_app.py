from word_ladder import WordLadder

ALPHABET_MAP = {"a": "bcdefghijklmnopqrstuvwxyz",
                "b": "cdefghijklmnopqrstuvwxyz",
                "c": "defghijklmnopqrstuvwxyz",
                "d": "efghijklmnopqrstuvwxyz",
                "e": "fghijklmnopqrstuvwxyz",
                "f": "ghijklmnopqrstuvwxyz",
                "g": "hijklmnopqrstuvwxyz",
                "h": "ijklmnopqrstuvwxyz",
                "i": "jklmnopqrstuvwxyz",
                "j": "klmnopqrstuvwxyz",
                "k": "lmnopqrstuvwxyz",
                "l": "mnopqrstuvwxyz",
                "m": "nopqrstuvwxyz",
                "n": "opqrstuvwxyz",
                "o": "pqrstuvwxyz",
                "p": "qrstuvwxyz",
                "q": "rstuvwxyz",
                "r": "stuvwxyz",
                "s": "tuvwxyz",
                "t": "uvwxyz",
                "u": "vwxyz",
                "v": "wxyz",
                "w": "xyz",
                "x": "yz",
                "y": "z",
                "z": ""}


def main():
    """Run an interactive command line to let the user
    input word pairs and generate word ladders"""
    english_words = load_words()

    adj_graph = build_adj_graph(english_words)

    while True:
        w1, w2 = input("> ").split()
        # Create a WordLadder object
        wl = WordLadder(w1, w2, adj_graph)
        # Generate the word ladder
        word_ladder = wl.make_ladder()
        print("Ladder: ", word_ladder)


def build_adj_graph(words):
    adj_graph = {}
    for w in words:
        adj_graph[w] = []
    cnt = 1
    N = len(words)
    for w in words:
        if not cnt % 1000 or cnt == N:
            print('{}/{}'.format(cnt, N))
        cnt += 1
        for i in range(len(w)):
            for c in ALPHABET_MAP[w[i]]:
                new_word = w[:i]+c+w[i+1:]
                if new_word in words:
                    adj_graph[w].append(new_word)
                    adj_graph[new_word].append(w)
        for i in range(len(w)):
            new_word = w[:i]+w[i+1:]
            if new_word in words:
                adj_graph[w].append(new_word)
                adj_graph[new_word].append(w)
    return adj_graph


def put(graph, w1, w2):
    if w1 in graph:
        graph[w1].append(w2)
    else:
        graph[w1] = [w2]


# Returns if w1 is one letter more than w2
def insert_one(w1, w2, length2):
    pad = 0
    for i in range(0, length2):
        j = i + pad
        while w1[i + pad] != w2[i]:
            pad += 1
            if pad > 1:
                return False
    return True


def edit_one(w1, w2, length):
    i = 0
    while w1[i] == w2[i]:
        i += 1
    i += 1
    while i < length and w1[i] == w2[i]:
        i += 1
    return i == length


def load_words():
    """Load words from complete wordlist file"""
    # We're creating a dictionary keyed on word
    # length, so that we can quickly get to a set of
    # words of a given length.
    valid_words = set()
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            valid_words.add(w)
    return valid_words


main()
