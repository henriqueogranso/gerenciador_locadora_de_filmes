#listas,tuplas de status
# criação de um banco de dados baseado em dicionário.
titulo={'madagascar': {'genero': 'animação','ano':2005,'duracao': '1h30m', 'status': 'disponível'}
        ,'pinguins': {'genero': 'animação', 'ano': 2014, 'duracao': '1h30m', 'status': 'reservado'}
        ,'kung fu panda': {'genero': 'animação', 'ano': 2008, 'duracao': '1h30m', 'status': 'disponível'}
        }
reservas = { 'pinguins':{ 'nome_cliente': 'joão', 'data_reserva': '01/01/2024', 'data_vencimento': '07/01/2024',}}
# H fiz esses de baixo
filmes = ['madagascar', 'pinguins', 'kung fu panda']
<<<<<<< HEAD
fila_reservas = ['madagascar', 'kung fu panda']
=======
fila_reservas = [f for f in filmes if titulo[f]['status'] == 'disponível']
>>>>>>> teste_sistema
pilha_devolucoes = []
status_opcoes = ('disponível', 'reservado', 'indisponível')
# lista de reservas de filmes.