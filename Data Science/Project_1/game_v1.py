"""This game in which the PC guesses a number from 1 to 100
and predicts him by himself less than for 20 attempts.
As a result, we get the number from which attempt the PC guessed."""

from unittest import result
import numpy as np

def random_predict(number: int=1) -> int:
    """The function guesses a number from 1 to 100 less than for 20 attempts.
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: from what attempt РС guessed the number
    """
    
    count = 0   #count - attempts counter
    a = 1     #lower bound of a random number  
    b = 101     #upper bound of a random number
    PC_predict = np.random.randint(a,b)
   
    while True:
        count += 1
        
        if number > PC_predict:
            a = PC_predict + 1
            PC_predict = np.random.randint(a,b)
        elif number < PC_predict:
            b = PC_predict
            PC_predict = np.random.randint(a,b)
        else:
            break #Exit of cycle if PC guessed the correct answer.
            
    return count    #return from what attempts PC guessed the number

#print(random_predict(np.random.randint(1,101)))
    
def predict_score(random_predict) ->int: 
    
    """Functions of 1000 different numbers, determines the average
    value of attempts when guessing a number from 1 to 100.
    Args:
        random_predict (func): the function of checking the quality
    Returns:
        int: The number of guessing attempts on average.
    """
    
    count_ls = []   #list of attempts
    numbers_ls = np.random.randint(1, 100, size=1000)  
    
    for number in numbers_ls:
        count_ls.append(random_predict(number))
    
    result = int(np.mean(count_ls))   #find average result of list    
    print(f'Average result of predict number is {result}')
    
    return result #average result of attempts

#RUN
if __name__ == '__main__':
    predict_score(random_predict)
