# Grupo: Alessandro de Silva Moreira, Dante Venga Dias e Gabriel Anselmo da Silva Nascimento
# Turma: 2º Informática

from abc import ABC, abstractmethod

# classe abstrata
class AtividadeFisica(ABC):
    def __init__(self, data, distancia):
        super().__init__()
        self.__data = data
        self.__distancia_km = distancia

    @abstractmethod
    def calcular_calorias(self):
        pass

    # métodos getter
    @property
    def distancia_km(self):
        return self.__distancia_km
    
    @property
    def data(self):
        return self.data

class Corrida(AtividadeFisica):
    def __init__(self, data, distancia):
        super().__init__(data, distancia)

    # método para calcular as calorias (polimorfismo)
    def calcular_calorias(self):
        calorias = self.distancia_km * 70
        return calorias

class Caminhada(AtividadeFisica):
    def __init__(self, data, distancia):
        super().__init__(data, distancia)

    # método para calcular as calorias (polimorfismo)
    def calcular_calorias(self):
        calorias = self.distancia_km * 35
        return calorias

class DiarioDeTreino:
    def __init__(self, lista):
        self.lista = lista
    
    # método que percorre a lista de atividades e chama todos os métodos calcular_calorias()
    def resumo_calorico(self):
        soma = 0
        for i in self.lista:
            soma += i.calcular_calorias()
        return soma

# testes
corrida1 = Corrida("14/12/2007", 4)
corrida2 = Corrida("22/08/2008", 7)
caminhada1 = Caminhada("26/06/2009", 20)
caminhada2 = Caminhada("19/04/2007", 10)
diario = DiarioDeTreino([corrida1, corrida2, caminhada1, caminhada2])

print(f"O total gasto da corrida 1 foi {corrida1.calcular_calorias()} cal")
print(f"O total gasto da corrida 2 foi {corrida2.calcular_calorias()} cal")
print(f"O total gasto da caminhada 1 foi {caminhada1.calcular_calorias()} cal")
print(f"O total gasto da caminhada 2 foi {caminhada2.calcular_calorias()} cal\n")

print(f"Total gasto: {diario.resumo_calorico()}")

# Boa noite Bruno!!! Maxima pls
# https://www.youtube.com/watch?v=yaZs0n27IV8 - assiste esse vídeo aqui Bruno!!!!
