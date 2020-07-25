import wAPI
import socket
import threading
socket = socket.socket()
socket.bind(("192.168.1.107",2))
socket.listen()
def connection(client):
    recv = client.recv(1024).decode()[2:]

    if recv == "get_next_hours":
        client.send(wAPI.get_next_hours().encode())
    elif recv == "get_max_min_temp":
        backsend = wAPI.get_max_min_temp()
        client.send(backsend.encode())
        print(backsend)
    else:
        print("unknown command:",recv)
while True:
    (client,addr) =socket.accept()
    print("connected with: "+str(addr))
    thread = threading.Thread(target=connection,args=(client,))
    thread.start()