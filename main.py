import tkinter as tk
import webbrowser

def pesquisar():
    termo = entrada.get()
    if termo:
        url = f"https://www.google.com/search?q={termo}"
        webbrowser.open(url)

janela = tk.Tk()
janela.title("Pesquisa no Google")

instrucao = tk.Label(janela, text="Digite algo para pesquisar no Google:")
instrucao.pack(pady=10)

entrada = tk.Entry(janela, width=50)
entrada.pack(pady=5)

botao_pesquisar = tk.Button(janela, text="Pesquisar", command=pesquisar)
botao_pesquisar.pack(pady=10)

janela.mainloop()
