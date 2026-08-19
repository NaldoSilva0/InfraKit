from core.plugin import Plugin
import subprocess
from core.result import PluginResult

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
            resultado = subprocess.run(["ping","-c", "2", target], capture_output=True, text=True)
            if resultado.returncode == 0:
                status = "SUCESSO!"
                retornar = PluginResult(
                    self.name,
                    status,
                    resultado.stdout)
                return retornar
            else:
                status = "ERRO!"
                resultado.stdout = "Erro ao realizar o ping nesse domínio!"
            retornar = PluginResult(self.name, status, resultado.stdout)
            
            return retornar
        
        except:
            status = "ERRO!"
            resultado = "Erro ao realizar o teste de conectividade"
            retornar = PluginResult(self.name, status, resultado)
            
            return retornar