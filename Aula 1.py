class Livro:
    def __init__(self, titulo, resumo, autor, protagonista, genero, faixa_etaria):
        self.titulo = titulo
        self.resumo = resumo
        self.autor = autor
        self.protagonista = protagonista
        self.genero = genero
        self.faixa_etaria = faixa_etaria
        self.disponibilidade = True
        self.responsavel = None
        
    #Ver quem está responsável pelo livro
    def ver_responsavel(self):
        if self.responsavel == None:
            return print('O livro está em sua responsabilidade')
        else:
            return print('{} está responsável pelo livro'.format(self.responsavel.nome))

    #Realizar um empréstimo
    def emprestar(self, amigo):
        if self.disponibilidade == True and amigo.idade >= self.faixa_etaria:
            self.responsavel = amigo.nome
            amigo.livros.append(self.titulo)
            self.responsavel = amigo
            self.disponibilidade = False
            return print('Empresatado para {}'.format(amigo.nome))
        elif self.disponibilidade == False:
            return print('Este livro já está empresatado para {}'.format(self.responsavel.nome))
        elif self.faixa_etaria > amigo.idade:
            return print('{} não tem idade para ler esse livro'.format(amigo.nome))
        
class Amigo:
    def __init__(self, nome, numero, email, ano_de_nascimento):
        self.nome = nome
        self.numero = numero
        self.email = email
        self.idade = 2021 - ano_de_nascimento
        self.livros = []

    #Ver quais livros estão sob responsabilidade do amigo
    def responsavel_livros(self):
        if self.livros == None:
            return print('{} está responsável por: {}'.format(self.nome, self.livros))
        else:
            return print('{} não está responsável por nenhum livro'.format(self.nome))