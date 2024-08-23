import socket
import threading
import pickle
import os


WORKER_HOST = 'localhost'
WORKER_PORT = 0  


MASTER_HOST = 'localhost'
MASTER_PORT = 5000

def handle_client(conn, addr):
    print(f"Connected to client: {addr}")
    
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            
            command = pickle.loads(data)
            action = command['action']
            filename = command['filename']
            
            if action == 'upload':
                file_content = command['content']
                with open(filename, 'wb') as f:
                    f.write(file_content)
                
                conn.send(b"File uploaded")
                
            elif action == 'download':
                if os.path.exists(filename):
                    with open(filename, 'rb') as f:
                        file_content = f.read()
                    conn.send(file_content)
                else:
                    conn.send(b"File not found")
                
            elif action == 'delete':
                if os.path.exists(filename):
                    os.remove(filename)
                    conn.send(b"File deleted")
                else:
                    conn.send(b"File not found")
        
        except Exception as e:
            print(f"Error: {e}")
            break
        
    conn.close()

def register_with_master(worker_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((MASTER_HOST, MASTER_PORT))
        command = {
            'action': 'register',
            'worker_address': (WORKER_HOST, worker_port)
        }
        s.send(pickle.dumps(command))

def start_worker():
    worker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker.bind((WORKER_HOST, WORKER_PORT))
    worker.listen(5)
    worker_port = worker.getsockname()[1]
    print(f"Worker node listening on {WORKER_HOST}:{worker_port}")
    
    
    register_with_master(worker_port)
    
    while True:
        conn, addr = worker.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_worker()

