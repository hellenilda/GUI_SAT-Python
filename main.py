import tkinter as tk
from tkinter import *

largura, altura = 650, 400

tela = tk.Tk()
tela.geometry(f'{largura}x{altura}')
tela.title('SATA')

Label(tela,text='PC 1').place(x=42,y=altura/2)
Label(tela,text='PC 2').place(x=largura/2,y=altura/2)
Label(tela,text='PC 3').place(x=325,y=altura/2)

tela.mainloop()
