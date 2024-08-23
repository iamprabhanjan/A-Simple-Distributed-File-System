import socket
import pickle


MASTER_HOST = 'localhost'
MASTER_PORT = 5000

def upload_file(filename):
    with open(filename, 'rb') as f:
        file_content = f.read()
    
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((MASTER_HOST, MASTER_PORT))
        command = {
            'action': 'upload',
            'filename': filename
        }
        s.send(pickle.dumps(command))
        worker_addresses = pickle.loads(s.recv(1024))
    
    if worker_addresses:
        for worker_host, worker_port in worker_addresses:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((worker_host, worker_port))
                command = {
                    'action': 'upload',
                    'filename': filename,
                    'content': file_content
                }
                s.send(pickle.dumps(command))
                response = s.recv(1024)
                print(f"{filename} uploaded to {worker_host}:{worker_port}")

def download_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((MASTER_HOST, MASTER_PORT))
        command = {
            'action': 'download',
            'filename': filename
        }
        s.send(pickle.dumps(command))
        workers = pickle.loads(s.recv(1024))
    
    if workers:
        for worker_host, worker_port in workers:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((worker_host, worker_port))
                command = {
                    'action': 'download',
                    'filename': filename
                }
                s.send(pickle.dumps(command))
                file_content = s.recv(1024)
                
                if file_content != b"File not found":
                    with open(f'downloaded_{filename}', 'wb') as f:
                        f.write(file_content)
                    print(f"{filename} downloaded successfully from {worker_host}:{worker_port}")
                    break
        else:
            print("File not found on any worker")
    else:
        print("File not found")

def delete_file(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((MASTER_HOST, MASTER_PORT))
        command = {
            'action': 'delete',
            'filename': filename
        }
        s.send(pickle.dumps(command))
        response = s.recv(1024)
        print(response.decode())

if __name__ == "__main__":
    while True:
        action = input("Enter action (upload/download/delete/exit): ").strip().lower()
        
        if action == 'upload':
            filename = input("Enter filename to upload: ").strip()
            upload_file(filename)
        elif action == 'download':
            filename = input("Enter filename to download: ").strip()
            download_file(filename)
        elif action == 'delete':
            filename = input("Enter filename to delete: ").strip()
            delete_file(filename)
        elif action == 'exit':
            break
        else:
            print("Invalid action. Please try again.")
