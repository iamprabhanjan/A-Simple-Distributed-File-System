





# Usage Guide

## Running the System

1. **Start the Master Node**

    ```bash
    python src/master_node.py
    ```

2. **Start Worker Nodes**

    ```bash
    python src/worker_node.py
    ```
    Run the above command in multiple terminals to simulate a distributed environment.

3. **Run the Client**

    ```bash
    python src/client.py
    ```

## Available Commands

- **Upload a File**

    ```plaintext
    Enter action (upload/download/delete/exit): upload
    Enter filename to upload: example.txt
    ```

- **Download a File**

    ```plaintext
    Enter action (download/delete/exit): download
    Enter filename to download: example.txt
    ```

- **Delete a File**

    ```plaintext
    Enter action (delete/exit): delete
    Enter filename to delete: example.txt
    ```

## Example Workflow

1. **Upload a File**

    ```plaintext
    Enter action: upload
    Enter filename: my_file.txt
    Output: my_file.txt uploaded to localhost:5001, localhost:5002
    ```

2. **Download a File**

    ```plaintext
    Enter action: download
    Enter filename: my_file.txt
    Output: my_file.txt downloaded successfully
    ```

3. **Delete a File**

    ```plaintext
    Enter action: delete
    Enter filename: my_file.txt
    Output: File deleted
    ```

## Further Exploration

- Explore the [Design Document](DESIGN.md).
