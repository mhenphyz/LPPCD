# Exercicio 03 - Slide 22

operadores = ['+', '-', '*', '/']

while True:
    
    primeiro_valor = input('Insira um número real:\n')
    segundo_valor  = input('Insira outra número real:\n')
    operacao = input('Escolha uma dos seguintes operadores:\n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão\n')    
    
    try:
        operador = primeiro_valor + operadores[int(operacao) - 1] + segundo_valor
        print(f'O resultado da conta matemática é {float(eval(operador))}')
        break
    except Exception as e:
        print('Não foi possível execultar a operação, tente novamente\n')