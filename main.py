import time
from tarefas import cadastrar, consultar, reservar, devolucao, catalogo_reservas, listar_catalogo, historico_devolucoes
from utils import mensagem

# importando funções de outras páginas 
 
continuidade_sistema = True
print("Bem-vindo ao sistema de locação de filmes!!")
#apresentação do sistema 
 
while continuidade_sistema:
    # H: Adicionei a opção listar catalogo e historico devoluçoes
    mensagem('Menu Principal')
    print("1. Cadastrar")
    print("2. Listar catálogo completo")
    print("3. Consultar")
    print("4. Reservar")
    print("5. Devolver")
    print("6. Histórico devoluções")
    print("7. Catálogo de filmes reservados")
    print("8. Sair")
    print()
    time.sleep(0.2)
    # almanetando o delay na execução do sistema.
    try:
        opção = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Digite apenas números!")
        continue
    # H: Adicionei o try/except para aparecer mensagem caso a pessoa digite letra
    
    # verificação para se caso a pessoa digite uma opção errada no sistema.
 
    if opção not in range(1, 9):
        print("Opção inválida, tente novamente.")
 
    elif opção == 1:
        time.sleep(0.2)
        cadastrar()
 
    elif opção == 2:
        time.sleep(0.2)
        listar_catalogo()
 
    elif opção == 3:
        time.sleep(0.2)
        consultar()
 
    elif opção == 4:
        time.sleep(0.2)
        reservar()
 
    elif opção == 5:
        time.sleep(0.2)
        devolucao()
        
    elif opção == 6:
        time.sleep(0.2)
        historico_devolucoes()
 
    elif opção == 7:
        time.sleep(0.2)
        catalogo_reservas()
 
    elif opção == 8:
        time.sleep(0.2)
        continuidade_sistema = False
        print("Sistema encerrado, muito obrigado por ter utilizado!")