# H: adicionei "titulos", "fila_reservas" e "pilha_devolucoes" em from dados
from dados import titulo, reservas, filmes, fila_reservas, pilha_devolucoes
from utils import mensagem, linha

def cadastrar():
    mensagem('cadastrar')
    nome = input("digite o nome do filme:").strip().lower() #v: adicionei o strip e lower para evitar erros de digitação
    # cria um cadastro selecionando pares de chaves em dicionários.
    if nome not in titulo:
        genero = input("digite o genero do filme:")
        ano = int(input("digite o ano do filme:"))
        duracao = input("digite a duração do filme:")
        titulo[nome] = {"genero": genero, "ano": ano, "duracao": duracao, "status": 'disponível'}
        # H: adicionei aqui filmes.append e fila_reservas.append
        filmes.append(nome)
        fila_reservas.append(nome)
        print("cadastro realizado com sucesso!")
    else:
        print("filme já cadastrado.")
        # nome representa o filme no caso do madagacar dentro do dicionário titulo, e adiciona ao dicionário conforme o usuário digitar.
        


def consultar():
    # mesmo princípio adiciona no dicionário. 
    mensagem('consultar')
    nome = input("digite o nome do filme que deseja consultar:").strip().lower() #v: adicionei o strip e lower para evitar erros de digitação
    if nome in titulo:
        print(f"nome: {nome}")
        print(f"genero: {titulo[nome]['genero']}")
        print(f"duração: {titulo[nome]['duracao']}")
        print(f"ano: {titulo[nome]['ano']}")
        print(f"status: {titulo[nome]['status']}")
    else:
        print("filme não encontrado.")
# H: adicionei listar_catalogo
def listar_catalogo():
    mensagem('catálogo completo')
    for nome in filmes:
        print(f"titulo: {nome}")
        print(f"status: {titulo[nome]['status']}")
        linha()

def reservar():
        mensagem('reservar')
        nome = input("digite o nome do filme que deseja reservar:").strip().lower()#v:. adicionei o strip e lower para evitar erros de digitação
        if nome not in titulo:
            print("filme não encontrado.")
            return
        if nome in reservas:
            print("filme já reservado.")
            return
        nome_cliente = input("digite o nome do cliente:").strip().lower()
        data_reserva = input("digite a data da reserva:")
        data_vencimento = input("digite a data de vencimento da reserva:")
        reservas[nome] = {"nome_cliente": nome_cliente, "data_reserva": data_reserva, "data_vencimento": data_vencimento}
        titulo[nome]['status'] = 'reservado'
        if nome in fila_reservas:
            fila_reservas.remove(nome)
        print("reserva realizada com sucesso!")
            

def devolucao():
    mensagem('devolução')     
    # função de devolução tem o mesmo princípio de reservar.
    nome = input("digite o nome do filme que deseja devolver:").strip().lower()#v: adicionei o strip e lower para evitar erros de digitação
    if nome in reservas:
        # verifica nome digitado dentro de reservas
        verf_nome_cliente = input("digite o nome do cliente para confirmar a devolução:").strip().lower() #v: adicionei o strip e lower para evitar erros de digitação
        if verf_nome_cliente != reservas[nome]['nome_cliente']:
            print("nome do cliente não confere, devolução cancelada.")
            return
        opção = input("deseja realmente devolver o filme? (s/n)")
        # Da uma opção do usuário se ele realmente quer devolver.
        if opção.lower() == 's':
            del reservas[nome]
            if nome in titulo:#V: corrijido o bug de não verificar se o filme existe em titulo antes de alterar o status
            # deleta o nome de reservas
                titulo[nome]['status']= 'disponível'
            # altera o status de reservados para disponível no dicionário de titulo.
            pilha_devolucoes.append(nome)
            # H: adicionei a pilha_devolucoes
            if nome not in fila_reservas:
                fila_reservas.append(nome)
            # H: adicionei a fila_reservas
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
        linha()
        
        
# H: Adicionei aqui histórico de devoluções
def historico_devolucoes():
    mensagem('histórico de devoluções')
    if not pilha_devolucoes:
        print("nenhuma devolução registrada ainda.")
    else:
        for nome in reversed(pilha_devolucoes):
            print(f"filme devolvido: {nome}")
            linha()