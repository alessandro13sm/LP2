# Nome: Alessandro da Silva Moreira
# Turma: 2º Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Simulador de Notas Escolares")
        janela.set_default_size(300, 200)
        janela.set_border_width(15)

        self.box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=False, spacing=10)

        self.nota_final = Gtk.Label(label="Nota Final: ")
        self.aprovacao = Gtk.Label(label="")

        self.nota1 = Gtk.Entry(placeholder_text="Primeira Nota")
        self.nota2 = Gtk.Entry(placeholder_text="Segunda Nota")
        self.nota3 = Gtk.Entry(placeholder_text="Terceira Nota")

        btn_media = Gtk.Button(label="Calcular Média")
        btn_media.connect("clicked", self.calcular_media)
        btn_recalcular = Gtk.Button(label="Recalcular Média")
        btn_recalcular.connect("clicked", self.recalcular)

        self.box_recuperacao = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=True, spacing=10)
        self.recuperacao = Gtk.Entry(placeholder_text="Prova de Recuperação")

        self.box_recuperacao.pack_start(self.recuperacao, expand=False, fill=True, padding=0)
        self.box_recuperacao.pack_start(btn_recalcular, expand=False, fill=True, padding=0)

        self.box_vert.pack_start(self.nota_final, expand=True, fill=True, padding=0)
        self.box_vert.pack_start(self.aprovacao, expand=True, fill=True, padding=0)
        self.box_vert.pack_start(self.nota1, expand=True, fill=True, padding=0)
        self.box_vert.pack_start(self.nota2, expand=True, fill=True, padding=0)
        self.box_vert.pack_start(self.nota3, expand=True, fill=True, padding=0)
        self.box_vert.pack_end(btn_media, expand=True, fill=True, padding=0)

        self.box_vert.pack_start(self.box_recuperacao, expand=False, fill=True, padding=0)
        janela.add(self.box_vert)
        janela.show_all()

        self.box_recuperacao.hide()
        self.media_atual = 0

    def calcular_media(self, componentes=None, dados=None):
        self.media_atual = (float(self.nota1.get_text()) + float(self.nota2.get_text()) + float(self.nota3.get_text())) / 3
        self.nota_final.set_label(f"Nota Final: {self.media_atual}")
        if self.media_atual >= 6:
            self.aprovacao.set_markup("<span foreground='green' weight='bold'>Aprovado</span>")
            self.box_recuperacao.hide()
        else:
            self.aprovacao.set_markup("<span foreground='red' weight='bold'>Em Recuperação</span>")
            self.box_recuperacao.show_all()

    def recalcular(self, componentes=None, dados=None):
        nova_media = (self.media_atual + float(self.recuperacao.get_text())) / 2
        self.nota_final.set_label(f"Nota Final (Pós-Rec): {nova_media:.2f}")
        if nova_media >= 6.0:
            self.aprovacao.set_markup("<span foreground='green' weight='bold'>Aprovado após Recuperação</span>")
        else:
            self.aprovacao.set_markup("<span foreground='red' weight='bold'>Reprovado</span>")

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()