import time
from tarefas import cadastrar, consultar, reservar, devolução, catalogo_reservas
from utils import mensagem

# importando funções de outras páginas 
 
continuidade_sistema = True
print("Bem-vindo ao sistema de locação de filmes!!")
#apresentação do sistema 
 
while continuidade_sistema:
    mensagem('Menu Principal')
    print("1. Cadastrar")
    print("2. Consultar")
    print("3. Reservar")
    print("4. Devolver")
    print("5. Catálogo de filmes reservados")
    print("6. Sair")
    time.sleep(0.2)
    # almanetando o delay na execução do sistema.
 
    opção = int(input("Digite a opção desejada: "))
    verf = [1, 2, 3, 4, 5, 6]
    # verificação para se caso a pessoa digite uma opção errada no sistema.
 
    if opção not in verf:
        print("Opção inválida, tente novamente.")
 
    elif opção == 1:
        time.sleep(0.2)
        cadastrar()
 
    elif opção == 2:
        time.sleep(0.2)
        consultar()
 
    elif opção == 3:
        time.sleep(0.2)
        reservar()
 
    elif opção == 4:
        time.sleep(0.2)
        devolução()
 
    elif opção == 5:
        time.sleep(0.2)
        catalogo_reservas()
 
    elif opção == 6:
        time.sleep(0.2)
        continuidade_sistema = False
        print("Sistema encerrado, muito obrigado por ter utilizado!")