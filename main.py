import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_list = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_list["A"])

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
letters = [letter for letter in word]

# My method
nato_segment = []
result = [nato_segment.append(value) for letter in letters for (key, value) in nato_list.items() if letter == key]
print(nato_segment)

# Instructors method
output = [nato_list[letter] for letter in word]
print(result)


