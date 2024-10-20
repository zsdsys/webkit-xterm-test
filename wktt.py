import gi
import os

gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2

window = Gtk.Window()
window.set_default_size(800, 600)
window.connect("destroy", Gtk.main_quit)

scrolled_window = Gtk.ScrolledWindow()
webview = WebKit2.WebView()

settings = webview.get_settings()

settings.set_enable_developer_extras(True)

file_path = os.path.abspath('term.html')

file_uri = f'file://{file_path}'

webview.load_uri(file_uri)
scrolled_window.add(webview)

window.add(scrolled_window)
window.show_all()
Gtk.main()

