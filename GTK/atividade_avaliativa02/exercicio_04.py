# Nome: Alessandro da Silva Moreira
# Turma: 2º Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Calculadora de IMC")
        janela.set_default_size(300, 200)

        box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=True, spacing=10)

        self.imc = Gtk.Label(label="IMC: ")
        self.classificacao = Gtk.Label(label="Classificação: ")

        self.peso = Gtk.Entry(placeholder_text="Kilogramas")
        self.altura = Gtk.Entry(placeholder_text="Metros")

        btn_entrar = Gtk.Button(label="Calcular")
        btn_entrar.connect("clicked", self.calcular_imc)

        box_vert.pack_start(self.imc, expand=True, fill=True, padding=0)
        box_vert.pack_start(self.classificacao, expand=True, fill=True, padding=0)
        box_vert.add(self.peso)
        box_vert.add(self.altura)
        box_vert.pack_end(btn_entrar, expand=True, fill=True, padding=10)
        janela.add(box_vert)
        janela.show_all()

    def calcular_imc(self, componente=None, dados=None):
        peso = float(self.peso.get_text())
        altura = float(self.altura.get_text())
        self.imc.set_label(f"IMC: {peso / (altura**2):.2f}")
        if peso / (altura**2) < 18.5:
            self.classificacao.set_label("Magreza")
        elif 18.5 <= (peso / (altura**2)) <= 24.9:
            self.classificacao.set_label("Normal")
        elif 25 <= (peso / (altura**2)) <= 29.9:
            self.classificacao.set_label("Sobrepeso")
        elif 30 <= (peso / (altura**2)) <= 34.9:
            self.classificacao.set_label("Obesidade Grau I")
        elif 35 <= (peso / (altura**2)) <= 39.9:
            self.classificacao.set_label("Obesidade Grau II")
        else:
            self.classificacao.set_label("Obesidade Grau III")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()