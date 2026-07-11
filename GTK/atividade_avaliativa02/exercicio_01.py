# Nome: Alessandro da Silva Moreira
# Turma: 2º Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Cartão de Visitas Digital")
        janela.set_default_size(400, 200)

        nome = Gtk.Label(label="Alessandro da Silva Moreira\n2º Informática")
        nome.set_justify(Gtk.Justification.CENTER)

        janela.add(nome)
        janela.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()
