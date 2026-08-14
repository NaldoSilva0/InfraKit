
import time
from core.engine import Engine
from cli.menu import menu

engine = Engine()

def executar_scan():
        print("═"*70)
        print("╔═══════════════════════════╗")
        print("║           SCAN            ║")
        print("╚═══════════════════════════╝")
        alvo = input(f"\nDigite o domínio do scan: ")
        if alvo == '':
            print("\nDomínio inválido!")
            return
                        
        
        resultado = engine.run(alvo)
        for resultado_plugin in resultado:                        
           print(resultado_plugin)
        
        print("\n--Scan finalizado--\n")
        input("Pressione ENTER para retornar ao menu...")


def mostrar_plugins():
        print("═"*70)
        print("╔═══════════════════════════╗")
        print("║          PLUGINS          ║")
        print("╚═══════════════════════════╝")
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

        elif resposta == "0":
            print("Saindo de InfraKit...")
            time.sleep(1.0)
            break
        else:
            print("\nOpção inválida!")
            print("Escolha uma opção disponível.")
            continue


menu_controle()

        