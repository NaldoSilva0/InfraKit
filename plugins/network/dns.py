import socket
from core.plugin import Plugin

class DNSPlugin(Plugin):
    def __init__(self):
        super().__init__("DNS", "Obtém informações DNS do alvo")

    def run(self, target):
        if target.startswith("http://"):
            target = target.replace("http://", '')

        elif target.startswith("https://"):
           target = target.replace("https://", '') 

        else:
            pass

        try:
            ip = socket.gethostbyname(target)
            status = "SUCESSO!"
            retornar = [status, ip]
    
            return retornar
        except:
            status = "ERRO!"
            texto = "Não foi possível resolver o domínio"
            retornar = [status, texto]
            return retornar

