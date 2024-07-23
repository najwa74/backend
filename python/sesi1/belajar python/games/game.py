import random


def start():
    while True:
            
        tempat_berisi = random.randint(1, 3)

        bentuk_goa = "|_|"

        goa_kosong = [bentuk_goa] * 3
        goa = goa_kosong.copy()

        goa_kosong[tempat_berisi - 1] = "|0_0|"

        goa_kosong = ' '.join(goa_kosong)
        goa = ' '.join(goa)

        
        print(f'''coba perhatikan 3 goa dibawah !!
            {goa}
            ''')

        jawab = int(input('''di goa manakah yg berisi?: '''))

        while jawab > 3:
            jawab = int(input(f"jawablah dengan angka 1, 2, atau 3!!: "))

        if jawab == tempat_berisi:
            print(f'''{goa_kosong} \n yap benaar, goa tersebut berisi.''')
        else:
            print(f"{goa_kosong} \n goa tersebut kosong")
    
        play_again = input("\n \napakah anda ingin lanjut bermain? [y/n]!: ")
        if play_again == "n":
            break

    
if __name__ == '__main__':
    start()