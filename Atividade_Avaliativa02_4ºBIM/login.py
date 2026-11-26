# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from repositorio_usuario import *

class App:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("login.glade")

        self.janela = self.builder.get_object("jan_principal")
        self.entrada_login = self.builder.get_object("entryLogin")
        self.entrada_senha = self.builder.get_object("entrySenha")
        self.lbl_resultado = self.builder.get_object("lblResultado")

        self.btn_entrar = self.builder.get_object("btnEntrar")
        if self.btn_entrar is not None:
            self.janela.set_default(self.btn_entrar)

        self.builder.connect_signals(self)
        self.janela.connect("destroy", Gtk.main_quit)
        self.janela.show_all()

    def _exibir_mensagem(self, mensagem):
        if self.lbl_resultado is not None:
            self.lbl_resultado.set_text(mensagem)
        print(mensagem)

    def ao_entrar(self, _widget):
        login = self.entrada_login.get_text().strip() if self.entrada_login else ""
        senha = self.entrada_senha.get_text() if self.entrada_senha else ""

        if not login or not senha:
            self._exibir_mensagem("Usuário ou senha inválidos.")
            return

        nome_usuario = verificar_login(login, senha)
        if nome_usuario is not None:
            self._exibir_mensagem(f"Login válido. Bem-vindo(a), {nome_usuario}!")
        else:
            self._exibir_mensagem("Usuário ou senha inválidos.")

if __name__ == "__main__":
    App()
    Gtk.main()