class Pessoa:
    def __init__(self, nome=None, idade=46):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Roberto')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Nilton'
    print(p.nome)
    print(p.idade)