import requests
from core.plugin import Plugin
from core.result import PluginResult

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
            codigo = resposta.status_code
            servidor = resposta.headers.get("server")
            tipo = resposta.headers.get("Content-Type")
            hsts = resposta.headers.get("Strict-Transport-Security", "Não encontrado")

            if codigo:
                status = "SUCESSO!"
                resultado = f"HTTP: {codigo}\nServer: {servidor}\nContent-Type: {tipo}\nHSTS: {hsts}"
                retornar = PluginResult(self.name, status, resultado)
                return retornar
            
            else:
                status = "ERRO!"
                resultado = "Erro ao realizar a conexão/requisição"
                retornar = PluginResult(self.name, status, resultado)
                return retornar
        except:
            status = "ERRO!"
            resultado = "Não foi possível realizar a requisição"
            return PluginResult(self.name, status, resultado)

