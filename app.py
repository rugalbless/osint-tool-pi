import random
import time
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BuscaPerfilRedes:
    def __init__(self, nome_usuario):
        self.nome_usuario = nome_usuario
        self.sites_sociais = ["site:instagram.com", "site:facebook.com", "site:x.com"]  # Pode adicionar mais redes sociais
        self.api_key = "9aa992bc23abdb83713ef7ef71c64c0cd64db4f411374860506635a5a0f5eeea"  # Substitua pela sua chave da API  (Limite para 100 pesquisas, funciona somente em perfis públicos)

    def buscar_perfis(self):
        resultados = []

        for site in self.sites_sociais:
            consulta = f"{site} {self.nome_usuario}"
            print(f"Pesquisando: {consulta}")

            params = {
                "q": consulta,
                "api_key": self.api_key,
                "engine": "google"
            }

            resposta = requests.get("https://serpapi.com/search", params=params)

            if resposta.status_code == 200:
                resultados_pesquisa = resposta.json()

                for resultado in resultados_pesquisa.get('organic_results', []):
                    link = resultado.get('link')
                    if any(site.split(":")[1] in link for site in self.sites_sociais):
                        resultados.append(link)

            else:
                print(f"Erro na requisição: {resposta.status_code} - {resposta.text}")

            time.sleep(random.randint(5, 10))

        return resultados

class AplicativoBuscaPerfil:
    def __init__(self, root):
        self.root = root
        self.root.title("Busca de Perfis")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Estilo do ttk
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')

        # Frame principal
        self.frame_principal = ttk.Frame(self.root, padding="20")
        self.frame_principal.pack(fill="both", expand=True)

        # Título
        self.label_titulo = ttk.Label(self.frame_principal, text="Buscador de Perfis em Redes Sociais", font=("Helvetica", 16))
        self.label_titulo.pack(pady=10)

        # Campo de entrada
        self.label_usuario = ttk.Label(self.frame_principal, text="Nome de usuário:")
        self.label_usuario.pack(pady=5)

        self.entrada_usuario = ttk.Entry(self.frame_principal, width=30)
        self.entrada_usuario.pack(pady=5)

        # Botão de busca
        self.botao_busca = ttk.Button(self.frame_principal, text="Iniciar Busca", command=self.iniciar_busca)
        self.botao_busca.pack(pady=15)

        # Barra de progresso
        self.progresso = ttk.Progressbar(self.frame_principal, orient="horizontal", length=300, mode="determinate")
        self.progresso.pack(pady=10)

    def salvar_resultados(self, resultados):
        nome_arquivo = f"{self.entrada_usuario.get()}_resultados.txt"
        with open(nome_arquivo, 'w') as f:
            for site in resultados:
                f.write(f"{site}\n")
        print(f"Resultados salvos em {nome_arquivo}")

    def iniciar_busca(self):
        nome_usuario = self.entrada_usuario.get()
        if nome_usuario:
            self.progresso['value'] = 0
            self.root.update()

            busca_perfil = BuscaPerfilRedes(nome_usuario)
            resultados = busca_perfil.buscar_perfis()

            for i in range(100):
                time.sleep(0.05)
                self.progresso['value'] += 1
                self.root.update()

            if resultados:
                texto_resultados = "\n".join(resultados)
                messagebox.showinfo("Resultado", f"Perfis encontrados:\n{texto_resultados}")
                self.salvar_resultados(resultados)
            else:
                messagebox.showinfo("Resultado", "Nenhum perfil encontrado.")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um nome de usuário.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoBuscaPerfil(root)
    root.mainloop()
