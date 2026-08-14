from core.plugin import Plugin
import os
import importlib
from core.result import PluginResult



class Engine:


    def __init__(self):
        self.plugins = []
        self.load_plugins()



    def load_plugins(self):
        for raiz, diretorios, arquivos in os.walk("plugins"):
             diretorios[:] = [d for d in diretorios if d != "__pycache__"]
             for arquivo in arquivos:
             

                if arquivo.endswith(".py"):
                    caminho = os.path.join(raiz, arquivo)
                    nome_modulo = caminho[:-3]
                    nome_modulo = nome_modulo.replace("/", ".")  
                    modulo = importlib.import_module(nome_modulo)

                    for nome in dir(modulo):
                        objeto = getattr(modulo, nome)
                        if self.is_plugin(objeto):
                            plugin = objeto()
                            self.plugins.append(plugin)

    def is_plugin(self, objeto):
            if isinstance(objeto, type):
                if issubclass(objeto, Plugin) and objeto is not Plugin:
                    return True
                else:
                    return False            
            return False                    
    def show_plugins(self):
        for plugin in self.plugins:
                print(f"Name: {plugin.name}")
                print(f"Description: {plugin.description}\n")

    def run(self, target):
        lista_plugin = []
        for plugin in self.plugins:
            try:
                
                resposta = plugin.run(target)
                
                status  =  resposta[0] 
                resposta =   resposta[1] 
                resultado = PluginResult(plugin.name, status, resposta)
                lista_plugin.append(resultado)
            except:
                status = resposta[0]
                resposta = "Erro ao realizar o comando"
                resultado = PluginResult(plugin.name, status, resposta)
                lista_plugin.append(resultado)
        return lista_plugin


        