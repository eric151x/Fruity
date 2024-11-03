from tkinter import *
import webview
import webview.menu as wm
from tkinter import filedialog
import os
from tkinter import messagebox
import zipfile
from tkinter import ttk

Local = os.path.dirname(os.path.abspath(__file__))
caminho = f"{Local}\Downloads"

if not os.path.exists(caminho):
    os.mkdir(caminho)
    files = os.listdir(caminho)

if not os.path.exists(f"{Local}\local.ini"):
    with open(f"{Local}\local.ini", "w") as arquivo:
        arquivo.write("")

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
        with open(f"{Local}\local.ini", "w") as arquivo:
            arquivo.write(local)
        messagebox.showinfo("Salvo!", "Salvo com sucesso!")

  
    configu = Tk()
    configu.title("Configuração")
    configu.geometry("330x100")
    
    texto = ttk.Label(configu, text="Caminho de instalação:")
    texto.grid(column=0, row=0)

    caminho = ttk.Entry(configu)
    caminho.grid(column=1, row=0)

    with open(f'{Local}\local.ini', 'r') as arquivo:
        conteudo = arquivo.read()
        caminho.delete(0,END)
        caminho.insert(0, conteudo)

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
    with open(f'{Local}\local.ini', 'r') as arquivo:
        conteudo2 = arquivo.read()

    if conteudo2 != "":
        def instalar(baguio, lugat):
            with zipfile.ZipFile(f"{lugat}/{baguio}", 'r') as file:
                file.extractall(path=conteudo2)

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
    else:
        messagebox.showinfo("Atenção!", "vá para configurações e adicione o local de instalação!")

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