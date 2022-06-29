morse = {    
    "A":".-"	,"B":"-...",
    "C":"-.-."	,"D":"-..",
    "E":"."	    ,"F":"..-.",
    "G":"--."	,"H":"....",
    "I":".."	,"J":".---",
    "K":"-.-"	,"L":".-..",
    "M":"--"	,"N":"-.",
    "O":"---"	,"P":".--.",
    "Q":"--.-"	,"R":".-.",
    "S":"..."	,"T":"-",
    "U":"..-"	,"V":"...-",
    "W":".--"	,"X":"-..-",
    "Y":"-.--"	,"Z":"--..",
    "0":"-----"	,"1":".----",
    "2":"..---"	,"3":"...--",
    "4":"....-"	,"5":".....",
    "6":"-...."	,"7":"--...",
    "8":"---.."	,"9":"----.",
    ", ":"--..--", ".":".-.-.-",
    "?":"..--..", "/":"-..-.", 
    "-":"-....-", "(":"-.--.", 
    ")":"-.--.-"
}

# word = input("Please indicate word to translate to morse... ").upper()
# new_word = ""

# for c in word:
#     new_word += morse[c]

#print(f"Morse: {new_word}")

def generate_phonetic():
    user_word = input("Enter a word...\n").upper()
    try:        
        list_morse = [ morse[letter] for letter in user_word ]   # list comprehension     
    except KeyError:
        print('Character not found')
        generate_phonetic()
    else:
        print(''.join(list_morse))


generate_phonetic()