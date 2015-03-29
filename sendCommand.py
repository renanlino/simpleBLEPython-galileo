#!/bin/python
"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ Biblioteca Python para manipulacao de dispositivos Bluetooth LE  @
@ Renan Yuri Lino - renan.lino@gmail.com                           @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
from pygatt.pygatt import *
import bluetooth
import sys
import time
import readAddr

def main():
    
    try:
        if sys.argv[1] == "--h":
            print "Antes de utilizar: forneca o endereco MAC Bluetooth Low Energy (BLE) do dispositivo no arquivo bltAddrWearable.\n"
            print "Script sendCommand: Envia uma cadeia de caracteres qualquer para o dispositivo."
            print "Exemplo: python sendCommand.py LR255"
            return         
    except:
        print "Argumento inexistente. Use --h para obter ajuda."
	return

    bleBluetoothAddress = readAddr.main()

    if bleBluetoothAddress == 0:
        return
    
    command = sys.argv[1]
    reset_bluetooth_controller()
    time.sleep(0.1)
    bleDevice = BluetoothLeDevice(bleBluetoothAddress)
    bleHandler = 0x11
    bleDevice.char_write(bleHandler, bytearray(command))

main()
