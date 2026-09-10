import pyfiglet


def menu():
        print("═"*70)

        texto = pyfiglet.figlet_format("INFRAKIT", font='doom')
        print(texto)
        print(" 1. Scan                 ")
        print(" 2. Plugins              ")
        print(" 3. Histórico            ")
        print(" 4. OSINT                ")    
        print(" 5. Hardware Status      ")           
        print(" 0. Sair                 ")

        print("═"*70)

        resposta = input("Digite a opção que desejar: ")

        return resposta
