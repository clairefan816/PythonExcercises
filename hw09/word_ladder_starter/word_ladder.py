from queue import Queue
from stack import Stack

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist

    def make_ladder(self):
        if len(self.w1) != len(self.w2):
            return None
        self.word_q = Queue()
        word_s = Stack()
        word_s.push(self.w1)
        self.word_q.enqueue(word_s)
        self.review_set = set()

        while True:
            if not self.word_q.isEmpty():
                ladder = self.word_q.dequeue()
                top_word = ladder.peek()
                for i in range(len(top_word)):
                    for c in ALPHABET:
                        if c == top_word[i]:
                            continue
                        new_word = top_word[:i]+c+top_word[i+1:]
                        if new_word in self.review_set:
                            continue
                        else:
                            self.review_set.add(new_word)
                            if new_word in self.wordlist:
                                new_ladder = ladder.copy()
                                new_ladder.push(new_word)
                                if new_word == self.w2:
                                    return new_ladder
                                else:
                                    self.word_q.enqueue(new_ladder)
            else:
                return None
