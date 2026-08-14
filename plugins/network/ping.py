from core.plugin import Plugin
import subprocess

class PingPlugin(Plugin):
    def __init__(self):
        super().__init__("PING", "Realiza teste de conectividade")

    def run(self, target):
        if target.startswith("http://"):
            target = target.replace("http://", '')

        elif target.startswith("https://"):
            target = target.replace("https://", '')

        else:
            pass

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
            status = "ERRO!"
            mensagem = "Erro ao realizar o teste de conectividade"
            retornar = [status, mensagem]
            return retornar