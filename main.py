import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_list = {row.letter: row.code for (index, row) in data.iterrows()}

# My method
# word = input("Enter a word: ").upper()
# while True:
#     try:
#         output = [nato_list[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         word = input("Enter a word: ").upper()
#         if word.isalpha():
#             output = [nato_list[letter] for letter in word]
#             print(output)
#             break
#         else:
#             continue
#     else:
#         print(output)
#         break


# Instructors method
# Does the same, but a lot shorter and 'smarter'
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [nato_list[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()