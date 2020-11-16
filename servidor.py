import socket

mi_socket = socket.socket()
mi_socket.bind(('127.0.0.1', 9000)) #direccion y puerto 
mi_socket.listen(5) #mensales o conexiones que va a escuchar el servidor 

while True:
	conexion, addr= mi_socket.accept()
	print "CLIENTE CONECTADO"
	print addr

	conexion.send("HOLA, SOY EL SERVIDOR") #linea para recibir informacion 
	respuesta = conexion.recv(1024) #bufer o bites #linea para enviar informacion 
	print respuesta 
	print "cliente desconectado"	
	conexion.close
	
