from tkinter import *
import main
import time, sys

janela = Tk()
txt = Entry(janela, width=10)

def clicked():
    # chama funcao em main pra inicializar
    lbl = Label(janela, text='vai votar: {}'.format(txt.get()))
    main.init(int(txt.get()))
    
    lbl.grid(column=0, row=2)

def criarJanela():
    janela.title("Bot")
    janela.geometry('350x200+500+200')

    lbl = Label(janela, text="Digite a quantidade de vezes pra votar: ")
    lbl.grid(column=0, row=0)
    txt.grid(column=0, row=1)
    btn = Button(janela,command=clicked, text="Click Aqui", bg="orange", bd=1, fg="red")
    btn.grid(column=1, row=1)

    janela.mainloop()

criarJanela()