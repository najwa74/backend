from libs import welcome_massage, exit_program
from games import game
from tools import warung

def menu():
    user_option = int(input(f'menu program: \n1. Games \n2. Warung Mini \n3. Keluar program \nSilahkan pilih: '))
    if user_option == 1:
        game.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
    else:
        print("hanya bole pilih yag tersedia di menu!!")
    

def main():
    welcome_massage()
    menu()  
    exit_program()

if __name__ == '__main__':
    main()