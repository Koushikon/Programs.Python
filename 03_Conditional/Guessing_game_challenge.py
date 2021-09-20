from random import randint


def take_guess():
    num = int(input('[+] Take a guess? '))
    return num

# Check guess distance
def right_Guess(*args):
    '''
    args[0] = Pick number
    args[1] = Guess number
    args[2] = Max distance
    args[3] = WORM || WORMER
    args[4] = COLD ||COLDER
    '''
    distance = abs(args[0] - args[1])
    if args[0] == args[1]:
        return (True, 0)
    elif distance < args[2]:
        return (args[3], distance)
    else:
        return (args[4], distance)


def display(*args):
    '''
    args[0] = Result
    args[1] = Distance
    '''
    if args[0] == True:
        print('[#] You are correct ✔')
        exit()
    else:
        print(f'[#] {args[0]}, And the distance is {args[1]}')


guessList = [10]
previous_guess = 0

pick = randint(1, 100)
# print('Random picked number is', pick)

for _ in range(0,3):
    guess = take_guess()
    if guess < 1 or guess > 100:
        print('[#] Out of bounds?')
        continue
    if len(guessList) == 1:
        result, pos = right_Guess(pick, guess, guessList[previous_guess], 'WARM!', 'COLD!')
    else:
        result, pos = right_Guess(pick, guess, guessList[previous_guess], 'WARMER!', 'COLDER!')
    display(result, pos)
    guessList.append(pos)
    previous_guess += 1

print('= = = = = = = = = = = = = =\n\tGame Over!!\n= = = = = = = = = = = = = =')

