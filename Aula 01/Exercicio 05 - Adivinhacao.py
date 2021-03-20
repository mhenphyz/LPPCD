# Exercicio 05 - Slide 40

from random import randint

low = 0
high = 10

random_number = randint(low, high)

while True:
    try:
        user_guess = int(input(f'Escolha um número de {low} a {high}\n'))
        
        if (user_guess == random_number):
            print('ok você acertou')
        
        elif (user_guess < random_number):
            print('Você errou para menos')
            
        else:
            print('Você errou para mais')
        
        print(f'O número gerado foi {random_number}')
        break
    except ValueError:
        print('Favor inserir um número inteiro')