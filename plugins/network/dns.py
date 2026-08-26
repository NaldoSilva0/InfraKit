
import dns.resolver
from core.plugin import Plugin
from core.result import PluginResult

class DNSPlugin(Plugin):
    def __init__(self):
        super().__init__("DNS", "Obtém informações DNS do alvo")

    def consultar_dns(self, target):
        try:
            ipv4 = dns.resolver.resolve(target, "A")
        except dns.resolver.NoAnswer:
            ipv4 = []

        try:    
            ipv6 = dns.resolver.resolve(target, "AAAA")
        except dns.resolver.NoAnswer:
            ipv6 = []
        except dns.resolver.NXDOMAIN:
            raise
        except dns.resolver.Timeout:
            raise

        try:    
            mx = dns.resolver.resolve(target, "MX")
        except dns.resolver.NoAnswer:
            mx = []
        except dns.resolver.NXDOMAIN:
            raise
        except dns.resolver.Timeout:
            raise

        try:
            ns = dns.resolver.resolve(target, "NS")
        except dns.resolver.NoAnswer:
            ns = []
        except dns.resolver.NXDOMAIN:
            raise
        except dns.resolver.Timeout:
            raise

        try:
            txt = dns.resolver.resolve(target, "TXT")
        except dns.resolver.NoAnswer:
            txt = []
        except dns.resolver.NXDOMAIN:
            raise
        except dns.resolver.Timeout:
            raise

        try:
            cname = dns.resolver.resolve(target, "CNAME")
        except dns.resolver.NoAnswer:
            cname = []
        except dns.resolver.NXDOMAIN:
            raise
        except dns.resolver.Timeout:
            raise
        
        retornar_listas = (ipv4, ipv6, mx, ns, txt, cname)
        return retornar_listas




    def run(self, target):


        if target.startswith("http://"):
            target = target.replace("http://", '')

        elif target.startswith("https://"):
           target = target.replace("https://", '') 
        
        else:
            pass

        try:
            ipv4, ipv6, mx, ns, txt, cname = self.consultar_dns(target)

        except dns.resolver.NXDOMAIN:
            return PluginResult(self.name, "ERRO!", "O domínio não existe")
        except dns.resolver.Timeout:
           return PluginResult(self.name, "ERRO!","Não obtivemos uma resposta DNS dentro do tempo esperado")
            

        status = "SUCESSO!"   

        ipv4 = "\n".join(str(ip4) for ip4 in ipv4)
        ipv6 = "\n".join(str(ip6) for ip6 in ipv6)
        mx = "\n".join(str(m) for m in mx)
        ns = "\n".join(str(n) for n in ns)
        txt = "\n".join(str(tx) for tx in txt)
        cname = "\n".join(str(cna) for cna in cname)

        if not ipv4:
            ipv4 = "Nenhum registro encontrado"

        if not ipv6:
            ipv6 = "Nenhum registro encontrado"

        if not mx:
            mx = "Nenhum registro encontrado"

        if not ns:
            ns = "Nenhum registro encontrado"

        if not txt:
            txt = "Nenhum registro encontrado"

        if not cname:
            cname = "Nenhum registro encontrado"

            
        resultado = f"A:\n{ipv4}\n\nAAAA:\n{ipv6}\n\nMX:\n{mx}\n\nNS:\n{ns}\n\nTXT:\n{txt}\n\nCNAME:\n{cname}"

        retornar = PluginResult(self.name, status, resultado)    
        return retornar


