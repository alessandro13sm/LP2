# Nome: Alessandro da Silva Moreira
# Turma: 2º Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Conversor de Moedas e Cripto")
        janela.set_default_size(300, 200)

        box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=True, spacing=10)

        self.conversao = Gtk.Label(label="Valor convertido: ")

        self.reais = Gtk.Entry(placeholder_text="Reais (R$)")

        self.btn_dolar = Gtk.Button(label="Para Dólar")
        self.btn_dolar.connect("clicked", self.converter_dolar)

        self.btn_euro = Gtk.Button(label="Para Euro")
        self.btn_euro.connect("clicked", self.converter_euro)

        self.btn_bitcoin = Gtk.Button(label="Para Bitcoin")
        self.btn_bitcoin.connect("clicked", self.converter_bitcoin)

        box_vert.pack_start(self.conversao, expand=True, fill=True, padding=0)
        box_vert.pack_start(self.reais, expand=True, fill=True, padding=0)
        box_vert.pack_end(self.btn_dolar, expand=True, fill=True, padding=10)
        box_vert.pack_end(self.btn_euro, expand=True, fill=True, padding=10)
        box_vert.pack_end(self.btn_bitcoin, expand=True, fill=True, padding=10)
        janela.add(box_vert)
        janela.show_all()

    def converter_dolar(self, componente=None, dados=None):
        dados = int(self.reais.get_text())
        self.conversao.set_text(f"{dados * 0.19}")

    def converter_euro(self, componente=None, dados=None):
        dados = int(self.reais.get_text())
        self.conversao.set_text(f"{dados * 0.17}")

    def converter_bitcoin(self, componente=None, dados=None):
        dados = int(self.reais.get_text())
        self.conversao.set_text(f"{dados * 0.0000031}")


    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()