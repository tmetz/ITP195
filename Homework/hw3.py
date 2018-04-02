"""
Tammy Metz
HW 3

Reads an input file, then prints the unique words to an output file.
Also prints a list of words that occur more than once, with their frequency.
"""

import string


def add_word(word, word_dict):
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1


def process_line(line, word_dict):
    # We could eliminate stop words by length, except that would also eliminate words like "he" and "go"
    stop_words = ["i", "is", "in", "the", "up", "a", "and", "if", "of", "are"]
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        word = word.lower()
        if word not in stop_words:
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_dict)


def pretty_print(word_dict):
    unique_words = []
    multi_words = []
    for key, val in word_dict.items():
        if val == 1:
            unique_words.append(key)
        else:
            multi_words.append((val, key))
    unique_words = sorted(unique_words) # Sort alphabetically
    multi_words = sorted(multi_words)  # Sort by frequency

    print("Printing results to output file.")
    output_file = open("output_hw3.txt", "w")
    output_file.write("List of unique words: \n")
    for word in unique_words:
        output_file.write(word)
        output_file.write(", ")
    output_file.write("\n\n")
    output_file.write("List of words that occur more than twice: \n")
    output_file.write("{:20s}{:20s} \n".format("Word", "Frequency"))
    for word_tup in multi_words:
        output_file.write("{:10s}{:11d}".format(word_tup[1], word_tup[0]))
        output_file.write("\n")
    output_file.close()


def main():
    word_dict = {}
    input_file = open("input_hw3.txt")
    for line in input_file:
        process_line(line, word_dict)
    pretty_print(word_dict)

if __name__ == "__main__":
    main()