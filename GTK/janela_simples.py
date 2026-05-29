import gi # importar pygobject + gtk
gi.require_version("Gtk", "3.0") # definir qual a versão
from gi.repository import Gtk # essas 3 linhas são obrigatórias

janela = Gtk.Window() # instanciar uma janela, criar uma variável que receberá um objeto do tipo Gtk.Window
janela.show() # e depois exibir essa janela
Gtk.main() # event loop
