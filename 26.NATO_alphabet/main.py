
import pandas as pd
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_nato():
    try:
        word  = input("write a word: ")
        ls = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only Letters please")
        generate_nato()
    else:
        print(ls)

generate_nato()