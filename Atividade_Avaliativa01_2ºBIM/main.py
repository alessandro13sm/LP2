from atividade_01 import *

print(f"-- SISTEMA DE GEOMETRIAS --".center(80, "-"))

# forma = Forma("Colorido")
quadrado = Quadrado("Azul", 2)
triangulo = Triangulo("Vermelho", 5, 5, 5, 1)
circulo = Circulo("Verde", 4)
retangulo = Retangulo("Amarelo", 7, 3)
hexagono = Hexagono("Laranja", 8)

formas = [quadrado, triangulo, circulo, retangulo, hexagono]
for forma in formas:
    print(f"Cor: {forma.cor}")
    forma.area()
    forma.perimetro()
    print("\n")

"""
    3 - Discussão

    a) O que aconteceu quando você tentou criar um objeto diretamente da classe Forma?

        Ocorreu um erro, uma vez que é uma forma abstrata e não pode ser instanciada.

    b) Se você tentar alterar a cor da forma diretamente (ex: forma.__cor = "Azul"), o que acontece? Por que usamos métodos Getters e Setters?

        Também ocorre um erro. Usamos para poder acessar e alterar valores privados.
    
    c) Quais códigos você não precisou repetir nas classes filhas por causa da classe Forma?

        O construtor que define o atributo __cor.

    d) Como o Python soube qual fórmula de área usar se, dentro do for, chamamos apenas o método .area()?

        Ele soube através do polimorfismo, já que cada objeto reescreve o método .area() (e é obrigado a reescrever pela classe pai abstrata)
    
    e) Caso você precisasse adicionar os cálculos para área e perímetro de Triângulo Equilátero, o que precisaria fazer?

        É cabível colocá-la como uma classe filha da classe Triangulo.
    
    f) Explique o que é o princípio de aberto/fechado dentro do SOLID. Como este princípio pode ser visto nesta estrutura que vocês montaram?

        O princípio fala sobre como softwares tem que estarem abertos para extensão, porém fechados para modificação.
        Dá para perceber no código através da classe abstrata, em que é possível adicionar mais coisas nela ou novas formas.
"""