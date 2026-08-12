from core.plugin import Plugin
import os
import importlib



class Engine:


    def __init__(self):
        self.plugins = []
        self.load_plugins()



    def load_plugins(self):
        arquivos = os.listdir("plugins/network")

        for arquivo in arquivos:
             
             if arquivo.endswith(".py"):
                nome_modulo = arquivo[:-3]  
                caminho_modulo = f"plugins.network.{nome_modulo}"
                modulo = importlib.import_module(caminho_modulo)

                for nome in dir(modulo):
                    objeto = getattr(modulo, nome)
                    if isinstance(objeto, type):
                        if issubclass(objeto, Plugin) and objeto is not Plugin:
                            plugin = objeto()
                            self.plugins.append(plugin)

    def show_plugins(self):
        for plugin in self.plugins:
                print(f"Name: {plugin.name}")
                print(f"Description: {plugin.description}\n")

    def run(self, target):
        lista_plugin = []
        for plugin in self.plugins:
            try:

                resposta = plugin.run(target)
                lista_plugin.append([plugin.name, resposta])
                
            except:
                status = ""
                resposta = "Erro ao realizar o comando"
                status = "ERRO!"
                resposta = [status, resposta]
                lista_plugin.append([plugin.name, resposta])
        return lista_plugin


        