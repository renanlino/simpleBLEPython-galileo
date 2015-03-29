"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Biblioteca Python para manipulacao de dispositivos Bluetooth LE  @
@ Renan Yuri Lino - renan.lino@gmail.com                           @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Script auxilixar para leitura do endereco BLE do dispositivo
"""

def main():
    try:
        addrFile = open("bltAddr","r")
    except IOError:
        print("Leitura do endereco BLE falhou!")
        return 0
    bleBluetoothAddress = addrFile.readline()
    addrFile.close()
    bleBluetoothAddress = bleBluetoothAddress.split()[0]

    return bleBluetoothAddress
