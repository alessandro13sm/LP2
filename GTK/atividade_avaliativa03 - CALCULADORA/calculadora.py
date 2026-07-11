# Nome: Alessandro da Silva Moreira
# Turma: 2º Informática

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class App:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect("delete-event", self.sair)
        janela.set_title("Calculadora")
        janela.set_resizable(False)
        janela.set_default_size(300, 200)
        janela.set_border_width(15)

        self.valor1 = 0
        self.valor2 = 0
        self.operador = None

        # todas as box necessárias
        box_vert = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=False, spacing=10)
        box_hor = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=False, spacing=10)
        box_hor.set_halign(Gtk.Align.CENTER)
        box_botoes1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=False, spacing=10)
        box_botoes1.set_halign(Gtk.Align.CENTER)
        box_botoes2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=False, spacing=10)
        box_botoes2.set_halign(Gtk.Align.CENTER)
        box_botoes3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=False, spacing=10)
        box_botoes3.set_halign(Gtk.Align.CENTER)
        box_botoes4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=False, spacing=10)
        box_botoes4.set_halign(Gtk.Align.CENTER)

        # todos os componentes
        self.visor = Gtk.Entry()
        btn_clear = Gtk.Button(label="C")
        btn_clear.connect("clicked", self.limpar)
        btn_7 = Gtk.Button(label="7")
        btn_7.connect("clicked", self.registrar_num, "7")
        btn_8 = Gtk.Button(label="8")
        btn_8.connect("clicked", self.registrar_num, "8")
        btn_9 = Gtk.Button(label="9")
        btn_9.connect("clicked", self.registrar_num, "9")
        btn_raiz = Gtk.Button(label="√")
        btn_raiz.connect("clicked", self.registrar_raiz, "0.5")
        btn_4 = Gtk.Button(label="4")
        btn_4.connect("clicked", self.registrar_num, "4")
        btn_5 = Gtk.Button(label="5")
        btn_5.connect("clicked", self.registrar_num, "5")
        btn_6 = Gtk.Button(label="6")
        btn_6.connect("clicked", self.registrar_num, "6")
        btn_soma = Gtk.Button(label="+")
        btn_soma.connect("clicked", self.registrar_op, "+")
        btn_1 = Gtk.Button(label="1")
        btn_1.connect("clicked", self.registrar_num, "1")
        btn_2 = Gtk.Button(label="2")
        btn_2.connect("clicked", self.registrar_num, "2")
        btn_3 = Gtk.Button(label="3")
        btn_3.connect("clicked", self.registrar_num, "3")
        btn_sub = Gtk.Button(label="-")
        btn_sub.connect("clicked", self.registrar_op, "-")
        btn_0 = Gtk.Button(label="0")
        btn_0.connect("clicked", self.registrar_num, "0")
        btn_igual = Gtk.Button(label="=")
        btn_igual.connect("clicked", self.calcular)
        btn_div = Gtk.Button(label="/")
        btn_div.connect("clicked", self.registrar_op, "/")
        btn_multi = Gtk.Button(label="*")
        btn_multi.connect("clicked", self.registrar_op, "*")

        lbl = Gtk.Label(label="Alessandro da Silva Moreira\n2º Informática")
        lbl.set_justify(Gtk.Justification.CENTER)

        # adições
        box_hor.add(self.visor)
        box_hor.add(btn_clear)
        box_botoes1.add(btn_7)
        box_botoes1.add(btn_8)
        box_botoes1.add(btn_9)
        box_botoes1.add(btn_raiz)
        box_botoes2.add(btn_4)
        box_botoes2.add(btn_5)
        box_botoes2.add(btn_6)
        box_botoes2.add(btn_soma)
        box_botoes3.add(btn_1)
        box_botoes3.add(btn_2)
        box_botoes3.add(btn_3)
        box_botoes3.add(btn_sub)
        box_botoes4.add(btn_0)
        box_botoes4.add(btn_div)
        box_botoes4.add(btn_multi)
        box_botoes4.add(btn_igual)
        box_vert.add(box_hor)
        box_vert.add(box_botoes1)
        box_vert.add(box_botoes2)
        box_vert.add(box_botoes3)
        box_vert.add(box_botoes4)
        box_vert.pack_end(lbl, expand=True, fill=True, padding=0)
        janela.add(box_vert)
        janela.show_all()

    # registra o número e limpa o visor caso tenha algum símbolo
    def registrar_num(self, componente=None, dados=None):
        if self.visor.get_text() == "+" or self.visor.get_text() == "-" or self.visor.get_text() == "*" or self.visor.get_text() == "/":
            self.visor.set_text("")
            if len(self.visor.get_text()) < 12:
                self.visor.set_text(self.visor.get_text() + dados)
        else:
            if len(self.visor.get_text()) < 12:
                self.visor.set_text(self.visor.get_text() + dados)
    
    # registra operador e obtém o valor que estava no visor
    def registrar_op(self, componente=None, dados=None):
        self.operador = dados
        valor = float(self.visor.get_text())
        if self.valor1 == 0:
            self.valor1 = valor
        else:
            self.valor2 = valor
        self.visor.set_text("")
        self.visor.set_text(dados)
        self.visor.grab_focus()

    # cálculo de raiz padrão
    def registrar_raiz(self, componente=None, dados=None):
        valor = float(self.visor.get_text()) ** float(dados)
        self.visor.set_text(f"{valor:.2f}")

    # verifica qual é o operador e faz a conta com base nisso
    def calcular(self, componente=None, dados=None):
        self.valor2 = float(self.visor.get_text())
        if self.operador == "+":
            self.visor.set_text(f"{self.valor1 + self.valor2}")
        elif self.operador == "-":
            self.visor.set_text(f"{self.valor1 - self.valor2}")
        elif self.operador == "*":
            self.visor.set_text(f"{self.valor1 * self.valor2}")
        elif self.operador == "/":
            if self.valor2 == 0:
                erro = Gtk.Window() # criação de uma nova janela para informar o erro de divisão por 0
                erro.set_default_size(100, 100)
                erro.set_resizable(False)
                erro.set_border_width(15)
                erro.set_title("ERRO")
                lbl = Gtk.Label(label="Não existe divisão por 0!")
                erro.add(lbl)
                erro.show_all()
            else:
                self.visor.set_text(f"{self.valor1 / self.valor2}")
        self.valor1 = self.valor2 = 0
        self.operador = None

    # função para o botão C
    def limpar(self, componente=None, dados=None):
        self.visor.set_text("")
        self.valor1 = self.valor2 = 0
        self.operador = None

    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    app = App()
    Gtk.main()
