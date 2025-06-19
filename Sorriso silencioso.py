import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

vida_maxima = 100
energia_maxima = 100

vida = vida_maxima
energia = energia_maxima
mochila = []
pontuacao = 0

itens = {
    "lanterna": {"tipo": "iluminação", "efeito": "permite ver no escuro"},
    "galho afiado": {"tipo": "arma", "efeito": "+10 ataque"},
    "bandagem": {"tipo": "cura", "efeito": "+20 vida"},
    "isqueiro": {"tipo": "fogo", "efeito": "assusta Jeff temporariamente"}
}

inimigos = {
    "Jeff the Killer": {"forca": 100, "velocidade": 90, "fala": "Go to sleep..."},
    "Sombra Silenciosa": {"forca": 60, "velocidade": 70, "fala": "..."}
}

def esperar(seg=3):
    time.sleep(seg)

def sorriso_jeff():
    print(Fore.RED + r'''
          .-"      "-.
         /            \
        |              |
        |,  .-.  .-.  ,|
        | )(_o/  \o_)( |
        |/     /\     \|
        (_     ^^     _)
         \__|IIIIII|__/
          | \IIIIII/ |
          \          /
           `--------`
            "Go to sleep..."''')

def exibir_menu():
    print(Fore.RED + "\nO Sorriso Silencioso")
    print("1. Iniciar Novo Jogo")
    print("2. Carregar Jogo")
    print("3. Opções")
    print("4. Sair")
    print("5. Quem é Jeff The Killer?")

def iniciar_novo_jogo():
    global vida, energia, mochila, pontuacao
    vida = vida_maxima
    energia = energia_maxima
    mochila = []
    pontuacao = 0
    print("Iniciando novo jogo...")
    esperar()
    inicio()

def carregar_jogo():
    try:
        with open("status.txt", "r") as arquivo:
            dados = arquivo.readlines()
            global vida, energia, mochila, pontuacao
            vida = int(dados[0])
            energia = int(dados[1])
            mochila = eval(dados[2])
            pontuacao = int(dados[3])
            print("Jogo carregado com sucesso!")
            inicio()
    except:
        print("Erro ao carregar jogo. Nenhum save encontrado.")

def mostrar_opcoes():
    print("Opções disponíveis no momento:")
    print("- Sobrevivência")
    print("- Exploração")
    print("- Fuga")

def jogo():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            iniciar_novo_jogo()
        elif escolha == '2':
            carregar_jogo()
        elif escolha == '3':
            mostrar_opcoes()
        elif escolha == '4':
            print("Saindo do jogo...")
            break
        elif escolha == '5':
            historia_jeff()
        else:
            print("Opção inválida. Tente novamente.")

def historia_jeff():
    print(Fore.RED + """
Jeff the Killer era um garoto comum até sofrer bullying e um ataque que o desfigurou.
Após um incêndio, ficou com a pele pálida e o rosto com um sorriso eterno.
Perdeu a sanidade, assassinou sua família e fugiu para a noite.
Desde então, aparece dizendo: 'Go to sleep...' antes de atacar.
""")
    esperar()

def salvar_status():
    with open("status.txt", "w") as arq:
        arq.write(f"{vida}\n{energia}\n{mochila}\n{pontuacao}")

def mostrar_mochila():
    print("\nItens na mochila:")
    for item in mochila:
        info = itens.get(item, {"tipo": "desconhecido", "efeito": "nenhum"})
        print(f"- {item.capitalize()} ({info['tipo']}): {info['efeito']}")
    print()

def inicio():
    print("Durante uma longa viagem, você passa por uma estrada deserta durante a noite.")
    esperar()
    print("Após um tempo dirigindo, você escuta o motor falhar...")
    esperar()
    print("...e o carro para completamente.")
    esperar()
    print("Você vê apenas uma floresta escura à sua direita.")
    esperar()
    print("Você sai do carro e verifica o motor.")
    esperar()
    escolha1()

