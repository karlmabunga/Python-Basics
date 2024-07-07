import random
def hangman():
    word = random.choice(['cranium', 'catan', 'sequence', 'batman', 'superman', 'thor', 'rome', 'canada', 'ireland'])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while True:
        main = ''
        missed = 0

        for c in word:
            if c in guessmade:
                main += c
            else:
                main += '_'
        if main == word:
            print(main)
            print("You've won!")
            break

        print('Guess the word: ', main)
        guess = input()

        if guess in validLetters:
            guessmade += guess
        else:
            print('Wrong choice')
            print('Enter a valid character')
            guess = input()
        
        if guess not in word:
            turns -= 1
            if turns == 9:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('       0        ')
            if turns == 8:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('       0        ')
                print('       |        ')
            if turns == 7:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('       0        ')
                print('       |        ')
                print('      /         ')
            if turns == 6:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('       0        ')
                print('       |        ')
                print('      / \       ')
            if turns == 5:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('       0        ')
                print('       |        ')
                print('      / \       ')
            if turns == 5:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('       0        ')
                print('       |        ')
                print('     _/ \       ')
            if turns == 4:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('       0        ')
                print('       |        ')
                print('     _/ \_      ')
            if turns == 3:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('     \ 0        ')
                print('       |        ')
                print('     _/ \_      ')
            if turns == 2:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('     \ 0 /      ')
                print('       |        ')
                print('     _/ \_      ')
            if turns == 2:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('     \ 0 | /    ')
                print('       |        ')
                print('     _/ \_      ')
            if turns == 1:
                print('%s turns left' %turns)
                print('  ------------  ')
                print('     \ 0_| /    ')
                print('       |        ')
                print('     _/ \_      ')
            if turns == 0:
                print("You've lost")
                print('  ------------  ')
                print('       ø/      ')
                print('      /|\      ')
                print('      / \      ')

name = input('Enter your name: ')
print('Welcome ', name)
print('--------------------------')
print('Try to guess the word in less that 10 attempts')
hangman()
print()