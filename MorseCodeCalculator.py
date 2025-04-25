#Morse Code Dictionary
morse_code = {     'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
    'e': '.',  'f': '..-.', 'g': '--.',  'h': '....',
    'i': '..', 'j': '.---', 'k': '-.-',  'l': '.-..',
    'm': '--', 'n': '-.',   'o': '---',  'p': '.--.',
    'q': '--.-','r': '.-.', 's': '...',  't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--','z': '--..', '0': '-----', '1': '.----',
    '2': '..---','3': '...--','4': '....-','5': '.....',
    '6': '-....','7': '--...','8': '---..','9': '----.',
    ' ': '/'  # space between words in Morse
}

text = input("Input Phrase to be Converted: ").lower()
morse_result = ' '
for char in text:
    if char in morse_code:
        morse_result += morse_code[char] + ' '
    else:
       morse_result += '? '

print("Morse code: " + morse_result)