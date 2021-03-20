nomes = list()
while True:
    nomes.append(input('Digite um nome para cadastro:\n'))
    
    if (input('Deseja execultar novamente?(sim/nao)\n') != 'sim'): break
    
print('\n\nNomes Cadastrados:')
for nome in nomes: print(nome.capitalize())