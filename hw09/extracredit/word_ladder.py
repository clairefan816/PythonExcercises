from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    # TODO:
    # Implement whatever functionality is necessary to generate a
    # stack representing the word ladder based on the parameters
    # passed to the constructor.
    def __init__(self, w1, w2, adj_graph):
        self.w1 = w1
        self.w2 = w2
        self.adj_graph = adj_graph

    def make_ladder(self):
        self.word_q = Queue()
        word_s = Stack()
        word_s.push(self.w1)
        self.word_q.enqueue(word_s)
        self.review_set = set()

        while True:
            if not self.word_q.isEmpty():
                ladder = self.word_q.dequeue()
                top_word = ladder.peek()
                for new_word in self.adj_graph[top_word] if top_word in self.adj_graph else []:
                    if new_word in self.review_set:
                        continue
                    else:
                        self.review_set.add(new_word)
                        new_ladder = ladder.copy()
                        new_ladder.push(new_word)
                        if new_word == self.w2:
                            return new_ladder
                        else:
                            self.word_q.enqueue(new_ladder)
            else:
                return None
