from random import randint


#Criando os quartos
def main():
    global hotel_rooms
    hotel_rooms = {}
    for floor_number in range(1, 7):
        for room_number in range(1, 10):
            if room_number < 10:
                concatenation = f"{str(floor_number)}0{str(room_number)}" 
            else:
                concatenation = f"{str(floor_number)}{str(room_number)}"
            hotel_rooms[concatenation] = room_viability()
    check_viability()
    

#Checando se os quartos estão ocupados ou não usando um sistema de randomização
def room_viability():
    available = randint(1,10)
    if available > 4:
        return True
    else:
        return False


#Checando se o quarto escolhido pelo usuário está livre ou não
def check_viability():
    print("Bem vindo ao nosso Hotel! Antes de pegar seu quarto, cheche a disponibilidade dos quartos até achar um vazio que o sirva bem!")
    room = input("Qual número do quarto que quer checar? Nota: Temos 6 andares com 10 quartos cada! ").strip().upper()
    try:
        while True:
            print(hotel_rooms[room])

            #Caso o quarto esteja ocupado, o usuário deve tentar escolher um novo quarto até achar algum disponível
            if hotel_rooms[room] is not True:
                print("Este quarto está ocupado. Tente checar outro.\n")
                room = input("Qual número do quarto que quer checar? Nota: Temos 6 andares com 10 quartos cada! ").strip().upper()
            #Caso o quarto esteja livre, o usuário tem a escolha de alugar o quarto ou não, levando ao fim do programa
            else:
                print("Este quarto está livre! Deseja alugá-lo? [YES/NO]\n")
                answer = input("R: ").strip().upper()
                if answer == "YES":
                    print(f"Você alugou o quarto {room}.")
                    hotel_rooms[room] = False
                else:
                    break
    #Em caso do jogador escolher um quarto inexistente, o sistema avisa e para
    except KeyError:
        print("Número de quarto inválido.")

main()