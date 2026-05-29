import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Tela:
    """ Classe que representa a interface """
    def __init__(self):
        tela = Gtk.Window()

        # definindo atributos/propriedades
        tela.set_title("1ª aula com GTK")
        tela.set_default_size(400, 400)

        # adicionando elementos neste container
        rotulo = Gtk.Label(label="Hello World em GTK!!")
        tela.add(rotulo)

        tela.connect("destroy", Gtk.main_quit)

        tela.show()
        rotulo.show()
        # tela.show_all() também funcionaria

if __name__ == '__main__':
    prog = Tela()
    Gtk.main()