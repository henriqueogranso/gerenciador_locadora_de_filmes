# Gerenciador de Locadora de Filmes

Este é um sistema simples desenvolvido em Python para gerenciar o catálogo, as reservas e as devoluções de uma locadora de filmes através do terminal.

Link do repositório: https://github.com/henriqueogranso/gerenciador_locadora_de_filmes/blob/d91f4705a61eb69badbc5feea8eb2e57288c8ef2/README.md

## Como Funciona

O sistema foi estruturado de forma modular e é dividido nos seguintes arquivos:
* main.py: Contém o loop principal e gerencia a navegação do menu interativo.
* tarefas.py: Concentra as funções das regras de negócio (cadastrar, consultar, reservar e devolver).
* dados.py: Atua como o armazenamento temporário (em memória), utilizando dicionários e listas.
* utils.py: Contém funções utilitárias para a formatação visual das mensagens no terminal.

## Estruturas de Dados Utilizadas

* Dicionários (dict): Para mapear os detalhes e metadados dos filmes e das reservas de forma rápida.
* Listas (list): Para listar o inventário geral e gerenciar as filas de filmes disponíveis.
* Pilhas (LIFO): Utilizada na lista de devoluções recentes, onde o último filme devolvido é o primeiro a ser exibido.

## Opções do Menu Principal

Ao iniciar o sistema, estão disponíveis as seguintes operações:
1. Cadastrar novo filme
2. Listar catálogo completo
3. Consultar informações de um filme
4. Reservar um filme para um cliente
5. Devolver um filme reservado
6. Ver histórico de devoluções (ordem reversa)
7. Ver catálogo de filmes reservados
8. Sair do sistema

## Como Executar

1. Certifique-se de ter o Python 3 instalado em sua máquina.
2. Certifique-se de que todos os arquivos do projeto (.py) estejam no mesmo diretório.
3. Abra o terminal ou prompt de comando na pasta do projeto.
4. Execute o comando:

```bash
python main.py