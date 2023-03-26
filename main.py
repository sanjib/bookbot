def count_words(s):
    words = s.split()
    return len(words)


def count_letters(s):
    count = {}
    for i in range(97, 123):
        count[chr(i)] = 0
    for letter in s:
        if ord("A") <= ord(letter) <= ord("Z"):
            letter = letter.lower()
        if ord('a') <= ord(letter) <= ord('z'):
            count[letter] += 1
    return count


def print_report(path, word_count, letter_count):
    print(f"-- Begin report of {path} --")
    print(f"Total words: {word_count}")
    print("Letter count:")
    for c in letter_count:
        print("  {}: {:>7}".format(c, letter_count[c]))
    print("-- End report --")


def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        content = f.read()
        print_report(path, count_words(content), count_letters(content))


main()
