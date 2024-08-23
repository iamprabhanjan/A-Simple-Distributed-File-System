# Distributed File System

![Distributed File System]

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Introduction

The Distributed File System (DFS) is a project that allows for the storage, management, and retrieval of files across multiple nodes in a network. This system is designed with essential features such as file replication, load balancing, fault tolerance, and advanced consistency mechanisms to ensure data integrity and availability even in the face of failures.

## Features

- **File Replication**: Automatically replicate files across multiple nodes to ensure redundancy and reliability.
- **Load Balancing**: Evenly distribute file storage and retrieval requests across nodes to optimize performance.
- **Fault Tolerance**: The system is resilient to node failures, ensuring that files remain accessible.
- **Consistency Mechanisms**: Advanced consistency management to prevent data corruption and ensure data accuracy.

## Architecture

### System Overview

The DFS is composed of the following key components:

1. **Master Node**: Manages the metadata, assigns tasks to worker nodes, and oversees file operations.
2. **Worker Nodes**: Store the actual files and communicate with the master node to handle requests.
3. **Client**: Provides the interface for users to interact with the distributed file system.


### Data Flow

1. **File Upload**: The client sends an upload request, the master node assigns worker nodes for storage, and the client uploads the file to those nodes.
2. **File Download**: The client requests a file, the master node provides the locations, and the client downloads the file from the designated worker node.
3. **File Deletion**: The client requests deletion, and the master node ensures that the file is removed from all relevant worker nodes.

## Installation

### Prerequisites

- **Python 3.7 or later**
- **pip** package manager

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/iamprabhanjan/A Simple distributed file system.git
    cd distributed_file_system
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the System**

    Start the master node, worker nodes, and client as described in the [Usage](#usage) section.

## Usage

### Running the System

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

### Available Commands

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

## Testing

### Running Tests

The project includes a comprehensive test suite to ensure all components function as expected.

1. **Run all tests**

    ```bash
    python -m unittest discover tests/
    ```

2. **Run a specific test**

    ```bash
    python tests/test_master_node.py
    ```

### Test Coverage

- **Master Node**: Tests for worker registration, file assignment, metadata management, and load balancing.
- **Worker Node**: Tests for file storage, retrieval, deletion, and health monitoring.
- **Client**: Tests for file upload, download, deletion, and consistency mechanisms.

## Project Structure

```plaintext
distributed_file_system/
│
├── src/
│   ├── master_node.py       # Master node logic
│   ├── worker_node.py       # Worker node logic
│   └── client.py            # Client logic
│
├── docs/
│   ├── README.md            # Main documentation
│   ├── INSTALLATION.md      # Installation guide
│   ├── USAGE.md             # Usage guide
│   └── DESIGN.md            # System design document
│
├── tests/
│   ├── test_master_node.py  # Tests for master node
│   ├── test_worker_node.py  # Tests for worker nodes
│   └── test_client.py       # Tests for client
│
├── .gitignore               # Files and directories to be ignored by Git
├── LICENSE                  # License for the project
└── requirements.txt         # Python dependencies
