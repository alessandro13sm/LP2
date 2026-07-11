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

        box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=True, spacing=10)

        self.status = Gtk.Label(label="Status: ")

        self.usuario = Gtk.Entry(placeholder_text="Usuário")
        self.senha = Gtk.Entry(placeholder_text="Senha")
        self.senha.set_visibility(False)

        btn_entrar = Gtk.Button(label="Entrar!")
        btn_entrar.connect("clicked", self.logar)

        box_vert.add(self.status)
        box_vert.add(self.usuario)
        box_vert.add(self.senha)
        box_vert.pack_end(btn_entrar, expand=True, fill=True, padding=10)
        janela.add(box_vert)
        janela.show_all()

    def logar(self, componente=None, dados=None):
        if self.usuario.get_text() == "admin" and self.senha.get_text() == "123":
            self.status.set_label("Status: Acesso Liberado")
        else:
            self.status.set_markup("Status: <span foreground='red'>Acesso Negado</span>")


    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()