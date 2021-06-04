# Assignment 3.2
score = input('Enter the score between 0.0 and 1.0? ')

try:
    score = float(score)
except:
    print("Error, You've entered Non-numeric value." )
    quit()

if score < 0.0 or score > 1.0:
    print('You Entered wrong score It should be between 0.0 to 1.0.')
    quit()
elif score >= 0.0 and score < 0.6: print('F')
elif score >= 0.6 and score < 0.7: print('D')
elif score >= 0.7 and score < 0.8: print('C')
elif score >= 0.8 and score < 0.9: print('B')
else: print('A')