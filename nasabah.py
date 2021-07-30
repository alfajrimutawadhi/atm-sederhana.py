class nasabah :
    def __init__(self, nama, pin = 121212, saldo = 0):
        self.nama = nama
        self.pin = pin
        self.saldo = saldo

    riwayat = []

    def setPin(self, angka):
        self.pin = angka

    def getPin(self):
        return self.pin

    def setSaldo(self, nominal):
        self.saldo = nominal

    def getSaldo(self):
        return self.saldo

    def tambahRiwayat(self, data) :
        self.riwayat.append(data)

