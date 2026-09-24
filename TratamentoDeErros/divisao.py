#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_INTERFACE = os.path.join(PASTA, 'divisao.glade')

class Aplicacao:
    def __init__(self):
        self.construtor = Gtk.Builder()
        self.construtor.add_from_file(ARQUIVO_INTERFACE)
        self.construtor.connect_signals(self)
        self.janela = self.construtor.get_object('jan_principal')
        self.txt_dividendo = self.construtor.get_object('txt_dividendo')
        self.txt_divisor = self.construtor.get_object('txt_divisor')
        self.btn_dividir = self.construtor.get_object('btn_dividir')
        self.lbl_resultado = self.construtor.get_object('lbl_resultado')

        self.janela.show_all()

    def ao_destruir(self, componente=None, dados=None):
        Gtk.main_quit()

    def mostrar_dialogo(self, titulo, mensagem):
        dialogo = Gtk.MessageDialog(
            transient_for = self.janela,
            flags = 0,
            message_type = Gtk.MessageType.WARNING,
            buttons = Gtk.ButtonsType.OK,
            text = titulo
        )
        dialogo.format_secondary_markup(mensagem)
        dialogo.run()
        dialogo.destroy()

    def ao_dividir(self, componente=None, dados=None):
        try:
            dividendo = float(self.txt_dividendo.get_text().replace(',', '.'))
            divisor = float(self.txt_divisor.get_text().replace(',', '.'))
            resultado = dividendo / divisor
        except ValueError:
            self.lbl_resultado.set_markup('-')
            self.mostrar_dialogo("Erro na entrada de dados", "Entre apenas com <b>números</b>")
            self.txt_divisor.set_text('')
            self.txt_dividendo.set_text('')
            self.txt_dividendo.grab_focus()
        except ZeroDivisionError:
            self.lbl_resultado.set_markup('-')
            self.mostrar_dialogo("Erro na entrada de dados", "Não há como <b>dividir por zero!</b>")
            self.txt_divisor.set_text('')
            self.txt_dividendo.set_text('')
            self.txt_dividendo.grap_focus()
        else:
            self.lbl_resultado.set_markup(f'<small><i>{resultado}</i></small>')
        finally:
            print('Erros tratados.')

if __name__ == "__main__":
    app = Aplicacao()
    Gtk.main()
