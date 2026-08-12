import os

for raiz, diretorios, arquivos in os.walk("plugins"):
	for arquivo in arquivos:
		if arquivo.endswith(".py"):
			caminho = os.path.join(raiz, arquivo)

			nome_modulo = caminho[:-3]
			nome_modulo = nome_modulo.replace("/", ".")

			print(nome_modulo)
    			
