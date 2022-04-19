class Pessoa:
    def __init__(self, *filhos, nome=None, idade=46):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__ == '__main__':
    nilton = Pessoa(nome='Nilton')
    roberto = Pessoa(nilton, nome='Roberto')
    print(Pessoa.cumprimentar(roberto))
    print(id(roberto))
    print(roberto.cumprimentar())
    print(roberto.nome)
    print(roberto.idade)
    for filho in roberto.filhos:
        print(filho.nome)