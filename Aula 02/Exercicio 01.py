# Exercício para agora) Implementar um método saca(valor) na classe Conta e criar
# uma programa Python que atua como gerente de contas. A aplicação usa a
# interface de comandos, direto no prompt, para fornecer as funcionalidade de criar
# conta, depositar valor em conta, sacar valor de uma conta e ver contas. Cada conta
# deverá ser acessada pelo seu número que deve ser único no sistema (não precisa
# de validação). Sugere-se o uso de uma lista ou um dicionário para armazenar as
# contas (apenas em memória mesmo). O menu deve ser apresentado ao usuário
# sempre que ele resolver alguma ação. Sugere-se como menu a seguinte estrutura:
# Sistema de Contas: menu principal
# 1: Criar conta
# 2: Remover conta
# 3: Listar contas
# 4: Depositar valor em conta
# 5: Sacar valor de uma conta
# Entre com uma opção:
        
contas = dict()

opcoes_menu = {
    1 : "Criar Conta",
    2 : "Remover Conta",
    3 : "Listar Contas",
    4 : "Depositar valor em conta",
    5 : "Sacar valor de uma conta"
}

range_opcoes = f'[1 - {len(opcoes_menu)}]'

def menu():
    while True:
        try:
            print("Escolha uma operação:\n")

            for operacao, descricao in opcoes_menu.items():
                print(f'{operacao} - {descricao}')
                
            operacao_usuario = int(input(f'{range_opcoes}:  '))
            
            if operacao_usuario in range(1, len(opcoes_menu) + 1) and operacao_usuario != 0:
                break
            else:
                print("\n\nOpção invalida, tente novamente:")
                
        except ValueError:
            print(f'Valor inserido precisar ser um número inteiro dentro do range {range_opcoes}')
            
        except Exception as e:
            print(f'Erro ao execultar operacao tente novamente \n {e}')
    
    return operacao_usuario
            
class Conta:
    
    def __init__(self, numero=None, titular=None, saldo=None, limite=None):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def deposito(self, valor):
        self.saldo += valor
        
    def saque(self, valor):
        self.saldo -= valor
        
def input_valor(texto_input):
    while True:
        try:
            saldo_inicial = float(input(f'{texto_input}\n'))
            return saldo_inicial
        except ValueError:
            print(f'Valor inserido precisar ser um número real.')
        except Exception as e:
            print(f'Erro ao execultar operacao tente novamente \n {e}')

def criar_conta():
    nome_usuario = input('Qual o nome do titular?\n')
    saldo_inicial = input_valor('Qual o saldo inicial?')
    limite_credito = input_valor('Qual o limite de crédito?')
    id_conta = (len(contas) + 1) if len(contas) > 0 else 1
    contas[id_conta] = Conta(numero=id_conta + 1, titular=nome_usuario, saldo=saldo_inicial, limite=limite_credito)

def listar_contas():
    if nao_existem_contas():
        return True
    
    print('')
    for id_conta, dados in contas.items():
       print(f'{id_conta} - {contas[id_conta].titular}')
       limite_conta = contas[id_conta].limite if contas[id_conta].saldo >= 0 else contas[id_conta].limite + contas[id_conta].saldo
       print(f'\tSaldo Atual:\t{contas[id_conta].saldo}\t\tLimite Disponivel: \t{limite_conta}')
    print('')
    
def nao_existem_contas():
    if len(contas) == 0:
        print('\n**\tNão existem contas.\t**\n')
        return True 
    else:
        return False
    
def escolher_conta():
    while True:
        try:
            listar_contas()
            
            id_conta = int(input())
            
            if id_conta != 0 and id_conta <= len(contas):
                return id_conta
            else:
                print("\n\nOpção invalida, tente novamente:")
                
        except ValueError:
            print(f'Valor inserido precisar ser uma conta válida.')
            
        except Exception as e:
            print(f'Erro ao execultar operacao tente novamente \n {e}')
            
    
def deletar_conta():
    if nao_existem_contas():
        return True
    
    print("Escolha uma conta para deletar:\n")
    id_conta = escolher_conta()
    if id_conta != 0:
        del contas[id_conta]
        
    return True

def deposito_conta():
    if nao_existem_contas():
        return True
    
    print('Selecione uma conta para fazer o deposito:')
    id_conta = escolher_conta()
    valor_deposito = input_valor('Qual o valor do deposito desejado?')
    contas[id_conta].deposito(valor_deposito)
    print(f'O valor de R${valor_deposito} foi depositado com sucesso')

def saque_conta():
    if nao_existem_contas():
        return True
    
    print('Selecione uma conta para fazer o saque:')
    id_conta = escolher_conta()
    valor_saque = input_valor('Qual o valor do saque desejado?')
    
    if valor_saque <= contas[id_conta].saldo:
        contas[id_conta].saque(valor_saque)
        print(f'O valor de R$ {valor_saque} foi sacado com sucesso sem usar o limite de crédito')
    elif (valor_saque > contas[id_conta].saldo) and (valor_saque <= (contas[id_conta].saldo + contas[id_conta].limite)):
        contas[id_conta].saque(valor_saque)
        limite_restante = contas[id_conta].limite + contas[id_conta].saldo
        print(f'O valor de R$ {valor_saque} foi sacado com sucesso usando seu crédito restando apenas R$ {limite_restante} crédito')
    else:
        limite_restante = contas[id_conta].limite + contas[id_conta].saldo
        # valor da divida errado
        print(f'Operação não realizada pois o saldo da conta se encontra negativo em R$ {contas[id_conta].saldo} com o limite de crédito restante em R$ {limite_restante} totalizando uma dívida de R${contas[id_conta].limite - limite_restante}')

funcoes = {
    1 : criar_conta,
    2 : deletar_conta,
    3 : listar_contas,
    4 : deposito_conta,
    5 : saque_conta,
}

if __name__== '__main__':
    
    while True:
        #print(contas)
        try:
            operacao = menu()
            funcoes[operacao]()
        except KeyboardInterrupt:
            exit()