#listas,tuplas de status
# criação de um banco de dados baseado em dicionário.
titulo = {'madagascar': {'genero': 'animação','ano':2005,'duracao': '1h30m', 'status': 'disponível'}
        ,'kung fu panda': {'genero': 'animação', 'ano': 2008, 'duracao': '1h30m', 'status': 'disponível'}, 
'pinguins': {'genero': 'animação', 'ano': 2014, 'duracao': '1h32m', 'status': 'disponivel'}     }
reservas = {}
# H fiz esses de baixo
filmes = ['madagascar', 'kung fu panda', 'pinguins']
fila_reservas = ['madagascar', 'kung fu panda', 'pinguins']
fila_reservas = [f for f in filmes if titulo[f]['status'] == 'disponível']
pilha_devolucoes = []
status_opcoes = ('disponível', 'reservado', 'indisponível')
# lista de reservas de filmes.