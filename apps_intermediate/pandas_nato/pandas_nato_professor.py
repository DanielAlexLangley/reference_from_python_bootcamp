
# TO DO 1. Create a dictionary in this format:
# TO DO 2. Create a list of the phonetic code words from a word that the user inputs.
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("pandas_nato_phonetic.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
