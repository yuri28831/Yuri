meme_dict = {
    "STALKEAR": "Investigar a vida de alguem online",
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "VDD": "Abreviacao de 'verdade'",
    "BISCOITAR": "Postar algo para chamar atencao",
    "HATER": "Pessoa que critica os outros o tempo todo",
    "VLW": "Abreviacao de 'valeu'",
    "TBT": "Throwback Thursday - postar algo do passado",
    "SQN": "So que nao",
    "LOL": "Laughing out loud - rindo muito",
    "OMG": "Oh my God - meu Deus",
    "AFF": "Expressao de irritacao ou decepcao",
    "TOP": "Algo muito bom",
    "SHIPPAR": "Torcer para duas pessoas ficarem juntas",
    "FLW": "Falou",
    "BLZ": "Beleza",
    "TMJ": "Tamo junto",
    "PFV": "Por favor",
    "MSG": "Mensagem",
    "ADD": "Adicionar",
    "DM": "Mensagem privada",
    "BTW": "By the way - a proposito",
    "FDS": "foda-se",
    "GG": "Good game - bom jogo",
    "NOOB": "Pessoa iniciante em algo",
    "PARTIU": "Vamos embora ou vamos fazer algo",
    "MDDS": "Meu Deus",
    "BORA": "Vamos",
    "FOMO": "Medo de ficar de fora",
    "GRWM": "Get ready with me - arrume-se comigo",
    "POV": "Point of view - ponto de vista"
    }

print("👋 Olá! Bem-vindo ao Dicionário Moderno!")
print("Você pode pesquisar 5 palavras modernas.")
print("Digite sempre em LETRAS MAIUSCULAS.\n")

for i in range(5):
    word = input("Digite uma palavra: ")

    if word in meme_dict:
        print("Significado:", meme_dict[word])
    else:
        print("❌ Palavra não encontrada no dicionário.")

    print() 

print("Obrigado por usar o Dicionário Moderno!")
