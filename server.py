import wAPI
import socket
import threading
socket = socket.socket()
socket.bind(("192.168.1.107",2))
socket.listen()
def connection(client):
    global max_min, hours
    recv = client.recv(1024).decode()[2:]

    if recv == "get_next_hours":
        client.send(hours.encode())
    elif recv == "get_max_min_temp":
        backsend = max_min
        client.send(backsend.encode())
        print(backsend)
    else:
        print("unknown command:",recv)
def get_info():
    global max_min,hours
    while True:
        max_min = wAPI.get_max_min_temp()
        hours = wAPI.get_next_hours()

info_getter = threading.Thread(target=get_info,args=())

while True:
    (client,addr) =socket.accept()
    print("connected with: "+str(addr))
    thread = threading.Thread(target=connection,args=(client,))
    thread.start()