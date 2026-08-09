from core.plugin import Plugin
import subprocess

class PingPlugin(Plugin):
    def __init__(self):
        super().__init__("Ping", "Realiza teste de conectividade")

    def run(self, target):
        try:
            status = ""
            print(f"Executando Ping em {target}")
            resposta = subprocess.run(["ping","-c", "2", target], capture_output=True, text=True)
            if resposta.returncode == 0:
                status = "SUCESSO!"
            else:
                status = "ERRO!"
                resposta.stdout = "Erro ao realizar o ping nesse domínio!"
            retornar = [status, resposta.stdout]
            return retornar
        
        except:
            status = ""
            mensagem = "Erro ao realizar o teste de conectividade"
            retornar = [status, resposta]
            return retornar