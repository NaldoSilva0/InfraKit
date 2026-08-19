class ScanResult:
    def __init__(self, target, resultados):
        self.target = target
        self.resultados = resultados

    def __str__(self):
        resultados = "\n".join(
            str(resultado) for resultado in self.resultados)
        return f"{self.target}\n{resultados}"
