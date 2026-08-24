class PluginResult():
    def __init__(self, nome, status, resultado):
        self.nome = nome
        self.status = status
        self.resultado = resultado

    def __str__(self):
        return f"\n{self.nome}\nStatus: {self.status}\nResultado:\n{self.resultado}\n"