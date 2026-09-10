import pyfiglet
import time
from core.engine import Engine
from cli.menu import menu
from core.database import listar_scans
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

        for registro in listar_scans():
            scan_id, id, alvo, plugin, status, resultado = registro
            print(f"Scan ID: {scan_id}")
            print(f"ID: {id}")
            print(f"Alvo: {alvo}")
            print(f"Plugin: {plugin}")
            print(f"Status: {status}")
            print(f"Resultado:")
        
    
            if plugin == "DNS":
                resultado = json.loads(resultado)
                for chave, valor in resultado.items():
                    print(f"{chave}:")
                    print(valor)
            else:
                print(resultado)






            print("-"*60)
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

        