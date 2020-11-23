from text_cleaner import TextCleaner
from frequencies import NgramFrequencies


def main(filename):
    tc = TextCleaner("corpse_bride.txt")
    list_of_sentences = tc.read_file()

    RANK = 10

    unigram = NgramFrequencies(RANK)
    bigram = NgramFrequencies(RANK)
    trigram = NgramFrequencies(RANK)

    for sentence in list_of_sentences:
        words = sentence.split()
        for i in range(len(words)):
            unigram.add_item(words[i])
            if i < len(words) - 1:
                bigram.add_item(words[i] + "_" + words[i+1])
            if i < len(words) - 2:
                trigram.add_item(
                    words[i] + "_" + words[i+1] + "_" + words[i+2])

    print("Top 10 unigrams:")
    print(unigram.top_n_freqs())
    print("Top 10 bigrams:")
    print(bigram.top_n_freqs())
    print("Top 10 trigrams:")
    print(trigram.top_n_freqs())


main()
