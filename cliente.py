import socket

mi_socket = socket.socket()
mi_socket.connect( ('127.0.0.1', 9000) )  #direccion y puerto

mi_socket.send("hola desde el cliente") #linea para enviar informacion 
respuesta = mi_socket.recv(1024) #bufer o bites 

print respuesta 
mi_socket.close() 
