from nasabah import nasabah
from datetime import datetime
from prettytable import PrettyTable


nasabah = nasabah('Fajri', saldo = 10000)
riwayat = nasabah.riwayat


class atm :
    def __init__(self) :
        self.pin_nasabah = nasabah.getPin()
        self.saldo_nasabah = nasabah.getSaldo()    
    
    def cekSaldo(self) :
        print('Saldo anda : Rp' + str(self.saldo_nasabah))

    def transaksi(self) :
        print('==============================================================')
        print('Pilihan menu :')
        print('1. Transfer')
        print('2. Tarik tunai')
        print('3. Simpan')
        input_menu = int(input('Masukkan pilihan menu : '))
        if input_menu == 1 :
            to_rekening = int(input('Masukkan nomor rekening  tujuan : '))
            nominal = int(input('Masukkan nominal : '))
            if (self.saldo_nasabah - nominal) >= 0 :
                self.saldo_nasabah -= nominal
                print('Proses transfer telah berhasil')
                tanggal = datetime.now()
                riwayat.append(['Transfer', datetime.now().strftime('%d-%m-%Y'), '-Rp'+str(nominal), 'Rp'+str(self.saldo_nasabah)])
                print('Sisa saldo anda : Rp' + str(self.saldo_nasabah))
            else :
                print('Saldo tidak mencukupi')
        elif input_menu == 2 :
            nominal = int(input('Masukkan nominal : '))
            if (self.saldo_nasabah - nominal) >= 0 :
                self.saldo_nasabah -= nominal
                tanggal = datetime.now()
                riwayat.append(['Tarik', datetime.now().strftime('%d-%m-%Y'), '-Rp'+str(nominal), 'Rp'+str(self.saldo_nasabah)])
                print('Sisa saldo anda : Rp' + str(self.saldo_nasabah))
            else :
                print('Saldo tidak mencukupi')
        elif input_menu == 3 :
            nominal = int(input('Masukkan nominal : '))
            self.saldo_nasabah += nominal
            tanggal = datetime.now()
            riwayat.append(['Simpan', datetime.now().strftime('%d-%m-%Y'), '+Rp'+str(nominal), 'Rp'+str(self.saldo_nasabah)])
            print('Sisa saldo anda : Rp' + str(self.saldo_nasabah))
        else :
            print('inputan salah')

    def gantiPin(self):
        pin_lama = int(input('Masukkan pin lama : '))
        if pin_lama == self.pin_nasabah:
            pin_baru = int(input('Masukkan pin yang baru : '))
            cek_pin = int(input('Masukkan kembali pin yang baru : '))
            if pin_baru == cek_pin :
                self.pin_nasabah = pin_baru
                nasabah.setPin(pin_baru)
                print('Pin berhasil diubah')
                # pin yang baru hanya bersifat sementara
                # karena tidak ada database yang berfungsi untuk menyimpan data
                pass
            else :
                print('Pin yang anda masukkan salah')
        else :
            print('Pin yang anda masukkan salah')
            index = False
    
    def riwayat(self):
        tabelku = PrettyTable(['Jenis', 'Tanggal', 'Nominal', 'Saldo'])
        for i in range(len(riwayat)):
            tabelku.add_row([riwayat[i][0], riwayat[i][1], riwayat[i][2], riwayat[i][3]])
        print(tabelku)
    
    
