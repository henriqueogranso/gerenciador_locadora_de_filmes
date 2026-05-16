from dados import titulo, reservas
from utils import mensagem 
def cadastrar():
        # cria um cadastro selecionando pares de chaves em dicionários.
        mensagem('cadastrar')
        nome = input("digite o nome do filme:")
        genero = input("digite o genero do filme:")
        ano = input("digite o ano do filme:")
        duracao = input("digite a duração do filme:")
        titulo[nome] = {"genero": genero, "ano": ano, "duracao": duracao, "status": 'disponível'}
        # nome representa o filme no caso do madagacar dentro do dicionário titulo, e adiciona ao dicionário conforme o usuário digitar.
        print("cadastro realizado com sucesso!")


def consultar():
        # mesmo princípio adiciona no dicionário 
        mensagem('consultar')
        nome = input("digite o nome do filme que deseja consultar:")
        if nome in titulo:
            print(f"nome: {nome}")
            print(f"genero: {titulo[nome]['genero']}")
            print(f"duração: {titulo[nome]['duracao']}")
            print(f"ano: {titulo[nome]['ano']}")
            print(f"status: {titulo[nome]['status']}")
        else:
            print("filme não encontrado.")

def reservar():
        mensagem('reservar')
        nome = input("digite o nome do filme que deseja reservar:")
        nome_cliente = input("digite o nome do cliente:")
        data_reserva = input("digite a data da reserva:")
        data_vencimento = input("digite a data de vencimento da reserva:")

        if nome in titulo:
            # verifica o nome do filme dentro do dicionário de titulo
            if nome not in reservas:
                reservas[nome]= {'nome_cliente': nome_cliente, 'data_reserva': data_reserva, 'data_vencimento': data_vencimento}
                titulo[nome]['status']= 'reservado'
                print("reserva realizada com sucesso!")
            else:
                print(f"o filme ja foi reservado por {reservas[nome]['nome_cliente']} e vence em {reservas[nome]['data_vencimento']}")
        else:
            # se caso o nome digitado não for encontrado dentro de titulo 
            print("filme não encontrado.")

def devolução():
     mensagem('devolução')     
     # função de devolução tem o mesmo princípio de reservar.
     nome = input("digite o nome do filme que deseja devolver:")
     if nome in reservas:
            # verifica nome digitado dentro de reservas 
            opção = input("deseja realmente devolver o filme? (s/n)")
            # Da uma opção do usuário se ele realmente quer devolver.
            if opção.lower() == 's':
                del reservas[nome]
                # deleta o nome de reservas
                titulo[nome]['status']= 'disponível'
                # altera o status de reservados para disponível no dicionário de titulo.
                print("devolução realizada com sucesso!")
            else:
                print("devolução cancelada.")
     else:
        print("filme não encontrado.")


def catalogo_reservas():
    mensagem('catálogo de filmes reservados')
    for nome in reservas:
        print(f"nome do filme: {nome}")
        print(f"nome do cliente: {reservas[nome]['nome_cliente']}") 
        print(f"data da reserva: {reservas[nome]['data_reserva']}")
        print(f"data de vencimento: {reservas[nome]['data_vencimento']}")
        
        
