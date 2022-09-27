# -*- coding: utf-8 -*-
from socket import *
import json

serverName = '192.168.1.8' # casa
#serverName = '192.168.1.17' # ext = 177.37.199.112 empresa
#serverName = '127.0.0.1'
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while 1:
	sentence = input('Client envia: ')
	clientSocket.send(sentence.encode())
	if sentence=="sair":
		print ("Sessao client finalizada !!!")
		clientSocket.close()  # SO FECHA A CONEXAO QUANDO ACABAR A CONVERSA
		break
	modifiedSentence = clientSocket.recv(1024).decode()
	print ('Server escreveu:', modifiedSentence)
	if modifiedSentence == "sair":
		print ("Servidor desconectado !!!")
		clientSocket.close()
		break
	
