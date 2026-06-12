#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Aplicacao:
    def __init__(self):
        janela = Gtk.Window()
        janela.connect('delete-event', self.sair)
        janela.set_title("Minha Primeira Box")
        janela.set_border_width(10)

        caixa = Gtk.Box(homogeneous=True, spacing=10)
        btn_fe = Gtk.Button()
        btn_fe.set_label("Fé")
        btn_fe.connect("clicked", self.imprimir, 1)
        btn_paz = Gtk.Button()
        btn_paz.set_label("Paz")
        btn_paz.connect("clicked", self.imprimir, 3)
        btn_coragem = Gtk.Button()
        btn_coragem.set_label("Coragem")
        btn_coragem.connect("clicked", self.imprimir, 5)

        caixa.add(btn_fe)
        caixa.add(btn_paz)
        caixa.add(btn_coragem)
        janela.add(caixa)
        janela.show_all()
    
    def imprimir(self, componente=None, dados=None):
        msg = componente.get_label()
        print(f":-) {msg * dados} :-)")
    
    def sair(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == '__main__':
    prog = Aplicacao()
    Gtk.main()