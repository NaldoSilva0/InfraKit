from datetime import datetime
import os

class Logger:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        caminho = "logs"
        caminho_arquivo = os.path.join(caminho)
        caminho = os.path.dirname(self.arquivo)

        os.makedirs(caminho_arquivo, exist_ok=True)

    def log(self, mensagem):
       with open(self.arquivo, "a", encoding="utf-8") as arquivo:
          data = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
          registro = (f"{data} | {mensagem}\n")
          arquivo.write(registro)

    def historico(self):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()