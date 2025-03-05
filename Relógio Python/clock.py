
import tkinter as tk
from time import strftime

# Função para atualizar o horário
def atualizar_horario():
    horario_atual = strftime('%H:%M:%S')  # Formato de 24 horas
    label_relogio.config(text=horario_atual)
    label_relogio.after(1000, atualizar_horario)  # Atualiza a cada 1 segundo

# Configuração da janela
janela = tk.Tk()
janela.title("Relógio Digital")
janela.geometry("300x300")  # Janela quadrada
janela.configure(bg="black")  # Fundo preto

# Label para exibir o horário
label_relogio = tk.Label(janela, font=("Arial", 40), fg="white", bg="black")
label_relogio.pack(expand=True)  # Centraliza o relógio na janela

# Inicia a atualização do horário
atualizar_horario()

# Inicia o loop principal da interface gráfica
janela.mainloop()