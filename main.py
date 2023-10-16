import random
import customtkinter as ctk



def gerar_numeros():
    aposta = random.sample(range(1, 61), 6)
    aposta.sort()
    for i in range(6):
        canvas.itemconfig(circles[i], outline='black', fill='green')  # Preenche os círculos
        canvas.itemconfig(numbers[i], text=str(aposta[i]), fill='white')  # Atualiza a cor do numero


# Criando a janela
janela = ctk.CTk()
ctk.set_appearance_mode("Light")
janela.title("Gerador de apostas para a Mega-Sena")
janela.resizable(False,False)


canvas = ctk.CTkCanvas(janela, width=400, height=100)
canvas.pack()

circles = []  # Armazena referencia aos circulos
numbers = []  # Armazena referencia aos numeros

for i in range(6):
    circle = canvas.create_oval(50 + i * 50, 50, 90 + i * 50, 90, outline='white', width=1)
    text = canvas.create_text(70 + i * 50, 70, text='', font=('Arial', 16, 'bold'))
    circles.append(circle)  # Add a referencia do circulo na lista
    numbers.append(text)  # Add a referencia do numero na lista

botao = ctk.CTkButton(janela, text="Gerar números", command=gerar_numeros, fg_color='green')
botao.pack()

janela.mainloop()