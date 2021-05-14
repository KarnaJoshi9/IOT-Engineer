import socket
import pandas as pd
def client_program():
    # data=pd.read_csv("E:\\Prachi\\HTTP Server\\Notebook\\dataset.csv")
    #
    # print(data.shape[0])
    # for row_i in range(0,data.shape[0]):
    #     print(data.iloc[row_i])
    #     print()
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input(" -> ")
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input(" ->  ")
    client_socket.close()

if __name__ == '__main__':
    client_program()
