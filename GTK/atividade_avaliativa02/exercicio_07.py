# Nome: Alessandro da Silva Moreira
# Turma: 2º Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Formulário de Inscrição em Evento")
        janela.set_default_size(300, 200)
        janela.set_border_width(15)

        box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=False, spacing=10)

        self.nome = Gtk.Entry(placeholder_text="Digite seu nome")
        btn = Gtk.Button(label="Salvar")
        btn.connect("clicked", self.registrar)

        self.curso = Gtk.ComboBoxText()
        self.curso.append_text("Informática")
        self.curso.append_text("Mecatrônica")
        self.curso.append_text("Edificações")

        self.certificado = Gtk.CheckButton(label="Deseja certificado?")

        self.resumo = Gtk.Label(label="")

        box_vert.pack_start(self.nome, expand=True, fill=True, padding=0)
        box_vert.pack_start(self.curso, expand=True, fill=True, padding=0)
        box_vert.pack_start(self.certificado, expand=True, fill=True, padding=0)
        box_vert.pack_end(btn, expand=True, fill=True, padding=0)
        box_vert.pack_end(self.resumo, expand=True, fill=True, padding=0)
        janela.add(box_vert)
        janela.show_all()

        self.resumo.hide()

    def registrar(self, componente=None, dados=None):
        if self.certificado.get_active():
            self.resumo.set_label(f"Resumo:\nNome: {self.nome.get_text()}\nCurso: {self.curso.get_active_text()}\nCertificado: Sim")
            self.resumo.set_halign(Gtk.Align.START)
            self.resumo.show_all()
        else:
            self.resumo.set_label(f"Resumo:\nNome: {self.nome.get_text()}\nCurso: {self.curso.get_active_text()}\nCertificado: Não")
            self.resumo.set_halign(Gtk.Align.START)
            self.resumo.show_all()

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()