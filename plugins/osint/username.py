from core.plugin import Plugin
from core.result import PluginResult
import time
import random
import requests

enderecos = {
    "GitHub": { "url": 
               "https://github.com/",
                "metodo":
                "github"
               },

    "LinkedIn": {
        "url":
        "https://www.linkedin.com/in/",
        "metodo":
        "linkedin"
                 },

    "Facebook": {
        "url":
        "https://www.facebook.com/",
        "metodo":
        "facebook"
                 },

    "Reddit": {
        "url":
        "https://www.reddit.com/user/",
        "sufixo": "/about.json",
        "metodo":
        "reddit"
               },

    "TikTok": {
       "url":
        "https://www.tiktok.com/@",
        "metodo":
        "status"
               },
    "Instagram": {
        "url":
        "https://www.instagram.com/",
        "metodo":
        "instagram"
    }
}
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15"
]

class UsernamePlugin(Plugin):
    def __init__(self):
        super().__init__("Username", "Verifica a presença de um usuários em plataformas públicas")

    def get_headers(self):
            return {
                "User-Agent": random.choice(USER_AGENTS),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Cache-Control": "max-age=0",
            }

    def verificar_status(self, resposta):
        if resposta.status_code == 200:
            return "Possivelmente registrado!"
        elif resposta.status_code == 404:
            return "Não registrado!"
        else:
            return f"Não foi possível verificar (HTTP {resposta.status_code})"

    def verificar_github(self, resposta):
        if resposta.status_code == 200:
            return "Possivelmente registrado!"
        elif resposta.status_code == 404:
            return "Não registrado!"
        else:
            return f"Não foi possível verificar (HTTP {resposta.status_code})"

    def verificar_reddit(self, resposta):
        if resposta.status_code == 200:
            return "Possivelmente registrado!"
        elif resposta.status_code == 404:
            return "Não registrado!"
        return f"Não foi possível verificar"

    def verificar_instagram(self, resposta):
        texto = resposta.text.lower()
        if resposta.status_code == 404:
            return "Não registrado!"
        if any(x in texto for x in["Desculpe, esta página não está disponível", "página não disponível", "o link que você seguiu pode estar quebrado"]):
            return "Não registrado!"
        if resposta.status_code == 200:
            return "Possivelmente registrado!"
        return f"Não foi possível verificar (HTTP: {resposta.status_code}"

    def verificar_facebook(self, resposta):
        texto = resposta.text.lower()
        if resposta.status_code == 404:
            return "Não registrado!"
        if any(x in texto for x in["Desculpe, esta página não está disponível", "página não disponível", "o link que você seguiu pode estar quebrado"]):
            return "Não registrado!"
        if resposta.status_code == 200:
            return "Possivelmente registrado!"
        return f"Não foi possível verificar (HTTP: {resposta.status_code}"        

    def verificar_linkedin(self, resposta):
        texto = resposta.text.lower()
        if resposta.status_code == 404:
            return "Não registrado!"
        if any(x in texto for x in["Desculpe, esta página não está disponível", "página não disponível", "o link que você seguiu pode estar quebrado"]):
            return "Não registrado!"
        if resposta.status_code == 200:
            return "Possivelmente registrado!"
        return f"Não foi possível verificar (HTTP: {resposta.status_code}"

    def verificar_tiktok(self, resposta):
        texto = resposta.text.lower()
        if resposta.status_code == 404:
            return "Não registrado!"
        if any(x in texto for x in["Desculpe, esta página não está disponível", "página não disponível", "o link que você seguiu pode estar quebrado"]):                return "Não registrado!"
        if resposta.status_code == 200:
            return "Possivelmente registrado!"
        return f"Não foi possível verificar (HTTP: {resposta.status_code}"
        
    def run(self, target):
        usuario = target.strip()
        resultado = []
        session = requests.Session()

        try:
            for nome, dados in enderecos.items():
                url = dados["url"]
                sufixo = dados.get("sufixo", "")
                metodo = dados.get("metodo", "status")

                try:
                        headers = self.get_headers()
                        resposta = session.get(
                            f"{url}{usuario}{sufixo}",
                            headers=headers,
                            timeout=12,
                            allow_redirects=True
                        )



                        if metodo == "reddit":
                            situacao = self.verificar_github(resposta)

                        elif metodo == "github":
                            situacao = self.verificar_reddit(resposta)

                        elif metodo == "linkedin":
                            situacao = self.verificar_linkedin(resposta)

                        elif metodo == "facebook":
                            situacao = self.verificar_facebook(resposta)

                        elif metodo == "instagram":
                            situacao = self.verificar_instagram(resposta)

                        elif metodo == "tiktok":
                            situacao = self.verificar_tiktok(resposta)    

                        else:
                            situacao = self.verificar_status(resposta)

                        mensagem = f"""Plataforma: {nome}
        Usuário: {usuario}
        URL: {url}{usuario}{sufixo}
        Status HTTP: {resposta.status_code}
        Situação: {situacao}
        """    
                        resultado.append(mensagem)
                        print(mensagem)
                        

                except requests.RequestException as e:
                        resultado.append(f"Plataforma: {nome}\nErro: {str(e)}")

                time.sleep(random.uniform(1.2, 2.8))

            resultado_final = "\n\n" + ("-" * 50 + "\n\n").join(resultado)
            return PluginResult(self.name, "SUCESSO!", resultado_final)

        except Exception as e:
            return PluginResult(self.name, "ERRO!", f"Erro geral: {str(e)}")

