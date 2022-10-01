import numpy as np
number = np.random.randint(1,100)
count = 0
while True:
    count +=1
    in_number = int(input("Try to guess the number from 1 to 100.\n"))
    if in_number > number:
        print("Number is less than your input. Let`s try again.")
    elif in_number < number:
        print("Number is bigger than your input. Let`s try again.")
    else:
        print("Congratulations!!! You guessed number!!!") 
        break  