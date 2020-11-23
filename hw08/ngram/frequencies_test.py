from frequencies import NgramFrequencies


def test_ngram_frequencies():
    nf = NgramFrequencies(2)
    assert nf.add_item("He_is") == 1
    assert nf.add_item("He_is") == 2
    assert nf.add_item("He_is") == 3
    assert nf.add_item("I_am") == 1
    assert nf.add_item("I_am") == 2
    assert nf.add_item("I_am") == 3
    assert nf.add_item("I_am") == 4
    assert nf.add_item("I_am") == 5
    assert nf.add_item("I_am") == 6
    assert nf.add_item("They_are") == 1

    assert nf.frequency("They_are") == 0.1

    assert nf.top_n_counts() == [("I_am", 6), ("He_is", 3)]
    assert nf.top_n_freqs() == [("I_am", 0.6), ("He_is", 0.3)]
