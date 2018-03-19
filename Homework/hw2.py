"""
Tammy Metz
3-11-18
ITP 195
Homework 2
Reads word.txt, finds the total number of words, gets the 10th line's word,
calculates how many words start with a capital letter,
counts the vowels of each word, adds extra words at the end of the output file,
writes a new file (output.txt) with the words that end with a vowel
"""


def main():
    words = []
    output_words = []
    vowels = ("a","e","i","o","u")
    capital_count = 0
    input_file = input("Please enter the name of the text fie to read: ")
    word_file = open(input_file, "r")
    for line in word_file:
        vowel_count = 0
        cur_word = line.strip()
        words.append(cur_word)
        for char in cur_word.lower():
            if char in vowels:
                vowel_count += 1
        print("{} has {} vowels".format(cur_word, vowel_count))
        if cur_word[0].isupper():
            capital_count += 1
        if cur_word.lower()[-1] in vowels:
            output_words.append(line)
    print("The total number of words is: {}".format(len(words)))
    print("The 10th line's word is: {}".format(words[9]))
    print("{} words start with a capital letter".format(capital_count))
    word_file.close()

    print ("Writing output file.")
    output_file = open("output.txt","w")
    output_file.writelines(output_words)
    output_file.write("\n\n")
    output_file.write("Spring\n")
    output_file.write("Break\n")
    output_file.write("is\n")
    output_file.write("here\n")
    output_file.close()
    

if __name__ == "__main__":
    main()

