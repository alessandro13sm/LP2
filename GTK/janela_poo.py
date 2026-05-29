import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Tela:
    """ Classe que representa a interface """
    def __init__(self):
        janela = Gtk.Window()
        janela.show()

if __name__ == '__main__':
    prog = Tela()
    Gtk.main()