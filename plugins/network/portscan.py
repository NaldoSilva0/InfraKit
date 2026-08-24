from core.plugin import Plugin
from core.result import PluginResult
import socket

lista_portas = {
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP"
}

class PortScan(Plugin):
    def __init__(self):
               
        super().__init__("PortScan", "Verifica portas de rede específicas")

    def run(self, target):
        resultados = []
        

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for porta, servico in lista_portas.items():
                s.settimeout(1)
                analise = s.connect_ex((target, porta))
                
                if analise == 0:
                    resposta = f"{porta:<5} | {servico:<6} | ABERTA"
                    resultados.append(resposta)
                else:
                    resposta = f"{porta:<5} | {servico:<6} | FECHADA"
                    resultados.append(resposta)
            status = "SUCESSO!"
            resultado_final = "\n".join(resultados)

            s.close()
            retornar = PluginResult(self.name, status, resultado_final)
            return retornar
             
        except Exception:
            status = "ERRO"
            resultado_final = "Erro ao realizar o comando!"


            s.close()
            retornar = PluginResult(self.name, status, resultado_final)
        
        return retornar