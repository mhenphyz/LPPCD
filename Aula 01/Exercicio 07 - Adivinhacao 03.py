from random import randint

low = 0 
high = 100

random_int = randint(low, high)

for i in range(5):
    user_guess = int(input(f'Tente adivinhar o número escolhido entre {low} e {high}\n'))
    
    if (user_guess == random_int):
        print(f'muito bem, você acertou em {i} tentativas!')
        exit(0)
    
    elif (user_guess < random_int):
        print('Você errou para menos, tente novamente')
        
    else:
        print('Você errou para mais, tente novamente')
        
print(f'Você perdeu, o número era {random_int}')