import random


answer = random.randint(1,100)
print('DEBUG MODE has activated:: answer: ', answer)
guess = int(input('Guess the number(1-100): '))
if guess-answer == 0:
    print('That is correct! The answer was {}'.format(answer))
else:
    print('WRONG Answer, stupid! The answer was {}.'.format(answer))
