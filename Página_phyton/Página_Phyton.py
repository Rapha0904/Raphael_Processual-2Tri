informacoes = {
    "Neurodivergencia": ["Autismo", "TDAH", "Dislexia"],
    "Profissionais": ["Psicólogo", "Terapeuta Ocupacional", "Psiquiatra"],
    "Comunidade": ["Famílias", "Pessoas Neurodivergentes", "Educadores"],
    "Categoria": ["Artigos", "Vídeos", "Cursos"],
    "Noticias": ["Nova pesquisa sobre autismo", "Evento sobre TDAH"]
}

def mostrar_filtros():
    print("\nFiltros disponíveis:")
    for filtro in informacoes:
        print(f" {filtro}")
    print("\nUse: 'abrir <Filtro>' para ver as opções.")

def abrir_filtro(filtro_digitado):
    # Ajusta para ignorar diferenças de maiúsculas/minúsculas
    filtro_digitado = filtro_digitado.lower()
    encontrado = False
    for filtro in informacoes:
        if filtro.lower() == filtro_digitado:
            print(f"\nOpções de {filtro}:")
            for item in informacoes[filtro]:
                print(f" - {item}")
            encontrado = True
            break
    if not encontrado:
        print("Filtro não encontrado.")
        print("Filtros disponíveis são:")
        for f in informacoes:
            print(f" - {f}")

def buscar(termo):
    print(f"\nBuscando por: '{termo}'...")
    resultados = []
    for categoria, itens in informacoes.items():
        for item in itens:
            if termo.lower() in item.lower():
                resultados.append((categoria, item))
    if resultados:
        print("Resultados encontrados:")
        for cat, res in resultados:
            print(f" - [{cat}] {res}")
    else:
        print("Nenhuma pesquisa realizada.")

# Instruções iniciais
print("Bem-vindo ao sistema de busca e filtros!")
print("\nComandos disponíveis:")
print(" - 'filtros' -> Mostrar filtros disponíveis.")
print(" - 'abrir <Filtro>' -> Abrir um filtro e ver as opções.")
print(" - 'buscar <termo>' -> Pesquisar um termo.")
print(" - 'sair' -> Encerrar o programa.")

# Loop principal
while True:
    comando = input("\nDigite um comando: ").strip()

    if comando.lower() == "filtros":
        mostrar_filtros()
    elif comando.lower().startswith("abrir "):
        filtro = comando[6:].strip()
        abrir_filtro(filtro)
    elif comando.lower().startswith("buscar "):
        termo = comando[7:].strip()
        buscar(termo)
    elif comando.lower() == "sair":
        print("\nSaindo... Até logo!")
        break
    else:
        print("Comando não reconhecido. Tente novamente usando 'filtros', 'abrir <Filtro>', 'buscar <termo>' ou 'sair'.")
        informacoes = {
    "Neurodivergencia": ["Autismo", "TDAH", "Dislexia"],
    "Profissionais": ["Psicólogo", "Terapeuta Ocupacional", "Psiquiatra"],
    "Comunidade": ["Famílias", "Pessoas Neurodivergentes", "Educadores"],
    "Categoria": ["Artigos", "Vídeos", "Cursos"],
    "Noticias": ["Nova pesquisa sobre autismo", "Evento sobre TDAH"]
}

def mostrar_filtros():
    print("\nFiltros disponíveis:")
    for filtro in informacoes:
        print(f" {filtro}")
    print("\nUse: 'abrir <Filtro>' para ver as opções.")

def abrir_filtro(filtro_digitado):
    # Ajusta para ignorar diferenças de maiúsculas/minúsculas
    filtro_digitado = filtro_digitado.lower()
    encontrado = False
    for filtro in informacoes:
        if filtro.lower() == filtro_digitado:
            print(f"\nOpções de {filtro}:")
            for item in informacoes[filtro]:
                print(f" - {item}")
            encontrado = True
            break
    if not encontrado:
        print("Filtro não encontrado.")
        print("Filtros disponíveis são:")
        for f in informacoes:
            print(f" - {f}")

def buscar(termo):
    print(f"\nBuscando por: '{termo}'...")
    resultados = []
    for categoria, itens in informacoes.items():
        for item in itens:
            if termo.lower() in item.lower():
                resultados.append((categoria, item))
    if resultados:
        print("Resultados encontrados:")
        for cat, res in resultados:
            print(f" - [{cat}] {res}")
    else:
        print("Nenhuma pesquisa realizada.")

# Instruções iniciais
print("Bem-vindo ao sistema de busca e filtros!")
print("\nComandos disponíveis:")
print(" - 'filtros' -> Mostrar filtros disponíveis.")
print(" - 'abrir <Filtro>' -> Abrir um filtro e ver as opções.")
print(" - 'buscar <termo>' -> Pesquisar um termo.")
print(" - 'sair' -> Encerrar o programa.")

# Loop principal
while True:
    comando = input("\nDigite um comando: ").strip()

    if comando.lower() == "filtros":
        mostrar_filtros()
    elif comando.lower().startswith("abrir "):
        filtro = comando[6:].strip()
        abrir_filtro(filtro)
    elif comando.lower().startswith("buscar "):
        termo = comando[7:].strip()
        buscar(termo)
    elif comando.lower() == "sair":
        print("\nSaindo... Até logo!")
        break
    else:
        print("Comando não reconhecido. Tente novamente usando 'filtros', 'abrir <Filtro>', 'buscar <termo>' ou 'sair'.")