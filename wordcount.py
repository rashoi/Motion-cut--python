def user_input():
    return input("Enter a number: ")


def process(text):
    import string
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words = text.split()
    return words


def counting(words):
    return len(words)


def main():
    text = user_input()
    words = process(text)
    word_count = counting(words)
    print(f"The number of words in the text is: {word_count}")


if __name__ == "__main__":
    main()
