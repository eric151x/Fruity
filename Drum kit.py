from tkinter import *
import webview
import webview.menu as wm
from tkinter import filedialog
from winotify import Notification
import os
import configparser
from tkinter import messagebox
import zipfile

config = configparser.ConfigParser()
config.read("config.ini")

def salvar(local):
    config['DEFAULT']['local'] = local

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def reiniciar():
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

def lugar():
    ludar = filedialog.askdirectory()

def configuracao():
    configu = Tk()
    configu.title("Configuração")
    configu.geometry("200x100")
    
    caminho = Entry(configu)
    caminho.grid(column=0, row=0)

    button = Button(configu, text="...", command=lugar)
    button.grid(column=1, row=0)

    save = Button(configu, text="salvar", command=salvar(local=caminho.get()))
    save.grid(column=2, row=1)

    caminho.config()
    configu.mainloop()

def instalar(baguio):
    messagebox.showinfo("Instalado!", f"{baguio} instalado com sucesso!")

def arquivos():
    caminho = f"C:/Users/{os.getlogin()}/Desktop/Python/Drum Kit/Downloads"
    files = os.listdir(caminho)

    win = Tk()
    win.geometry("200x300")
    win.title("Downloads")

    transform = StringVar(win)
    transform.set(files[0])

    lista = OptionMenu(win, transform, *files)
    lista.grid(column=0, row=0)

    pronto = transform.get()

    istala = Button(win, text="Instalar", command=instalar(pronto))
    istala.grid(column=0, row=1)

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
                wm.MenuAction('Reiniciar', reiniciar),
                wm.MenuSeparator(),
                wm.MenuAction("Configurações", configuracao),
                wm.MenuAction("Sair", exit)
            ],
        ),
    
    wm.MenuAction("Downloads", arquivos)
]

webview.start(read_cookies, view, private_mode=False, http_server=True, http_port=13377, menu=menu_itens) 