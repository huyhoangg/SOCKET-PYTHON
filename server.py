import socket
import threading
import main as f1

HOST = "192.168.1.8"
PORT = 20202
FORMAT = "utf8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(5)

clients = []
names = []

print("server is listening")

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024)
            broadcast(msg)
        except:
            index = clients.index(conn)
            clients.remove(conn)
            conn.close()
            name = names[index]
            broadcast(f'{name} has left the room !'.encode(FORMAT))
            break

def receive():
    while True:
        conn, addr = s.accept()
        print(f'{str(addr)} connected')

        conn.send('name'.encode(FORMAT))
        name = conn.recv(1024).decode(FORMAT)
        names.append(name)
        clients.append(conn)

        print(f'name of client is {name}')
        broadcast(f'{name} has joined the chat'.encode(FORMAT))
        conn.send('connected to chatroom'.encode(FORMAT))

        thread = threading.Thread(target = handle_client, args=(conn,))
        thread.start()

def register():
    while True:
        conn, addr = s.accept()
        print(f'{str(addr)} connected')

        username = conn.recv(1024).decode(FORMAT)

        if f1.checkUsername(username):
            conn.send('Existed username, try others :'.encode(FORMAT))
            print("")
            username = conn.recv(1024).decode(FORMAT)
            print("")
            psw = conn.recv(1024).decode(FORMAT)
            f1.writeInfo(username,psw)
        else:
            conn.send('Enter password :'.encode(FORMAT))
            psw = conn.recv(1024).decode(FORMAT)
            f1.writeInfo(username,psw)

        conn.send('Account created successfully'.encode(FORMAT))

        thread = threading.Thread(target=register)
        thread.start()




register()










