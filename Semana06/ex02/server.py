#Importa as bibliotecas necessárias
import socket 
import threading

#Define o número de bytes a serem recebidos vindos do servidor
HEADER = 64

#Define a porta de comunicação
PORT = 5050

#Define SERVER como o ip atual
SERVER = socket.gethostbyname(socket.gethostname())

#Associa o servidor à porta de comunicação por meio da variável ADDR
ADDR = (SERVER, PORT)

#Define o formato de codificação binária UFT-8
FORMAT = 'utf-8'

#Define a mensagem de desconexão
DISCONNECT_MESSAGE = "!DISCONNECT"

#Especifica qual o tipo de endereço IP aceito para conexão e indica o streaming de dados
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Vincula o socket ao endereço ADDR
server.bind(ADDR)

#Define uma função para configurar a conexão entre o servidor e cliente
def handle_client(conn, addr):
    #Gera uma mensagem para a conexão
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        
        #Define o número de bytes da mensagem
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            
            #Converte para uma variável inteira o número de bytes
            msg_length = int(msg_length)
            
            #Atribui a mensagem à uma variável
            msg = conn.recv(msg_length).decode(FORMAT)
            
            #Verifica a mensagem recebida
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            #Imprime o endereço do cliente e a mensagem
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))
            
    #Finaliza a conexão
    conn.close()
        
#Define uma função que permite vizualizar e administrar as conexões do servidor
def start():
    
    #Função para checar o servidor
    server.listen()
    
    #Mostra o status do servidor
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    while True:
        #Conexões admitidas pelo servidor
        conn, addr = server.accept()
        
        #Thead que envia conexões para o handle_client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        
        #Inicia a thread
        thread.start()
        
        #Mostra as conexões ativas
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

#Indica a inicialização do servidor
print("[STARTING] server is starting...")
start()