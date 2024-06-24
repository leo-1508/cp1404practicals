"""
Time estimate: 30 minutes
"""


def count_word_occurrences(text):

    words = text.split()


    word_counts = {}


    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def print_sorted_word_counts(word_counts):

    max_word_length = max(len(word) for word in word_counts)


    sorted_words = sorted(word_counts.items())


    for word, count in sorted_words:
        print(f"{word:{max_word_length}} : {count}")


def main():

    text = input("Text: ")


    word_counts = count_word_occurrences(text)


    print_sorted_word_counts(word_counts)


if __name__ == "__main__":
    main()
