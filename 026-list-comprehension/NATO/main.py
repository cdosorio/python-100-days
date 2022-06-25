import pandas


#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
df_nato = pandas.read_csv("nato_phonetic_alphabet.csv")
#dict_nato = {row[0]: row[1] for row in df_nato.values}
dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}  # DICT Comprehension
#print(dict_nato)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_word = input("Enter a word...\n").upper()
    try:        
        list_nato = [ dict_nato[letter] for letter in user_word ]        
    except KeyError:
        print('Please only letters')
        generate_phonetic()
    else:
        print(list_nato)


generate_phonetic()
