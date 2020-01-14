
import random

number=random.randint(0,101)
while True:
    answer=input("Введите число: ")
    if not answer or answer == "exit":
        break
        if not answer.isdigit():
            print ("введите правильное число")
            continue
    user_answer = int(answer)
    if user_answer>number:
        print ("Загаданное число меньше less")
    elif user_answer<number:
        print ("Загаданное число больше more")
    else:
        print ("Вы угадали Got It")
        break