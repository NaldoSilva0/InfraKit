import requests
from core.plugin import Plugin

class HttpPlugin(Plugin):
    def __init__(self):
        super().__init__("HTTP", "Obtem informações básicas de um servidor http")

    def run(self, target):
        status = ""
        if target.startswith("http://") or target.startswith("https://"):
            pass
        else:
            target = "https://" + target

        try:
            resposta = requests.get(target)
            if resposta.status_code == 200:
                
                status = "SUCESSO!"
                resultado = "Requisição realizada com sucesso! código HTTP: 200"
                retornar = [status, resultado]
                return retornar
            elif resposta.status_code == 404:
                status = "ERRO!"
                resultado = "Recurso não encontrado! Código HTTP: 404"
                retornar = [status, resultado]
                return retornar
        except:
            status = "ERRO!"
            resultado = "Não foi possível realizar a requisição"
            retornar = [status, resultado]
            return retornar
