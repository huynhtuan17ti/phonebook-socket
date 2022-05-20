import socket
from threading import Thread
import socket as sk
from tkinter import messagebox
import tkinter as tk
from server_utils import *

# ---- HANDLING CLIENT ---
def accept_incoming_connections():
    '''
        Sets up handling for incoming clients
    '''
    try:
        while True:
            # Get client information
            client, client_address = SERVER.accept()

            # print client in console and server app interface
            client_connected = "%s: %s has connected." % client_address
            print("%s:%s has connected." % client_address)
            SERVER_APP.insertMsg(client_connected)
            
            # Start communicate with client
            Thread(target=handle_client, args=(client, client_address)).start()
    except:
        # Error from server or client
        msg = "Error"
        SERVER_APP.insertMsg(msg)

def handle_client(client, client_address):
    '''
        Handles a single client connection
    '''
    welcome = f'Welcome {client_address}!'

    # Send welcome to client
    client.send(welcome.encode(cfg['FORMAT']))
    wait_response(client, cfg['FORMAT'])
    clients[client] = client_address

    try:
        msg = None
        # why loop for handing requests from client here
        while True:
            # Send request to client
            request = 'Please tell me your request!'
            client.send(request.encode(cfg['FORMAT']))
            # Receive message from client
            msg = client.recv(1024).decode(cfg['FORMAT'])
            print(client_address, ': ', msg)

            if msg == "all data":
                send_phone_book_data(client)
                
            if msg == 'all thumbnails':
                send_thumbnails(client)
            
            if msg == "close":
                raise Exception('Client closed!')
            
            token = msg.split()
            if token[0] == 'detail':
                send_user_interface(client, token[1])
                
            if token[0] == 'image':
                send_user_image(client, token[1])
            
    except:
        # Client disconnected to server
        msg = "%s: %s has disconnected." % client_address
        for sock in clients:
            if sock == client:
                del clients[sock]
                break
        SERVER_APP.insertMsg(msg)
    
    # close client
    client.close()

# ---- SERVER APP UI ----
class ServerApp(tk.Tk):
    '''
    Server application: Giao diện server sử dụng tkinter
    Hiện lên các thông báo về kết nối của client
    '''
    def __init__(self):
        tk.Tk.__init__(self)

        # Khởi tạo khung của cửa sổ server
        self.title("Server")
        self.geometry("400x600")
        self.resizable(width=False, height=False)

        # Lấy thông tin {hostname} và {ip_address} của thiết bị sử dụng làm server
        hostname = sk.gethostname()
        ip_address = sk.gethostbyname("")

        # In ra màn hình giao diện của server
        hostname_label = tk.Label(self, text=f"Hostname: {hostname}")
        ip_address_label = tk.Label(self, text=f"IP Address: {ip_address}")
        hostname_label.pack()
        ip_address_label.pack()

        tk.Button(self, text = "Disconnect to all clients", command = self.disconnect_clients,font=('Times New Roman', 10), bg="crimson", fg="white").pack(pady=15)

        # Khởi tạo Listbox hiển thị thông tin client thông qua {server_list}
        scrollbar = tk.Scrollbar(self, orient="vertical")
        self.server_list = tk.Listbox(self, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.server_list.yview)

        scrollbar.pack(side= tk.RIGHT, fill=tk.Y)
        self.server_list.pack(side=tk.LEFT, fill= tk.BOTH, expand=True)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # Nhận {msg} làm argument
    # {msg} là một string message
    def insertMsg(self, msg):
        '''Chèn {msg} vào Listbox'''
        self.server_list.insert(tk.END, msg)
    
    # Handle nút ngừng kết nối tới tất cả clients
    def disconnect_clients(self):
        if clients == {}:
            self.server_list.insert(tk.END, "No clients available")
            return

        for sock in clients.keys():
            sock.send(bytes("disconnect", cfg['FORMAT']))

    def on_closing(self):
        if messagebox.askokcancel("Quit server", "Do you want to quit?"):
            for sock in clients.keys():
                sock.send(bytes("disconnect", cfg['FORMAT']))
            # self.destroy()
            # sys.exit()
            self.quit()
            quit()

if __name__ == '__main__':
    clients = {} # store multiple clients
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP

    SERVER.bind((cfg['HOST'], cfg['SERVER_PORT']))
    SERVER.listen(5)

    print("[SEVER SIDE]")
    print("Server:", cfg['HOST'], cfg['SERVER_PORT'])
    print('='*40)

    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.daemon = True
    ACCEPT_THREAD.start()

    # Khởi động giao diện server
    SERVER_APP = ServerApp()
    SERVER_APP.mainloop()

    SERVER.close()