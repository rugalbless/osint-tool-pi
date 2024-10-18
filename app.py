import random
import time
import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BuscaPerfilRedes:
    def __init__(self, nome_usuario):
        self.nome_usuario = nome_usuario
        self.sites_sociais = ["site:instagram.com", "site:facebook.com", "site:x.com"] #Pode ser adicionado mais redes sociais, é colocar o site entre parenteses
        self.api_key = "9aa992bc23abdb83713ef7ef71c64c0cd64db4f411374860506635a5a0f5eeea"  # Coloque aqui sua API key (Limite para 100 pesquisas, funciona somente em perfis públicos)

    def buscar_perfis(self):
        """Realiza a busca em sites de redes sociais para encontrar perfis com base no nome de usuário"""
        resultados = []
        
        for site in self.sites_sociais:
            consulta = f"{site} {self.nome_usuario}"
            print(f"Pesquisando: {consulta}")

            # Configura os parâmetros da pesquisa
            params = {
                "q": consulta,
                "api_key": self.api_key,
                "engine": "google"
            }

            # Faz a requisição para a SerpAPI
            resposta = requests.get("https://serpapi.com/search", params=params)

            if resposta.status_code == 200:
                resultados_pesquisa = resposta.json()
                
                # Processa os resultados da pesquisa
                for resultado in resultados_pesquisa.get('organic_results', []):
                    link = resultado.get('link')
                    if any(site.split(":")[1] in link for site in self.sites_sociais):
                        resultados.append(link)

            else:
                print(f"Erro na requisição: {resposta.status_code} - {resposta.text}")

            time.sleep(random.randint(5, 10))  # Evita atingir limites de requisição

        return resultados

class AplicativoBuscaPerfil:
    def __init__(self, root):
        self.root = root
        self.root.title("Busca de Perfis")
        self.root.geometry("400x300")
        
        self.label_usuario = tk.Label(root, text="Nome de usuário:")
        self.label_usuario.pack(pady=10)

        self.entrada_usuario = tk.Entry(root)
        self.entrada_usuario.pack(pady=5)

        self.botao_busca = tk.Button(root, text="Iniciar Busca", command=self.iniciar_busca)
        self.botao_busca.pack(pady=20)

        self.progresso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progresso.pack(pady=10)

    def salvar_resultados(self, resultados):
        """Salva os resultados em um arquivo de texto para consultas futuras"""
        nome_arquivo = f"{self.entrada_usuario.get()}_resultados.txt"
        with open(nome_arquivo, 'w') as f:
            for site in resultados:
                f.write(f"---------------------\n{site}\n")
        print(f"Resultados salvos em {nome_arquivo}")

    def iniciar_busca(self):
        nome_usuario = self.entrada_usuario.get()
        if nome_usuario:
            self.progresso['value'] = 0
            self.root.update()  # Atualiza a interface

            busca_perfil = BuscaPerfilRedes(nome_usuario)
            resultados = busca_perfil.buscar_perfis()
            
            # Simula o progresso de busca
            for i in range(100):
                time.sleep(0.1)  # Simulação do processo de pesquisa
                self.progresso['value'] += 1
                self.root.update()  # Atualiza a barra de progresso

            if resultados:
                texto_resultados = "\n".join(resultados)
                messagebox.showinfo("Resultado", f"Perfis encontrados:\n{texto_resultados}")
                self.salvar_resultados(resultados)  # Salva os resultados para consulta posterior
            else:
                messagebox.showinfo("Resultado", "Nenhum perfil encontrado.")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um nome de usuário.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoBuscaPerfil(root)
    root.mainloop()
