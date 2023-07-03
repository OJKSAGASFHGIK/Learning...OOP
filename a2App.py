from dataclasses import dataclass, field
from datetime import datetime
from random import randint

# a4 = class , b1 = variables


class a1:
    def a1def(self):
        print('Def of class a1.')


class a2:
    def __init__(self, nome, idade, trabalhando=False, jogando=False):
        self.nome = nome
        self.idade = idade
        self.trabalhando = trabalhando
        self.jogando = jogando

    def jogar(self, jogo):
        if self.trabalhando:
            print(f"{self.nome} can't play in times of job.")
            return
        elif not self.trabalhando:
            print(f"{self.nome} are playing {jogo}.")

    def agora(self, a):
        if self.trabalhando:
            print("It's working much...")
            return
        self.trabalhando = True
        print(f'{self.nome} has {self.idade} and are working in {a}.')

    def depois(self):
        if not self.trabalhando:
            print(f"{self.nome} aren't working.")
            return
        self.trabalhando = False
        print(f'{self.nome} stopped of work.')
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def ano_de_nascimento(self):
        return self.ano_atual - self.idade

    random = "It's"

    @classmethod
    def classmethod(cls):
        print(f"{cls.random} a classmethod. It means that you won't use __init__ here.")

    @staticmethod
    def random_id():
        random_id = randint(10000, 20000)
        return random_id


class desconto:
    def __init__(self, item, desconto):
        self.item = item
        self.desconto = desconto

    def descontar(self):
        return self.item*(1-(self.desconto/100))

    # Getter
    @property
    def item(self):
        return self._item
    # Setter

    @item.setter
    def item(self, itemA):
        if isinstance(itemA, str):
            itemA = str(itemA.replace(' ', ''))
            itemA = float(itemA.replace('R$', ''))
        self._item = itemA


class miniDatabase:
    def __init__(self):
        self.__pessoa = {}

    def add(self, id, nome):
        if 'usuarios' not in self.__pessoa:
            self.__pessoa['usuarios'] = {id: nome}
        else:
            self.__pessoa['usuarios'].update({id: nome})

    def show(self):
        for id, nome in self.__pessoa['usuarios'].items():
            print(id, nome)

    def clear(self, id):
        del self.__pessoa['usuarios'][id]


class pessoa:
    def __init__(self, pessoa):
        self.__pessoa = pessoa
        self.__recebedorDeClasse = None

    @property
    def pessoa(self):
        return self.__pessoa

    @property
    def recebedorDeClasse(self):
        return self.__recebedorDeClasse

    @recebedorDeClasse.setter
    def recebedorDeClasse(self, recebedorDeClasse):
        self.__recebedorDeClasse = recebedorDeClasse


class a3:
    def __init__(self, someName):
        self.__someName = someName

    @property
    def someName(self):
        return self.__someName

    def write(self):
        print('a3 are in use.')


class a4:
    def __init__(self, someName):
        self.__someName = someName

    @property
    def someName(self):
        return self.__someName

    def write(self):
        print('a4 are in use.')


#
class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class list:
    def __init__(self):
        self.list = []

    def add(self, product):
        self.list.append(product)

    def show(self):
        for product in self.list:
            print(product.name, product.price)

    def sum(self):
        b1 = 0
        for product in self.list:
            b1 += product.price
        return b1


# .append(a5(state, initial))
class a5:
    def __init__(self, state, initial):
        self.state = state
        self.initial = initial

    def __del__(self):
        print(f'{self.state} foi apagado.')


class a6:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.place = []
        self.general = [self.name, self.age, self.place]

    def a6append(self, state, initial):
        self.place.append(a5(state, initial))

    def a6print(self):
        for a5 in self.place:
            print(self.name, self.age, a5.state, a5.initial)

    def __del__(self):
        print(f'{self.name} foi apagado.')


# class a9(a7, a8):
class a7:
    def __init__(self, name):
        self.name = name

    def eating(self):
        print(f'{self.name} are eating.')


class a8:
    def shopping(self):
        print(f'{self.name} are shopping.')


class a9(a7, a8):
    def studying(self):
        print(f'{self.name} are studying.')


#
class a10:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        str_mod = str(f'{self.first_name} {self.last_name}')
        return str_mod

    def __eq__(self, o):
        return self.last_name == o.last_name

# In this case, we are using the method __eq__ to compare 2 variables:
#   a1 = a10(1)
#   a2 = a10(2)
#   ex: print(a1 == a2)


@dataclass(slots=True)
class a11:
    first_name: str = field(compare=False)  # compare
    last_name: str
    status: bool = False
    _list: list = field(default_factory=list, repr=False)
    _full_name: str = field(default='unknown', init=True,
                            repr=False, compare=False)

    def __post_init__(self):
        self._full_name = f'{self.first_name} {self.last_name}'  # compare

# +Field methods:
#   compare - It's for don't compare, ex: print(hm == hm2)
#   kw_only=True - It's for this: v_some = a1(itsYourKw=['some list'])
#       cool idea:
#           @dataclass(kw_only=True)
#   frozen=True - It's for block your dataclass: @dataclass(frozen=True)
#   .__dict__ - show everything in the class: print(a1.__dict__)

#   slots=True - It's show just the keys: @dataclass(slots=True)
#   .__slots__ - It's show just the keys: print(a1.__slots__)
