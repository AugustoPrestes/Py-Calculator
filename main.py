# Importando as dependencias
from tkinter import *
from tkinter import ttk

# import de cores
cor1 = "#51515c"  # Chumbo Escuro
cor2 = "#ffffff"  # Branco
cor3 = "#40188f"  # Lilás
cor4 = "#525254"  # Cinza claro
cor5 = "#bf430a"  # Laranja


janela = Tk()
janela.title("Py-Calculadora")
janela.geometry("400x479")
janela.config(bg=cor1)


# Frame do display
frame_display = Frame(janela, width=400, height=100, bg=cor1)
frame_display.grid(row=0, column=0)

# Frame do teclado
frame_tecla = Frame(janela, width=400, height=495)
frame_tecla.grid(row=1, column=0)


todos_valores = ""

valor_texto = StringVar()

# Criando a lógica da calculadora
# Funcao para printar os numeros
def print_valor(evento):

    global todos_valores

    todos_valores = todos_valores + str(evento)

    # Passando o valor para o display
    valor_texto.set(todos_valores)

# Funcao que calcula os numeros
def calcular():

    global todos_valores

    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))


# Funcao limpa o display
def limpar_display():

    global todos_valores

    todos_valores = ''
    valor_texto.set("")


# Label

app_label = Label(frame_display, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 30 bold'), bg=cor1, fg=cor2)
app_label.place(x=0, y=0)

# Tabela de Botões

# Linha 1
b_1 = Button(frame_tecla, command = lambda: limpar_display() ,text="C", width=23, height=4, bg=cor5, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=2, y=2)
b_2 = Button(frame_tecla, command = lambda: print_valor('%'), text="%", width=10, height=4, bg=cor3, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=188, y=2)
b_3 = Button(frame_tecla, command = lambda: print_valor('/'), text="/", width=15, height=4, bg=cor3, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=279, y=2)

# Linha 2
b_4 = Button(frame_tecla, command = lambda: print_valor('9'), text="9", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=2, y=78)
b_5 = Button(frame_tecla, command = lambda: print_valor('8'), text="8", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=93, y=78)
b_5 = Button(frame_tecla, command = lambda: print_valor('7'), text="7", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=188, y=78)
b_6 = Button(frame_tecla, command = lambda: print_valor('+'), text="+", width=15, height=4, bg=cor3, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=279, y=78)

# Linha 3
b_7 = Button(frame_tecla, command = lambda: print_valor('6'), text="6", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=2, y=152)
b_8 = Button(frame_tecla, command = lambda: print_valor('5'), text="5", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=93, y=152)
b_8 = Button(frame_tecla, command = lambda: print_valor('4'), text="4", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=188, y=152)
b_9 = Button(frame_tecla, command = lambda: print_valor('-'), text="-", width=15, height=4, bg=cor3, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=279, y=152)

# Linha 4
b_10 = Button(frame_tecla, command = lambda: print_valor('3'), text="3", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=2, y=226)
b_11 = Button(frame_tecla, command = lambda: print_valor('2'), text="2", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=93, y=226)
b_11 = Button(frame_tecla, command = lambda: print_valor('1'), text="1", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=188, y=226)
b_12 = Button(frame_tecla, command = lambda: print_valor('%'), text="<=", width=15, height=4, bg=cor3, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=279, y=226)

# Linha 5
b_13 = Button(frame_tecla, command = lambda: print_valor('0'), text="0", width=23, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=2, y=300)
b_11 = Button(frame_tecla, command = lambda: print_valor('.'), text=".", width=10, height=4, bg=cor4, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=188, y=300)
b_12 = Button(frame_tecla, command = lambda: calcular() , text="=", width=15, height=4, bg=cor3, fg=cor2, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=279, y=300)



janela.mainloop()