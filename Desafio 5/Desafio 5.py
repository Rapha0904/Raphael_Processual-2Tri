nomes = []
caracteres_validos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

print("Por favor, digite 10 nomes:")

for i in range(10):
    while True:
        nome = input(f"Digite o {i+1}º nome: ")
        nome_valido = True
        for char in nome:
            if char not in caracteres_validos:
                print(f"Erro: O nome '{nome}' contém caracteres inválidos. Por favor, digite apenas letras e espaços.")
                nome_valido = False
                break
        if nome_valido:
            nomes.append(nome)
            break

print("\n--- Nomes Inseridos ---")
print(nomes)

# 4) Organize os nomes em ordem alfabética
nomes.sort()
print("\n--- Nomes em Ordem Alfabética ---")
print(nomes)

# 5) Para cada nome, printe a quantidade de letras de cada um
print("\n--- Quantidade de Letras por Nome ---")
for nome in nomes:
    print(f"O nome '{nome}' tem {len(nome)} letras.")