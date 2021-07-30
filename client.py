import socket
import threading

HOST = "192.168.1.8"
PORT = 20202
FORMAT = "utf8"

username = input("please enter your name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode(FORMAT)
            if msg == 'name':
                client.send(username.encode(FORMAT))
            else:
                print(msg)
        except:
            print("error dectected")
            client.close()
            break

def write():
    while True:
        msg = f'{username} :{input("")}'
        client.send((msg.encode(FORMAT)))

def register():

    print('[Register]')

    username = input("Enter username :")
    client.send(username.encode(FORMAT))
    print("")

    msg = client.recv(1024).decode(FORMAT)

    if msg == "Existed username, try others :":
        print(msg)
        username = input("")
        client.send(username.encode(FORMAT))
        print('Enter password :')
        psw = input("")
        client.send(psw.encode(FORMAT))
    else:
        print(msg)
        psw = input("")
        client.send(psw.encode(FORMAT))

    msg = client.recv(1024).decode(FORMAT)
    print(msg)



register_thread = threading.Thread(target=register)
register_thread.start()



'''


receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()
'''


