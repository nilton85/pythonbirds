class Pessoa:
    olhos = 2

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
    roberto.sobrenome = 'Goncalves'
    del roberto.filhos
    roberto.olhos = 1
    del roberto.olhos
    print(roberto.__dict__)
    print(nilton.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(roberto.olhos)
    print(nilton.olhos)
    print(id(Pessoa.olhos), id(roberto), id(nilton.olhos))