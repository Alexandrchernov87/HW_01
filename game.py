"""Компьютер загадывает целое число от 1 до 100"""
import numpy as np
def random_predict(number:int=1) -> int:
    """Угадываем число загаданное компьютером, используя информацию 
    больше или меньше случайное число нужного нам числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 1
    max = 100
    predict_number = (min + max) / 2
     
    while number != predict_number:
        count += 1
        # Сужаем зону поиска
        if number > predict_number: 
            min = predict_number + 1.5   
        elif number < predict_number: 
            max = predict_number - 1.5    
        predict_number = round((max + min ) / 2)
        
    return(count)

print(f'Количество попыток:{random_predict()}')
random_predict(10)
         
