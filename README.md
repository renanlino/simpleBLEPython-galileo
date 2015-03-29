#Biblioteca para comando de dispositivos Bluetooth Low Energy

##0) Observações importantes
- Esta biblioteca foi desenvolvida para uso com a Intel Galileo Gen 2 rodando o Intel IoT Developer Kit 1.0. Saiba mais em https://software.intel.com/en-us/iot/downloads

##1) Requisitos
- Intel Galileo Gen 2 (não testado na Gen 1, mas não há nada que impeça o uso)
- Sistema Intel IoT Developer Kit 1.0 devidamente instalado
- Dispositivo Bluetooth devidamente instalado e configurado na Intel Galileo
- Acesso ao terminal do Linux na Intel Galileo (via Ethernet, Wifi, Serial ou PoorMansTelnet)

##2) Dependências
- Esta biblioteca inclui na pasta *deps* os módulos Python necessários para execução dos scripts:
	- pexpect
	- ptyprocess
	- pybluez
- No IoT Developer Kit 1.0 não há nenhuma outra dependência pendente

##3) Instalação
1. Copie para o cartão SD de seu sistema Yocto em uma pasta conveniente (ex. /home/root/simpleBLEPython) todos os arquivos desta biblioteca
2. Pela linha de comando do Yocto, execute a instalação de cada um dos módulos Python incluídos na pasta *deps*:
	- Abra a pasta correspondente
	- Execute o comando: $ python setup.py install

##4) Utilizando a biblioteca
- Antes de utilizar a biblioteca escreva o endereço MAC Low Energy de seu dispositivo Bluetooth no arquivo bltAddr com o seguinte formato de exemplo: 00:0E:0B:00:39:AA (você pode utilizar um editor de texto comum caso esteja em um computador convencional ou o comando *vi* no Yocto - altamente não recomendado).
- IMPORTANTE: Antes de executar o script é preciso habilitar o dispositivo Bluetooth na Intel Galileo! Utilize a seguinte sequência de comandos no terminal, supondo que seu dispositivo Bluetooth esteja endereçado no Linux como *hci0*:
	- $ rfkill unblock all
	- $ hciconfig hci0 up
- O script aceita o argumento *--h* para exibir um resumo de sua função e um exemplo de utilização

##5) Referência rápida
1. sendCommand.py
	- Envia a cadeia de caracteres passada como argumento para o dispositivo BLE. 
	- Argumentos: Uma cadeia de caracteres, sem espaço
	- Uso: python sendCommand.py cadeiaDeCaracteres
