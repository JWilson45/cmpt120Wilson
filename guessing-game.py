answer = 'Ostrich'

while 1 == 1:
    print('Thinking of an Animal')
    print("Why not take a guess? You've got nothing better to do.")
    guess = input().lower()
    if guess[0] == 'q' or '':
        print('Sorry to see you go...')
        break
    elif guess == answer.lower():
        print('Whoop. Dee. Doo. You got it.')
        like = input('Do you like this animal? Y/N: ').lower()
        if like == 'y':
            print('Glad you like it! Did you know they are rideable?')
            break
        elif like == 'n':
            print("Try riding one, maybe it'll change your mind.")
            break
        else:
            break
    else:
        print('Try again')
        print('')
