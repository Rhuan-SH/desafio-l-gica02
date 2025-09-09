import random 

pontuacao = 0
nomeHeroi = input("Digite o nome do seu herói: ")
print(f"Bem-vindo, {nomeHeroi}! Vamos começar sua jornada ranqueada.")
print("Você começará no rank Ferro. Boa sorte!")

def classificar_ranqueadas(pontuacao):
    if pontuacao < 10:
        return "Ferro"
    elif pontuacao >= 10 and pontuacao < 20:
        return "Bronze"
    elif pontuacao >= 20 and pontuacao < 50:
        return "Prata"
    elif pontuacao >= 50 and pontuacao < 80:
        return "Ouro"
    elif pontuacao >= 80 and pontuacao < 90:
        return "Platina"
    elif pontuacao >= 90 and pontuacao < 100:
        return "Diamante"
    else:
        return  "Imortal"

while True:
    resultado = random.choice(["vitória", "derrota"])
    if resultado == "vitória":
        pontuacao += random.randint(5, 15)
        print(f"Parabéns, {nomeHeroi}! Você venceu a partida e ganhou pontos.")
    else:
        pontuacao -= random.randint(3, 10)
        if pontuacao < 0:
            pontuacao = 0
        print(f"Infelizmente, {nomeHeroi}, você perdeu a partida e perdeu pontos.")
    
    rank_atual = classificar_ranqueadas(pontuacao)
    print(f"Sua pontuação atual é {pontuacao}. Seu rank atual é {rank_atual}.")
    
    continuar = input("Deseja jogar outra partida? (s/n): ")
    if continuar.lower() != 's':
        print(f"Obrigado por jogar, {nomeHeroi}! Até a próxima.")
        break

print(f"Seu rank final é {rank_atual} com {pontuacao} pontos.")