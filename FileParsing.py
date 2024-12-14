'''
Написать программу, которая находит самое длинное слово в файле.
В качестве результата выводится на экран длина самого длинного слова и
все слова такой длины
'''

# Принимаются все символы, кроме пробелов

def finding_longest_word_in_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        words = content.split()
        longest_word = max(words, key = len)
        longest_word_length = len(longest_word)
        longest_words = []
        for word in words:
            if len(word) == longest_word_length:
                longest_words.append(word)
    
    return longest_word_length, longest_words

file_path = input("Enter the file path: ")
word_length, longest_words = finding_longest_word_in_file(file_path)

print("The length of the longest word(s) is: ", word_length)
print("The longest words are: ", longest_words)
