
import time
from core.engine import Engine
from cli.menu import menu

engine = Engine()

def menu_controle():
    while True:
        resposta = menu()

        if resposta == "2": 
            print("═"*70)
            print("╔═══════════════════════════╗")
            print("║          PLUGINS          ║")
            print("╚═══════════════════════════╝")
            engine.show_plugins()
            print("═"*70)
            input("Pressione ENTER para retornar ao menu...")
            
            continue

        elif resposta == "1":
                print("═"*70)
                print("╔═══════════════════════════╗")
                print("║           SCAN            ║")
                print("╚═══════════════════════════╝")
                alvo = input(f"\nDigite o domínio do scan: ")
                if alvo == '':
                    print("\nDomínio inválido!")
                    continue
                

                resultado = engine.run(alvo)
                for resultado_plugin in resultado:
                    print("-"*70)                            
                    print(f"\n{resultado_plugin[0]}\n")
                    print("-"*70)
                    print(f"Status: {resultado_plugin[1][0]}\n")
                    print(f"Resultado: {resultado_plugin[1][1]}\n")

                print("\n--Scan finalizado--\n")
                input("Pressione ENTER para retornar ao menu...")
                continue
        elif resposta == "0":
            print("Saindo de InfraKit...")
            time.sleep(1.0)
            break
        else:
            print("\nOpção inválida!")
            print("Escolha uma opção disponível.")
            continue


menu_controle()

        