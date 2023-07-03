# https://www.youtube.com/watch?v=RLVbB91A5-8&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=1&t=57s&ab_channel=Ot%C3%A1vioMiranda
# 1:09 - class Pessoa, 1:57, 2:26, 3:32, 7:07, 7:48, 9:46, 12:39, 12:48,
# 13:46 - self.funcao = funcao , 17:28, 17:56, 19:49, 21:00, 23:05, 31:15, 32:04,
# 34:06,
# https://www.youtube.com/watch?v=ZTKeC1lae6I&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=2&ab_channel=Ot%C3%A1vioMiranda
# 4:17 - @classmethod,
# https://www.youtube.com/watch?v=fChIn5Agl90&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=3&ab_channel=Ot%C3%A1vioMiranda
# 1:17 - @staticmethod, 2:35,
# https://www.youtube.com/watch?v=PGXwNophTOQ&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=4&ab_channel=Ot%C3%A1vioMiranda
# 4:14 - #Getter, 4:44 - @property, 5:28 - _var, 5:57 - #Setter, 6:32 - @var.setter,
# 7:12 - self._var = var2,
# https://www.youtube.com/watch?v=Q86OP92hYG0&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=5&ab_channel=Ot%C3%A1vioMiranda
# 0:15,
# https://www.youtube.com/watch?v=Xo1oCx6hqG4&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=6&ab_channel=Ot%C3%A1vioMiranda
# 0:45, 2:26 - self.dados = {} ,
# https://www.youtube.com/watch?v=lA4UAIEGKaU&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=7&ab_channel=Ot%C3%A1vioMiranda
# self.__something = None
# https://www.youtube.com/watch?v=ewGulRBQxOE&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=8&ab_channel=Ot%C3%A1vioMiranda
# 'you can call other classes in a class. The class is like one variable, so you don't
#   need a self. inside this.'
# https://www.youtube.com/watch?v=O6F77N09HdI&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=9&ab_channel=Ot%C3%A1vioMiranda
# https://www.youtube.com/watch?v=zUwZNb5Vc1U&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=12
# from dataclasses import dataclass, field
# @dataclass
#   class a11:
#       first_name: str
#       _list: list = field(default_factory=list)
#
from random import randint

from a2App import (a1, a2, a3, a4, a6, a9, a10, a11, desconto, list,
                   miniDatabase, pessoa, product)

input('Next===>')
b1 = a1()  # class
print("""===
+Code in files:
-a2App:
    class a1:
        def a1def(self):
            print('Def of class a1.')
-a1Note:
    from a2App import a1
    b1 = a1()
    b1.a1def()
===""")
b1.a1def()

#
input('2.Next===>')

b2 = a2('Rebeca', 23)
b3 = a2('Micaela', 27)
b2.agora('OOP')
b2.agora('')
b2.depois()
b2.depois()
b2.jogar('Stardew Valley')
b3.agora('HTML5')
b3.jogar('Hollow Knight')

#
input('3.Next===>')

b4 = a2('Luiz', 24)
print(f'{b4.nome} nasceu em {b4.ano_de_nascimento()}.')

#
input('4.Next===>')
a2.classmethod()
print("""===
-Code in a2App:
    random = "It's"
    @classmethod
    def classmethod(cls):
        print(f"{cls.random} a classmethod. It means that you won't use __init__ here.")
===""")

#
input('5.Next===>')
b5 = a2.random_id()
print(f"random id: {b5}")
print("""===
-Code:
    @staticmethod
    def random_id():
        random_id = randint(10000, 20000)
        return random_id
===
-Note:
You can't use parameters in a @staticmethod, Becouse your fuction here is be static.
===""")

#
input('6.Next===>')
print("""===
#Code in a2App.py:
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
===
-Note:
The @property is for establish one connection with the variable, and use this valor
 in the future. Example:
    class a1:
        def __init__(self, b1):
            self.b1 = b1
        @property
        def b1(self):
            return self._b1
        @setter
        ...
In this case, everything that changes b1 will change _b1 too. You will do this, for
 do debbugs in your def @setter.
===""")
b6 = str(input("Price of item: "))
b7 = float(input("% of discount: "))
b8 = desconto(b6, b7)
print(b8.descontar())

#
input('7.Next===>')
print("""===
+Code in files:
-a2App:
class miniDatabase:
    def __init__(self):
        self.__pessoa = {}
    def add(self, id, nome):
        if 'usuarios' not in self.__pessoa:
            self.__pessoa['usuarios'] = {id:nome}
        else:
            self.__pessoa['usuarios'].update({id:nome})
    def show(self):
        for id, nome in self.__pessoa['usuarios'].items():
            print(id, nome)
    def clear(self, id):
        del self.__pessoa['usuarios'][id]
===
-Notas:
This class just served for remember a little of dict and for you know that when you use
 this in python: '__randomVar'(more important) or this: '_randomVar'(less important)
 It means what is heart of your project, and what you(or some community) can't edit.
===""")
b9 = miniDatabase()
b9.add(1, 'Greque')
b9.add(2, 'OJK')
b9.add(3, 'Sagas')
b9.clear(2)
b9.show()

#
input('8.Next===>')
b10 = pessoa('Algum nome')
b11 = a3('a')
b12 = a4('b')
pessoa.recebedorDeClasse = b11
pessoa.recebedorDeClasse.write()
pessoa.recebedorDeClasse = b12
pessoa.recebedorDeClasse.write()
print("""In this case, 'the class pessoa have one valor in yourself' like 'None'.
 Everything that are in None is received for it.""")
# a4 b12
#
input('9.Next===>')
b13product_list = list()

b14 = product('egg', 3)  # It's like a repeating structure
b13product_list.add(b14)
b14 = product('banana', 6)
b13product_list.add(b14)

b13product_list.show()
print(b13product_list.sum())
print(b13product_list)
# a4 b14
#
input('10.Next===>')
b15 = a6(f'name{randint(1,99)}', f'age{randint(1,99)}')
b15.a6append(f'state{randint(1,99)}', 'abbreviation')
b15.a6print()
del b15
b16 = a6(f'name{randint(1,99)}', f'age{randint(1,99)}')
b16.a6append(f'state{randint(1,99)}', 'abbreviation')
b16.a6print()
del b16
# a6 b16
#
input('11.Next: "class a9(a7, a8):" ===> ')
b17 = a9('Greque')
b17.eating()
b17.shopping()
b17.studying()
# a9 b17
#
input('10.Next===>')
b18 = a10('Name', 'L.Name')
b19 = a10('Name', 'L.Name')
print(b18 == b19)
#
# a10 b19
input('11.Next===>')
b20 = a11('pudim', 'doce', True, ['list', 1])
b21 = a11('banana', 'doce', True, ['list', 1])
print(f"""{b20}
{b21}
{b20 == b21}
keys: {a11.__slots__}""")
