from tkinter import *
import webview
import webview.menu as wm
from tkinter import filedialog
import ttkthemes
from winotify import Notification
import os

def resetar():
    view.load_url('https://drum-kit-uxbn.glide.page')

def exit():
    view.destroy()

def read_cookies():
    cookies = view.get_cookies()
    for c in cookies:
        print(c.output())

class Api:
    def clearCookies(self):
        view.clear_cookies()
        print('Cookies cleared')

notificacao = Notification(app_id="Drum Kit", title="Baixado!", msg="Baixado com sucesso!")

def notifi_baixado():
    notificacao.show()

def config():
    configu = Tk()
    configu.title("Configuração")
    configu.geometry("200x100")
    
    caminho = Entry(configu)
    caminho.grid(column=0, row=0)

    button = Button(configu, text="...", command=lugar)
    button.grid(column=1, row=0)

    caminho.config()
    configu.mainloop()

def lugar():
    ludar = filedialog.askdirectory()

def arquivos():
    caminho = "/Downloads"
    files = os.listdir(caminho)

    win = Tk()
    win.geometry("450x800")

    transform = StringVar(win)
    transform.set(files[0])

    lista = OptionMenu(win, transform, files)
    lista.grid(column=0, row=0)

    win.mainloop()

tk = Tk()
tk.geometry("800x450")

webview.settings = {
  'ALLOW_DOWNLOADS': True,
  'ALLOW_FILE_URLS': True,
  'OPEN_EXTERNAL_LINKS_IN_BROWSER': False,
  'OPEN_DEVTOOLS_IN_DEBUG': True
}

view = webview.create_window('Drum Kits', 'https://drum-kit-uxbn.glide.page', js_api=Api())

menu_itens = [
    wm.Menu(
        'Menu',
            [
                wm.MenuAction('Resetar', resetar),
                wm.MenuSeparator(),
                wm.MenuAction("Configurações", config),
                wm.MenuAction("Sair", exit)
            ],
        ),
    
    wm.MenuAction("Downloads", arquivos)
]

webview.start(read_cookies, view, private_mode=False, http_server=True, http_port=13377, menu=menu_itens) 