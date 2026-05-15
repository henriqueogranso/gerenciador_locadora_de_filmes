from dados import titulo, reservas
from utils import linha, mensagem 
def cadastrar():
        mensagem('cadastrar')
        nome = input("digite o nome do filme:")
        genero = input("digite o genero do filme:")
        ano = input("digite o ano do filme:")
        duracao = input("digite a duração do filme:")
        titulo[nome] = {"genero": genero, "ano": ano, "duracao": duracao, "status": 'disponível'}
        print("cadastro realizado com sucesso!")


def consultar():
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
        nome = input("digite o nome do filme que deseja reservar:")
        nome_cliente = input("digite o nome do cliente:")
        data_reserva = input("digite a data da reserva:")
        data_vencimento = input("digite a data de vencimento da reserva:")

        if nome in titulo:
            if nome not in reservas:
                reservas[nome]= {'nome_cliente': nome_cliente, 'data_reserva': data_reserva, 'data_vencimento': data_vencimento}
                titulo[nome]['status']= 'reservado'
                print("reserva realizada com sucesso!")
            else:
                print(f"o filme ja foi reservado por {reservas[nome]['nome_cliente']} e vence em {reservas[nome]['data_vencimento']}")
        else:
            print("filme não encontrado.")

def devolução():
     nome = input("digite o nome do filme que deseja devolver:")
     if nome in reservas:
            opção = input("deseja realmente devolver o filme? (s/n)")
            if opção.lower() == 's':
                del reservas[nome]
                titulo[nome]['status']= 'disponível'
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
        
        
