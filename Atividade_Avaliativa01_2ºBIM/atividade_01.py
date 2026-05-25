from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Forma):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.lado = lado
    
    def area(self):
        print(f"A área desse quadrado é: {self.lado**2}")
    
    def perimetro(self):
        print(f"O perímetro desse quadrado é: {self.lado * 4}")

class Triangulo(Forma):
    def __init__(self, cor, lado1, lado2, base, altura):
        super().__init__(cor)
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
        self.altura = altura
        while self.lado1 + self.lado2 < self.base or self.lado1 + self.base < self.lado2 or self.base + self.lado2 < self.lado1:
            print("Desiguldade Triangular! Insira novos valores para esse triângulo.")
            self.lado1 = int(input("Medida do lado 1: "))
            self.lado2 = int(input("Medida do lado 2: "))
            self.base = int(input("Medida da base: "))

    def area(self):
        if self.lado1 == self.lado2 == self.base:
            print(f"Área do triângulo (equilátero): {(self.lado1**2) * (3**0.5) / 4:.2f}")
        else:
            print(f"Área do triângulo: {(self.base * self.altura) / 2:.2f}")

    def perimetro(self):
        print(f"Perímetro do triângulo: {self.lado1 + self.lado2 + self.base}")

class Circulo(Forma):
    def __init__(self, cor, raio, pi=3.14):
        super().__init__(cor)
        self.raio = raio
        self.pi = pi
    
    def area(self):
        print(f"Área do círculo: {self.pi * (self.raio**2):.2f}")

    def perimetro(self):
        print(f"Perímetro do círculo: {2 * self.pi * self.raio:.2f}")

class Retangulo(Forma):
    def __init__(self, cor, base, altura):
        super().__init__(cor)
        self.base = base
        self.altura = altura
    
    def area(self):
        print(f"Área do retângulo: {self.base * self.altura}")
    
    def perimetro(self):
        print(f"Perímetro do retângulo: {2 * self.base + 2 * self.altura}")

class Hexagono(Forma):
    def __init__(self, cor, lado):
        super().__init__(cor)
        self.lado = lado
    
    def area(self):
        print(f"Área do hexágono: {6 * ((self.lado**2) * (3**0.5) / 4):.2f}")
    
    def perimetro(self):
        print(f"Perímetro do hexágono: {self.lado * 6}")
