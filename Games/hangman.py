import random

def getWord():
    line = random.randint(0,999)
    f = open('dictionary')
    file = f.readlines()
    word = file[line]
    return word

def find(word, letter, guessedWord):
    match = False
    for i in range(len(word)):
        if (word[i] == letter):
            match = True
            guessedWord = guessedWord[:i] + letter + guessedWord[i+1:]
    if (match == False):
        print('No Match Found!')
    return guessedWord

def win(guessedWord):
    nodash = True
    for i in range(len(guessedWord)):
        if (guessedWord[i] == '-'):
            nodash = False           
    return nodash

print('Welcome to the Hangman.')
word = getWord()
word = word.upper()
length = len(word) - 1
guessedWord = ''
for x in range(length):
    guessedWord = guessedWord + '-'

for x in range(length*2):
    print(guessedWord)
    letter = input('Guess a letter: ')
    letter = letter.upper()
    guessedWord = find(word, letter, guessedWord)
    if win(guessedWord):
        print(word)
        print('You Win')
        break
    print('You have', (length*2)-x-1, 'tries left')
    if (x == length*2-1):
        print(word)
