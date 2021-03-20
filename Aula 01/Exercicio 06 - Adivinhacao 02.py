# Exercicio 06 - Slide 42

from random import randint

low = 0
high = 100

random_number = randint(low, high)

attempts = 0

while True:
    try:
        user_guess = int(input(f'Escolha um número de {low} a {high}\n'))
        
        if (user_guess == random_number):
            print(f'muito bem acertou, em {attempts} tentativas!')
            break
        
        elif (user_guess < random_number):
            print('Você errou para menos, tente novamente')
            attempts += 1
            
        else:
            attempts += 1
            print('Você errou para mais, tente novamente')
        
    except ValueError:
        print('Favor inserir um número inteiro')