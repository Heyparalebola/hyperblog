import random


def choose_option():
    options = ("piedra", "papel", "tijera")
    user_option = input("Elige entre piedra, papel o tijera => ")
    user_option = user_option.lower()

    if not user_option in options:
        print("Esa opción no es válida")
        # continue
        return None, None

    computer_option = random.choice(options)

    print("User option =>", user_option)
    print("(Computer option =>", computer_option)
    return (user_option, computer_option)

def check_rules (user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print ("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print ("Piedra gana a tijera")
            print ("El usuario ha ganado")
            user_wins += 1
        elif computer_option == "papel":
            print ("Papel gana a piedra")
            print ("La computadora ha ganado")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "tijera":
            print ("Tijera gana a papel")
            print ("La computadora ha ganado")
            computer_wins += 1
        elif computer_option == "piedra":
            print ("Papel gana a piedra")
            print ("El usuario ha ganado")
            user_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print ("Tijera gana a papel")
            print ("El usuario ha ganado")
            user_wins += 1
        elif computer_option == "piedra":
            print ("Piedra gana a tijera")
            print ("La computador ha ganado")
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
    
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print ('computer_wins', computer_wins)
        print ('user_wins', user_wins)
        rounds += 1
        
        user_option, computer_option = choose_option()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if user_wins == 2:
            print ('El ganador es el usuario')
            break
        if computer_wins == 2:
            print ('El ganador es el usuario')
            break
        
run_game()