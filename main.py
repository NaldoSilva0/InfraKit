import sys
import time
from core.engine import Engine

print(f"\n---InfraKit---")

time.sleep(0.5)

engine = Engine()

total_valores = len(sys.argv)


if total_valores == 1:

    print("\nSugestões de comandos: \n")
    print("python main.py scan <alvo>")
    print("python main.py plugins\n")

else:
    comando = sys.argv[1]

    if comando == "plugins": 
        print("~"*80)   
        engine.show_plugins()


    elif comando == "scan":
       if total_valores == 3:
            print(f"Comando: scan")
            print(f"Alvo: {sys.argv[2]}\n")

            resultado = engine.run(sys.argv[2])
            for resultado_plugin in resultado:
                print("-"*70)
                print(f"\n{resultado_plugin[0]}\n")
                print("-"*70)
                print(f"Status: {resultado_plugin[1][0]}\n")
                print(f"Resultado: {resultado_plugin[1][1]}\n")

            print("\n--Scan finalizado--\n")
       else:
           print("O comando precisa de um valor!")
           print("Exemplo: \n python main.py scan google.com")




        