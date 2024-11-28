import tkinter as tk
import pyautogui
import keyboard
import time

# Lista de frases pré-definidas
frases = [
    
]

# Função para simular a digitação do texto selecionado
def digitar_frase(frase):
    time.sleep(0.5)  # Tempo para posicionar o cursor no local desejado
    pyautogui.typewrite(frase, interval=0.05)   

# Função para abrir a janela de seleção de frases
def abrir_seletor():
    # Cria a janela principal
    janela = tk.Tk()
    janela.title("Selecione uma frase")
    janela.geometry("600x400")

    # Adiciona os botões para cada frase
    for frase in frases:
        tk.Button(
            janela, 
            text=frase, 
            command=lambda f=frase: [digitar_frase(f), janela.destroy()]
        ).pack(pady=5, fill="x")

    janela.mainloop()

# Configurar um atalho global para abrir o seletor
keyboard.add_hotkey("ctrl+space", abrir_seletor)

# Mensagem para o usuário
print("Pressione Ctrl + Space para abrir o menu de frases.")

# Manter o script em execução
keyboard.wait("esc")  # O script para ao pressionar "ESC"
