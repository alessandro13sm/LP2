#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Nomes: Alessandro da Silva Moreira, Matheus Mendes Francisco e Leon Antonio Pereira Batista
# Turma: 2º Informática

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_INTERFACE = os.path.join(PASTA, 'editor_anotacoes.glade')

class Aplicacao:
    def __init__(self):
        self.construtor = Gtk.Builder()
        self.construtor.add_from_file(ARQUIVO_INTERFACE)
        self.construtor.connect_signals(self)

        self.janela = self.construtor.get_object('janela_principal')
        self.titulo = self.construtor.get_object('lbl_titulo')
        self.entrada_titulo = self.construtor.get_object('input_titulo')
        self.entrada_anotacao = self.construtor.get_object('input_anotacao')
        self.btn_salvar = self.construtor.get_object('btn_salvar')
        self.btn_limpar = self.construtor.get_object('btn_limpar')
        self.lbl_caracteres = self.construtor.get_object('palavras')
        self.alteracoes = self.construtor.get_object('salvamento')
        self.caracteres = 0
        self.palavras = 0
        self.txt_titulo = ''
        self.txt_anotacao = ''
        self.alterou = False

        self.janela.show_all()

    def salvar(self, componente=None, dados=None):
        if not self.alterou:
            self.alteracoes.set_markup(f'<span foreground="red">Nada foi escrito</span>')
        else:
            title = self.entrada_titulo.get_text()
            self.titulo.set_markup(f"<big><b>Editor de Anotações - {title}</b></big>")
            self.alteracoes.set_markup(f'<span foreground="green">Alterações salvas</span>')

    def limpar(self, componente=None, dados=None):
        self.alterou = False
        self.entrada_titulo.set_text("")
        self.entrada_anotacao.set_text("")
        self.titulo.set_markup(f"<big><b>Editor de Anotações - sem título *</b></big>")
        self.lbl_caracteres.set_markup(f"<small>0 caracteres - 0 palavras</small>")
        self.alteracoes.set_markup(f'<span foreground="red">Alterações não salvas</span>')

    def atualizar_textos(self, componente=None, dados=None):
        self.alterou = True
        self.txt_titulo = self.entrada_titulo.get_text()
        self.txt_anotacao = self.entrada_anotacao.get_text()
        self.caracteres = len(self.txt_titulo) + len(self.txt_anotacao)
        self.palavras = len(self.txt_titulo.split()) + len(self.txt_anotacao.split())
        self.lbl_caracteres.set_text(f"{self.caracteres} caracteres - {self.palavras} palavras")

    def fechar(self, componente=None, dados=None):
        Gtk.main_quit()

if __name__ == "__main__":
    Aplicacao()
    Gtk.main()