def escolha1():
    print("\nO que você faz?")
    print("1 - Olha ao redor.")
    print("2 - Entra no carro.")
    print("3 - Entra na floresta.")
    escolha = input("Escolha 1, 2 ou 3: ")

    if escolha == "3":
        floresta()
    elif escolha == "1":
        print("Você olha ao redor, mas não encontra nada.")
        energia_gasta(5)
        esperar()
        print("Sons estranhos vêm da floresta...")
        print("\n1 - Entrar na floresta.")
        print("2 - Voltar para o carro.")
        nova = input("Escolha: ")
        if nova == "1":
            floresta()
        else:
            voltar_para_carro()
    elif escolha == "2":
        ficar_no_carro()
    else:
        print("Escolha inválida.")
        escolha1()

def floresta():
    print("\nVocê entra na floresta com cuidado.")
    esperar()
    print("Uma sensação estranha toma conta de você...")
    esperar()
    print("Passos rápidos se aproximam!")
    print("1 - Continuar andando.")
    print("2 - Esconder-se.")
    escolha = input("Escolha: ")

    if escolha == "1":
        energia_gasta(10)
        print("Você segue, mas uma figura pálida aparece.")
        esperar()
        if "isqueiro" in mochila:
            print("Você acende o isqueiro rapidamente!")
            print("Jeff recua e desaparece na escuridão.")
            pontuar(20)
            fim()
        else:
            vida_perdida(100)
            print(Fore.RED + inimigos["Jeff the Killer"]["fala"])
            sorriso_jeff()
            fim()
    elif escolha == "2":
        print("Você se esconde com sucesso.")
        esperar()
        print("Você encontra uma lanterna no chão.")
        mochila.append("lanterna")
        pontuar(10)
        print("\n1 - Voltar para o carro.")
        print("2 - Continuar explorando.")
        escolha = input("Escolha: ")
        if escolha == "1":
            voltar_para_carro()
        elif escolha == "2":
            explorar_floresta()
        else:
            floresta()

def explorar_floresta():
    print("Você encontra um galho afiado e o pega.")
    mochila.append("galho afiado")
    pontuar(10)
    print("Logo adiante, uma figura encapuzada aparece: a Sombra Silenciosa!")
    esperar()
    print(Fore.MAGENTA + inimigos["Sombra Silenciosa"]["fala"])
    esperar()
    if "galho afiado" in mochila:
        print("Você usa o galho como arma e acerta a criatura.")
        pontuar(30)
        print("Ela desaparece. Você sobreviveu.")
    else:
        vida_perdida(50)
        print("Você tenta correr, mas ela te fere.")
    fim()

def ficar_no_carro():
    print("Você espera horas... e então algo aparece na janela.")
    esperar()
    print(Fore.RED + '"Go to sleep..."')
    if "isqueiro" in mochila:
        print("Você usa o isqueiro e Jeff foge.")
        pontuar(25)
        fim()
    else:
        vida_perdida(100)
        sorriso_jeff()
        fim()

def voltar_para_carro():
    print("Você retorna ao carro assustado.")
    esperar()
    if "bandagem" in mochila:
        print("Você usa uma bandagem e recupera 20 de vida.")
        cura(20)
    print("Mas algo já está dentro do carro...")
    esperar()
    print(Fore.RED + inimigos["Jeff the Killer"]["fala"])
    vida_perdida(100)
    sorriso_jeff()
    fim()

def fim():
    salvar_status()
    print("\nFim de jogo.")
    print(f"Status: Vida {vida}, Energia {energia}, Pontuação {pontuacao}")
    mostrar_mochila()
    print("Deseja jogar novamente? (sim/não)")
    escolha = input("-> ").lower()
    if escolha == "sim":
        iniciar_novo_jogo()
    elif escolha == "não":
        creditos()
    else:
        fim()

def creditos():
    print("Jogo desenvolvido por Matheus Fuchs")
    esperar()
    print("Obrigado por jogar 'O Sorriso Silencioso'.")
    esperar()

def pontuar(pontos):
    global pontuacao
    pontuacao += pontos
    print(f"(+{pontos} pontos)")

def vida_perdida(valor):
    global vida
    vida -= valor
    if vida <= 0:
        vida = 0

def cura(valor):
    global vida
    vida += valor
    if vida > vida_maxima:
        vida = vida_maxima

def energia_gasta(valor):
    global energia
    energia -= valor
    if energia < 0:
        energia = 0
