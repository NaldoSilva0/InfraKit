import socket
from core.plugin import Plugin
from core.result import PluginResult

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
            resultado = socket.gethostbyname(target)
            status = "SUCESSO!"
            retornar = PluginResult(self.name, status, resultado)
    
            return retornar
        except:
            status = "ERRO!"
            resultado = "Não foi possível resolver o domínio"
            retornar = PluginResult(self.name, status, resultado)

            
            return retornar

