# Nome: Alessandro da Silva Moreira
# Turma: 2º Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Contador de Cliques")
        janela.set_default_size(300, 200)

        box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=True)

        self.num = Gtk.Label(label="0")
        self.num.set_justify(Gtk.Justification.CENTER)

        btn = Gtk.Button(label="Clique Aqui!")
        btn.connect("clicked", self.incrementar)

        box_vert.add(self.num)
        box_vert.add(btn)
        janela.add(box_vert)
        janela.show_all()

    def incrementar(self, componente=None, dados=None):
        dados = int(self.num.get_text())
        dados += 1
        self.num.set_label(str(dados))

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()