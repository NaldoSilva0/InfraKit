from core.plugin import Plugin
from core.result import PluginResult
import psutil



class HardConfig(Plugin):
    def __init__(self):
        super().__init__("HardConfig", "Mostra as informações internas do seu computador", "computer")

        

    def barra(self, porcentagem, tamanho=20):
        concluido = int(tamanho * porcentagem // 100)
        restante = tamanho - concluido
        return f"[{'█' * concluido}{'-' * restante}] {porcentagem:.1f}%"

    def uso_cpu(self):
        cpus_perc = psutil.cpu_percent(percpu=True, interval=1)
        cpus_total = psutil.cpu_percent(interval=None)
        return cpus_perc, cpus_total


    def uso_ram(self):
        ram = psutil.virtual_memory()
        ram_uso = ram.used / (1024**3)
        ram_total = ram.total / (1024**3)
        return ram, ram_uso, ram_total


    def uso_armazenamento(self):
        disco = psutil.disk_usage("/")
        disco_uso = disco.used / (1024**3)
        disco_total = disco.total / (1024**3)
        return disco, disco_total, disco_uso
    
    def uso_rede(self):
        rede = psutil.net_io_counters()
        enviados = rede.bytes_sent / (1024 ** 2)
        recebidos = rede.bytes_recv / (1024 ** 2)
        return rede, enviados, recebidos
        

    def run(self):
        try:

            _, ram_uso, ram_total = self.uso_ram()
            ram_porcentagem = (ram_uso / ram_total) * 100
            ram_barra = self.barra(ram_porcentagem)

            _, cpus_total = self.uso_cpu()
            cpu_barra = self.barra(cpus_total)     

            _, disco_total, disco_uso = self.uso_armazenamento()
            disco_porcentagem = (disco_uso / disco_total) *100
            disco_barra = self.barra(disco_porcentagem)

            _, enviados, recebidos = self.uso_rede()


            resultado = [
            f"╔══════════════════════════════════════════════════════╗",
            f"║ RAM                                                  ║",
            f"╠══════════════════════════════════════════════════════╣",            
            f"║ RAM Total:  {ram_total:.2f}GB                                   ║",
            f"║ RAM Usando:  {ram_uso:.2f}GB                                  ║",
            f"║ RAM Barra: {ram_barra}              ║",
            f"╠══════════════════════════════════════════════════════╣",
            f"║ CPU                                                  ║",
            f"╠══════════════════════════════════════════════════════╣",            
            f"║ CPU Total:  {cpus_total:.1f}%                                    ║",            
            f"║ CPU Barra:  {cpu_barra}             ║",      
            f"╠══════════════════════════════════════════════════════╣",
            f"║ ARMAZENAMENTO                                        ║",
            f"╠══════════════════════════════════════════════════════╣",  
            f"║ DISCO Total:  {disco_total:.2f}GB                               ║",
            f"║ DISCO Usando:  {disco_uso:.2f}GB                               ║",
            f"║ DISCO Barra: {disco_barra}            ║",       
            f"╠══════════════════════════════════════════════════════╣",
            f"║ REDE                                                 ║",
            f"╠══════════════════════════════════════════════════════╣",
            f"║ BYTES Enviados:  {enviados:.2f}MB                             ║",
            f"║ BYTES Recebidos:  {recebidos:.2f}MB                            ║",
            f"╚══════════════════════════════════════════════════════╝"
            ]

            resultado_final = "\n".join(resultado)

            retornar = PluginResult(self.name, "SUCESSO!", resultado_final)
            return retornar
        except Exception as e:
            resultado_final = f"Erro ao realizar as instruções {str(e)}"
            retornar = PluginResult(self.name, "ERRO!", resultado_final)
            return retornar
