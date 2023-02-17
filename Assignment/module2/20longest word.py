def main():
    text = input("Please input a list of words to evaluate: ")

    longest = 0

    for words in text.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words

    print("The longest word is", longest_word, "with length", len(longest_word))

main() 