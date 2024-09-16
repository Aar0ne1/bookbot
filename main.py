def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    count = len(words)
    return count

def letter_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    letters = {}
    lower_case = file_contents.lower()
    for i in lower_case:
        if i.isalpha():
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
    return letters

def report():
    dictionary = letter_count()
    newlist = list(dictionary.items())
    return sorted(newlist, key=lambda item: item[1], reverse=True)
    
def main():
    total_words = word_count()
    frequency_of_letters = report()
    print(f"Total word count: {total_words}")
    for letter, count in frequency_of_letters:
        print(f"The '{letter}' character was found {count} times")
    

if __name__ == "__main__":
    main()

