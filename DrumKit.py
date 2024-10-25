from tkinter import *
import webview
import webview.menu as wm
from tkinter import filedialog
import os
import configparser
from tkinter import messagebox
import zipfile
from tkinter import ttk

Local = os.path.dirname(os.path.abspath(__file__))
caminho = f"{Local}\Downloads"

if os.path.exists(caminho):
    files = os.listdir(caminho)

else:
    os.mkdir(caminho)
    files = os.listdir(caminho)

config = configparser.ConfigParser()

config_file_path = os.path.join(Local, 'config.ini')

# Verifica se o arquivo config.ini existe
if os.path.exists(config_file_path):
    print("O arquivo config.ini existe.")
else:
    config['DEFAULT'] = {
        'LOCAL_INSTALACAO': None
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

    messagebox.showwarning("Atenção!", "Por favor vá nas configurações e configure o local de instalação")

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

def configuracao():

    def salvar(local):
        config.set("DEFAULT", "LOCAL_INSTALACAO", local)
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        messagebox.showinfo("Salvo!", "Salvo com sucesso!")

    configu = Tk()
    configu.title("Configuração")
    configu.geometry("300x200")
    
    texto = ttk.Label(configu, text="Caminho de instalação:")
    texto.grid(column=0, row=0)

    caminho = ttk.Entry(configu)
    caminho.grid(column=1, row=0)

    def lugar():
        ludar = filedialog.askdirectory()
        caminho.delete(0,END)
        caminho.insert(0, ludar)

    button = ttk.Button(configu, text="...", command=lugar)
    button.grid(column=2, row=0)

    limpar = ttk.Button(configu, text="Limpar Cookies", command=Api.clearCookies)
    limpar.grid(column=0, row=1)

    save = ttk.Button(configu, text="Salvar", command=lambda: salvar(caminho.get()))
    save.grid(column=2, row=1)

    caminho.config()
    configu.mainloop()

def arquivos():
    def instalar(baguio, lugat):
        with zipfile.ZipFile(f"{lugat}/{baguio}", 'r') as file:
            file.extractall(path=config["DEFAULT"]["LOCAL_INSTALACAO"])

        messagebox.showinfo("Instalado!", f"{baguio} instalado com sucesso!")

    def apagar(negocio, lugar):
        os.remove(path=f"{lugar}/{negocio}")
        messagebox.showinfo("Apagado!", f"{negocio} apagado com sucesso!")

    files = os.listdir(caminho)

    win = Tk()
    win.geometry("200x200")
    win.title("Downloads")

    istala = ttk.Button(win, text="Instalar", command=lambda: instalar(transform.get(), caminho))
    istala.grid(column=0, row=1)

    apag = ttk.Button(win, text="Apagar", command=lambda: apagar(transform.get(), caminho))
    apag.grid(column=0, row=2)

    if files == []:
        inicio = "Nenhum download"
        istala.config(state="disabled")
        apag.config(state="disabled")

    else:
        inicio = files[0]

    transform = StringVar(win)
    transform.set(inicio)

    lista = ttk.OptionMenu(win, transform, *files)
    lista.grid(column=0, row=0)


    win.mainloop()

webview.settings = {
  'ALLOW_DOWNLOADS': True,
  'ALLOW_FILE_URLS': True,
  'OPEN_EXTERNAL_LINKS_IN_BROWSER': False,
  'OPEN_DEVTOOLS_IN_DEBUG': True
}

view = webview.create_window('Drum Kits', 'https://drum-kit-uxbn.glide.page', js_api=Api(), draggable=True, background_color="#131315")

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