def inicio():
    print("Você dirige há horas por uma estrada solitária e sem sinal de celular.")
    esperar()
    print("O rádio chia estático, o céu se fecha, a noite se intensifica...")
    esperar()
    print("O motor falha e o carro para com um suspiro mecânico final.")
    esperar()
    print("Você desce... o ar está frio e a única coisa ao redor é uma floresta escura à sua direita.")
    esperar()
    print("Você abre o capô, esperando entender o problema.")
    esperar()
    print("Mas algo dentro de você já sabe: você não vai sair dali facilmente.")
    esperar()
    escolha1()

def escolha1():
    print("\nO que você faz?")
    print("1 - Procurar algo útil ao redor.")
    print("2 - Voltar ao carro e esperar.")
    print("3 - Entrar na floresta.")
    print("4 - Montar um abrigo improvisado próximo ao carro.")
    escolha = input("Escolha 1, 2, 3 ou 4: ")

    if escolha == "1":
        print("Você encontra um isqueiro caído na grama.")
        mochila.append("isqueiro")
        pontuar(10)
        esperar()
        print("O som da floresta parece te chamar...")
        floresta()
    elif escolha == "2":
        ficar_no_carro()
    elif escolha == "3":
        floresta()
    elif escolha == "4":
        montar_abrigo()
    else:
        print("Escolha inválida.")
        escolha1()

def montar_abrigo():
    global energia
    print("Você junta galhos, folhas e uma lona do porta-malas.")
    energia_gasta(15)
    pontuar(5)
    esperar()
    print("Você monta um abrigo rústico e se cobre do frio.")
    print("Durante a madrugada, sons vêm da floresta...")
    esperar()
    print("Mas algo protegeu você... talvez sorte.")
    sobreviver_amanhecer()

def floresta():
    print("Você caminha entre galhos, sentindo o peso da escuridão.")
    esperar()
    print("Uma figura parece surgir e desaparecer entre as árvores.")
    esperar()
    print("Você vê ao longe uma cabana de madeira, velha e com uma porta entreaberta.")
    print("1 - Ir até a cabana.")
    print("2 - Ignorar e continuar floresta adentro.")
    print("3 - Voltar ao carro.")
    escolha = input("Escolha 1, 2 ou 3: ")

    if escolha == "1":
        cabana()
    elif escolha == "2":
        alucinacoes()
    elif escolha == "3":
        voltar_para_carro()
    else:
        print("Escolha inválida.")
        floresta()

def cabana():
    print("Você entra na cabana... cheiro de madeira podre e sangue seco no ar.")
    esperar()
    print("Uma velha cama, uma prateleira vazia e... algo brilha no chão.")
    print("Você encontra uma bandagem.")
    mochila.append("bandagem")
    pontuar(10)
    print("Você ouve passos se aproximando da cabana...")
    esperar()
    if "isqueiro" in mochila:
        print("Você acende o isqueiro rapidamente e se esconde.")
        print("A figura hesita, recua e desaparece.")
        pontuar(20)
        fim()
    else:
        vida_perdida(100)
        print(Fore.RED + inimigos["Jeff the Killer"]["fala"])
        sorriso_jeff()
        fim()

def alucinacoes():
    print("Você começa a ouvir vozes... sussurros.")
    esperar()
    print("Sons familiares... sua mãe? sua própria voz?")
    esperar()
    print("Você vê vultos e começa a correr sem direção.")
    energia_gasta(20)
    print("1 - Parar e respirar.")
    print("2 - Continuar correndo.")
    escolha = input("Escolha 1 ou 2: ")

    if escolha == "1":
        print("Você respira fundo e se esconde entre as raízes de uma árvore enorme.")
        print("Você sobrevive até o amanhecer.")
        pontuar(30)
        sobreviver_amanhecer()
    elif escolha == "2":
        print("Você tropeça e rola por uma encosta.")
        vida_perdida(50)
        print("Ferido e sangrando, você vê Jeff se aproximar lentamente...")
        esperar()
        sorriso_jeff()
        fim()
    else:
        print("Escolha inválida.")
        alucinacoes()

def sobreviver_amanhecer():
    print("\nA luz do sol começa a romper as árvores...")
    esperar()
    print("Você sobreviveu à noite.")
    print("Mas algo dentro de você nunca mais será o mesmo.")
    pontuar(50)
    fim()

jogo()