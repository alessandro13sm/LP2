#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Nomes: Alessandro da Silva Moreira, Matheus Mendes Francisco e Leon Antonio Batista
# Turma: 2º Informática

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

CSS_ESTILO = b"""
.bordas-redondas {
    border-radius: 10px;
    border: 1px solid gray;
}
"""

PASTA = os.path.dirname(os.path.abspath(__file__))
ARQ = os.path.join(PASTA, 'divide_conta.glade')

class Aplicacao:
    def __init__(self):
        self.construtor = Gtk.Builder()
        self.construtor.add_from_file(ARQ)
        self.construtor.connect_signals(self)
        self.janela = self.construtor.get_object('jan_principal')
        self.valor_conta = self.construtor.get_object('txt_valor')
        self.num_pessoas = self.construtor.get_object('txt_pessoas')
        self.gorjeta = self.construtor.get_object('txt_gorjeta')
        self.btn_calcular = self.construtor.get_object('btn_calcular')
        self.btn_salvar = self.construtor.get_object('btn_salvar')
        self.btn_abrir = self.construtor.get_object('btn_abrir')
        self.btn_limpar = self.construtor.get_object('btn_limpar')
        self.lbl_saida = self.construtor.get_object('lbl_saida')
        self.lbl_status = self.construtor.get_object('lbl_status')
        self.comprovante_salvo = None

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

    def ao_calcular(self, componente=None, dados=None):
        try:
            valor = float(self.valor_conta.get_text().replace(',', '.'))
            pessoas = float(self.num_pessoas.get_text().replace(',', '.'))
            gorjeta = float(self.gorjeta.get_text().replace(',', '.')) / 100
            resultado = (valor + (valor * gorjeta)) / pessoas
            self.comprovante_salvo = resultado
            if valor < 0 or pessoas < 0:
                raise ValueError(self.mostrar_dialogo("Valor inválido", "O valor da conta ou a quantidade de pessoas não pode ser <b>negativa!</b>"))
        except ValueError:
            self.mostrar_dialogo("Valor inválido", "Digite apenas <b>números</b> nos campos de entrada!")
            self.valor_conta.set_text('')
            self.num_pessoas.set_text('')
            self.gorjeta.set_text('')
            self.valor_conta.grab_focus()
        except ZeroDivisionError:
            self.mostrar_dialogo("Valor inválido", "Impossível dividir por <b>0 pessoas</b>!")
            self.valor_conta.set_text('')
            self.num_pessoas.set_text('')
            self.gorjeta.set_text('')
            self.valor_conta.grab_focus()
        except FileNotFoundError:
            self.mostrar_dialogo("Arquivo inexistente", "O arquivo do comprovante salvo <b>não existe</b>!")
            self.valor_conta.grab_focus()
        else:
            self.lbl_saida.set_markup(f'Cada pessoa paga\n<big><big><big><b>{resultado:.2f}</b></big></big></big>')
        finally:
            self.lbl_status.set_markup('<span foreground="green">Dados salvos.</span>')

    def ao_salvar(self, componente=None, dados=None):
        if self.valor_conta.get_text():
            self.comprovante_salvo = self.lbl_saida.get_text().replace(',', '.')
            self.lbl_status.set_text('Aguardando dados...')
        else:
            self.lbl_status.set_text('Nenhum dado para salvar...')

    def ao_abrir(self, componente=None, dados=None):
        if self.comprovante_salvo != None:
            self.mostrar_dialogo("Comprovante salvo", f"O comprovante salvo tem o valor de {self.comprovante_salvo}")
        else:
            self.mostrar_dialogo(f"Comprovante inexistente", "Não existe comprovante salvo!")

    def ao_limpar(self, componente=None, dados=None):
        self.valor_conta.set_text('')
        self.num_pessoas.set_text('')
        self.gorjeta.set_text('')
        self.comprovante_salvo = None
        self.valor_conta.grab_focus()
        self.lbl_status.set_text('Aguardando dados...')

if __name__ == "__main__":
    app = Aplicacao()
    Gtk.main()
