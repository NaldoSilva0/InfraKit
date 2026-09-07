class PluginResult():
    def __init__(self, nome, status, resultado):
        self.nome = nome
        self.status = status
        self.resultado = resultado

    def __str__(self):
        resultado_final = ""

        if isinstance(self.resultado, dict):
            for chave, valor in self.resultado.items():
                resultado_final += f"{chave}:\n{valor}\n\n"                    
        else:
            resultado_final = str(self.resultado)

        return f"\n{self.nome}\nStatus: {self.status}\nResultado:\n{resultado_final}\n"