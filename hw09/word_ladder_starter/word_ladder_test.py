from word_ladder import WordLadder

valid_words = {}
with open('words_alpha.txt') as word_file:
    for w in word_file.read().split():
        if len(w) in valid_words.keys():
            # Add to an existing set
            valid_words[len(w)].add(w)
        else:
            # Initialize a set with one element
            valid_words[len(w)] = {w}


def test_make_ladder():

    test_ladder1 = WordLadder('cat', 'hat', valid_words[3])
    test_ladder2 = WordLadder('love', 'hate', valid_words[4])
    test_ladder3 = WordLadder('angel', 'devil', valid_words[5])
    test_ladder4 = WordLadder('earth', 'ocean', valid_words[5])

    assert test_ladder1.make_ladder().size() == 2
    assert test_ladder2.make_ladder().size() == 4
    assert test_ladder3.make_ladder().size() == 8
    assert test_ladder4.make_ladder().size() == 14
