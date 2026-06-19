# importa o Gtk e as classes da atividade anterior
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from att1 import *

# classe da janela
class App:
    def __init__(self):
        # cria a janela, definindo o título, tamanho e evento para sair
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Tracker de Treinos")
        janela.set_default_size(500, 500)

        box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=True, spacing=10)

        btn_corrida = Gtk.Button(label="Registrar Corrida")
        btn_corrida.connect("clicked", self.pegar_corrida)

        btn_caminhada = Gtk.Button(label="Registrar Caminhada")
        btn_caminhada.connect("clicked", self.pegar_caminhada)
        self.label_inferior = Gtk.Label(label="")

        box_vert.add(btn_corrida)
        box_vert.add(btn_caminhada)
        box_vert.pack_end(self.label_inferior, expand=False, fill=False, padding=0)
        janela.add(box_vert)
        janela.show_all()
    
    # método que roda ao clicar no botão de registrar corrida
    def pegar_corrida(self, componente=None, dados=None):
        dados = int(input("Digite a distância: "))
        data = input("Digite a data: ")
        corrida = Corrida(data, dados) # pega todos os dados para a classe e instancia
        self.label_inferior.set_label(f"Você gastou {corrida.calcular_calorias()} cal na corrida!") # atualiza a label
        print(f"{dados} * 70 = {corrida.calcular_calorias()}") # log no terminal

    def pegar_caminhada(self, componente=None, dados=None):
        dados = int(input("Digite a distância: "))
        data = input("Digite a data: ")
        caminhada = Caminhada(data, dados) # pega todos os dados para a classe e instancia
        self.label_inferior.set_label(f"Você gastou {caminhada.calcular_calorias()} cal na caminhada!") # atualiza a label
        print(f"{dados} * 35 = {caminhada.calcular_calorias()}") # log no terminal

    # evento para sair
    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    aplicacao = App()
    Gtk.main() # loop para a GUI continuar na tela

# https://www.youtube.com/watch?v=yaZs0n27IV8 - assiste esse vídeo aqui Bruno!!!!