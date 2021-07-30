from card import *

atm = atm()
trial = 0

while trial < 3:
    input_pin = int(input('Masukkan pin : '))
    if input_pin == atm.pin_nasabah :
        index = True
        while index :
            print('Selamat datang ' + nasabah.nama + ' di ATM PIPI.COM')
            print('==============================================================')
            print('Pilihan menu :')
            print('1. Cek Saldo')

            print('2. Transaksi')
            print('3. Ganti Pin')
            print('4. Riwayat Transaksi')
            print('5. Keluar\n')
            menu_input = int(input('Masukkan pilihan menu : '))

            if menu_input == 1 :
                atm.cekSaldo()
                
                index_menu = 0
                while index_menu == 0:
                    input_lanjutan = input('Apakah ingin melanjutkan transaksi (y/n) ? :')
                    if input_lanjutan == 'y' :
                        print('==============================================================')
                        index_menu = 1
                        index = False
                    elif input_lanjutan == 'n' :
                        trial = 3
                        index = False
                        break
                    else :
                        print('inputan salah')
                

            elif menu_input == 2 :
                atm.transaksi()
                
                index_menu = 0
                while index_menu == 0:
                    input_lanjutan = input('Apakah ingin melanjutkan transaksi (y/n) ? :')
                    if input_lanjutan == 'y' :
                        print('==============================================================')
                        index_menu = 1
                        index = False
                    elif input_lanjutan == 'n' :
                        trial = 3
                        index = False
                        break
                    else :
                        print('inputan salah')

            elif menu_input == 3 :
                atm.gantiPin()
                
                index_menu = 0
                while index_menu == 0:
                    input_lanjutan = input('Apakah ingin melanjutkan transaksi (y/n) ? :')
                    if input_lanjutan == 'y' :
                        print('==============================================================')
                        index_menu = 1
                        index = False
                    elif input_lanjutan == 'n' :
                        trial = 3
                        index = False
                        break
                    else :
                        print('inputan salah')

            elif menu_input == 4 :
                atm.riwayat()

                index_menu = 0
                while index_menu == 0:
                    input_lanjutan = input('Apakah ingin melanjutkan transaksi (y/n) ? :')
                    if input_lanjutan == 'y' :
                        print('==============================================================')
                        index_menu = 1
                        index = False
                    elif input_lanjutan == 'n' :
                        trial = 3
                        index = False
                        break
                    else :
                        print('inputan salah')
                        
            elif menu_input == 5 :
                print('Terima Kasih :)')
                index = False
                trial = 3

            else :
                print('inputan salah')

    else :
        print('Pin yang anda masukkan salah')
        trial += 1
        if trial == 3 :
            print('silahkan masukkan ulang kartu ATM anda')
            break

        
        
