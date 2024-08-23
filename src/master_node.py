import socket
import threading
import pickle
import random


MASTER_HOST = 'localhost'
MASTER_PORT = 5000


metadata = {}
worker_nodes = []

REPLICATION_FACTOR = 2  

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            command = pickle.loads(data)
            action = command['action']
            
            if action == 'register':
                worker_address = command['worker_address']
                worker_nodes.append(worker_address)
                print(f"Registered worker node: {worker_address}")
                
            elif action == 'upload':
                filename = command['filename']
                worker_addresses = random.sample(worker_nodes, min(REPLICATION_FACTOR, len(worker_nodes)))
                
                if filename not in metadata:
                    metadata[filename] = []
                metadata[filename].extend(worker_addresses)
                
                conn.send(pickle.dumps(worker_addresses))
                print(f"File {filename} stored at {worker_addresses}")
                
            elif action == 'download':
                filename = command['filename']
                if filename in metadata:
                    conn.send(pickle.dumps(metadata[filename]))
                else:
                    conn.send(pickle.dumps([]))
                    
            elif action == 'delete':
                filename = command['filename']
                if filename in metadata:
                    del metadata[filename]
                    conn.send(b"File deleted")
                else:
                    conn.send(b"File not found")
        
        except Exception as e:
            print(f"Error: {e}")
            break
        
    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((MASTER_HOST, MASTER_PORT))
    server.listen(5)
    print(f"Master node listening on {MASTER_HOST}:{MASTER_PORT}")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
