playersstats = {}
playersname = []
player = {}
matches = 0
goals = {}
totalgoals = 0 

while True:
    nump = int(input("Digite quantos jogadores deseja adicionar: "))
    if nump <= 0:
        break
    for c in range(0, nump):
        name = str(input(f"Insira o nome do {c+1}º jogador: "))
        playersname.append(name)
        player["Nome"] = name
        matches = int(input(f"Insira quantas partidas {name} jogou: "))
        player["Partidas jogadas"] = matches
        for c in range(0, matches):
            goals[f"{c+1}º jogo"] = intgol = int(input(f"Insira quantos gols {name} fez no {c+1}º jogo: "))
            totalgoals += intgol
        player["Gols Totais"] = totalgoals
        player["Gols por partida"] = goals
        playersstats[f"{name}"] = player
        player = {}
        goals = {}
        totalgoals = 0
        matches = 0
    end = str(input("Deseja adicionar mais jogadores? [S/N]\nR: ")).upper()
    if end in "N":
        print(f"Estes são os jogadores:\n\n{playersname}")
        print(f"\nCaso queira ver as estatísticas de algum jogador, digite o número que corresponde à posição em que o jogador aparece nessa lista")
        print("Caso não queira ver nenhuma estatística, digite 999.")
        stats = int(input("\nR: "))
        if stats != 999:
            print(list(playersstats.values())[stats])
            end = str(input("Deseja continuar? [S/N]\nR: ")).upper()
            if end in "N":
                break
        else:
            break
    