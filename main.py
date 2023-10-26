#Splits text into words based on whitespace and returns number of words
def count(file_contents):
    words = file_contents.split()
    return len(words)
#Splits text into letters and counts occurance of each letter.
def char_occurance(file_contents):
    file_contents = file_contents
    char_oc = None
    int_oc = None
    occurance_dict = {}
    for character in file_contents:
        char = character.lower()
        if char in occurance_dict:
            occurance_dict[char] += 1

        elif char not in occurance_dict:
            occurance_dict[char] = 1
    print(occurance_dict)
    return occurance_dict

#Sort directory alphabetically and print character occurences.
def report(occurance_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    for letter in sorted(occurance_dict):
        if letter.isalpha() == True:
            print(f"the {letter} character was found {occurance_dict[letter]} times")
        else:
            pass
    print("--- End of Report ---")



#With frankenstein's textfile as input, store the text, count the words
#and occurance of letters.
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = count(file_contents)
    print(words)
    occurance_dict = char_occurance(file_contents)
    report(occurance_dict)