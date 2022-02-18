"""Находит ли программа нужное число меньше чем за 20 попыток"""
import numpy as np

def random_predict(number:int=1) -> int:
    
    count = 0
    min = 1
    max = 100
    predict_number = (min + max)/2
    
    while number != predict_number:
        count += 1
        if number > predict_number: 
            min = predict_number + 1.5   
        elif number < predict_number: 
            max = predict_number - 1.5
        predict_number = round((max + min )/2)
        
    return(count)

def score_game(random_predict) -> int:
    """За какое количество попыток  из 1000 подходов угадывается наш алгоритм 

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101,size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    return(count_ls)

print(score_game(random_predict))
