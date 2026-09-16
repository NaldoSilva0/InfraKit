import pyfiglet
import time
from core.engine import Engine
from cli.menu import menu
from core.database import listar_scans, listar_sessoes 
import json

engine = Engine()

def executar_osint():
        texto = pyfiglet.figlet_format("OSINT", font='doom')
        print(texto)
        print(" 1. Username (BETA)              ")
        print(" 2. Voltar                ") 

        



        opcao = input("Digite a opção que deseja: ")
        if opcao == "1":
            usuario_alvo = input(f"\nDigite o username: ")
            if usuario_alvo == "":
                print("\nUsername inválido!")
                return
            engine.run_plugin("Username", usuario_alvo)

            input("Pressione ENTER para retornar ao menu...")

def executar_hardconfig():
        texto = pyfiglet.figlet_format("HARDCONFIG", font='doom')
        print(texto)
        resposta = engine.run_plugin_no_target("HardConfig")
        print(resposta)
        input("Pressione ENTER para retornar ao menu...")
     
def executar_scan():

        texto = pyfiglet.figlet_format("SCAN", font='doom')
        print(texto)
        alvo = input(f"\nDigite o domínio do scan: ")
        if alvo == '':
            print("\nDomínio inválido!")
            return
                        
        
        resultado = engine.run(alvo)
        print("Executando plugins...")

        print(resultado)
        
        print("\n--Scan finalizado--\n")
        input("Pressione ENTER para retornar ao menu...")

def log_historico():
        print("═"*70)
        
        texto = pyfiglet.figlet_format("LOG", font='doom')
        print(texto)
        
        for id, alvo in listar_sessoes():
            print(f"Scan ID: {id} | Alvo: {alvo}")

        print("")

        while True:
            lista_sec = []
            sessoes = listar_sessoes()
            for id, alvo in sessoes:
                lista_sec.append(id)

            numero = input("\nDigite o id: ")
            if numero.isdigit():
                numero = int(numero)   

            if numero in lista_sec:
                break
            else:
                print("Digite um ID válido! ")                

        registros = listar_scans(numero)

        if registros:
            scan_id, id, alvo, plugin, status, resultado = registros[0]

            print("="*60)
            print(f"                          SCAN #{scan_id}")
            print("="*60)            
            print(f"Alvo: {alvo}")
            

            if not registros:
                print("Nenhum resultado encontrado")
                return
            for registro in registros:
                scan_id, id, alvo, plugin, status, resultado = registro

                print(f"\n[{id}] {plugin}")
                print(f"Status: {status}")
                print("Resultado: ")
    
                if plugin == "DNS":
                    resultado = json.loads(resultado)
                    for chave, valor in resultado.items():
                        print(f"\n[{chave}]:")
                       
                        if valor == "Nenhum registro encontrado":
                            print(valor)
                        else:
                            for registro_dns in valor.split("\n"):
                                print(f"• {registro_dns}")
                elif plugin == "PortScan":
                    print(f"{'Porta':<7} | {'Serviço':<7} | {'Status'}")
                    print("-" * 31)
                    for linha in resultado.split("\n"):
                        partes = linha.split()
                        porta = partes[0]
                        servico = partes[2]
                        status = partes[4]
                        print(f"{porta:<7} | {servico:<7} | {status}")
                
                elif plugin == "HTTP":
                    print(f"{'Processo':<15} | {'Resultado':<7}")
                    print('-'*31)
                    for linha in resultado.split("\n"):
                        partes = linha.split(":", 1)
                        processo = partes[0]
                        resul = partes[1]
                        print(f"{processo:<12} | {resul:<7}")

                else:
                    print(resultado)


                print("="*60)
        input("Pressione ENTER para retornar ao menu...")

def mostrar_plugins():
        print("═"*70)
        texto = pyfiglet.figlet_format("PLUGINS", font='doom')
        print(texto)
        engine.show_plugins()
        print("═"*70)
        input("Pressione ENTER para retornar ao menu...")

def menu_controle():
    while True:
        resposta = menu()

        if resposta == "2": 
            mostrar_plugins()

        elif resposta == "1":
            executar_scan()

        elif resposta == "3":
            log_historico()

        elif resposta == "4":
            executar_osint()

        elif resposta == "5":
            executar_hardconfig()

        elif resposta == "0":
            print("Saindo de InfraKit...")
            time.sleep(1.0)
            break
        else:
            print("\nOpção inválida!")
            print("Escolha uma opção disponível.")
            continue


menu_controle()

        