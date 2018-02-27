answer = 'Ostrich'

while 1 == 1:
    print('Thinking of an Animal')
    print("Why not take a guess? You've got nothing better to do.")
    guess = input()
    if guess.lower() == answer.lower():
        print('Whoop. Dee. Doo. You got it.')
        break
    elif guess == 'quit':
        print('Sorry to see you go...')
        break
    else:
        print('Try again')
