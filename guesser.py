import random

NUM_DIGITS = 1
MAX_GUESSES = 3

def getClues(guess, secretNum):

    if guess == secretNum:
        return 'Correct!'
        
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Bumba')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bungo'
        
    else:
        clues.sort()
        return ' '.join(clues)

def getSecretNum():

    numbers = list('0123456789')
    random.shuffle(numbers)
    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def main():
	print('''Guesser, a deductive logic game.
	
	I am thinking of a {}-digit number with no repeated digits.
	Try to guess what it is. Here are some clues:
	When I say:		That means:
	Bungo			One Digit is Correct but in the wrong position.
	Bumba			One digit is correct and in the right position.
	Hoopla			No digit is correct.
	
	For example, if the secret number was 248 and your guess was 843, the clues would be Bumba Bungo. '''.format(NUM_DIGITS))

while True:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print(' You have {} guesses to get it.'.format(MAX_GUESSES))
    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
        guess = ''
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print('Guess #{}: '.format(numGuesses))
            guess = input('> ')
        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1
        if guess == secretNum:
            break 
        if numGuesses > MAX_GUESSES:
            print('You ran out of guesses.')
            print('The answer was {}.'.format(secretNum))
    print('Do you want to play again? (yes or no)')
    if not input('> ').lower().startswith('y'):
        break
    print('Thanks for playing!')

if __name__ == '__name__':
    main()
