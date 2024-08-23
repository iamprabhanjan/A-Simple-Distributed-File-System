# System Design

## Overview

This document provides a detailed overview of the architecture, components, and workflows of the Distributed File System (DFS).


### Components

1. **Master Node**
   - Responsible for managing metadata, assigning tasks, and ensuring replication and load balancing.
   
2. **Worker Nodes**
   - Store files, handle file operations, and report to the master node.
   
3. **Client**
   - Provides the interface for users to interact with the DFS.

### Data Flow

1. **Upload Process**
   - Client sends a request to upload a file.
   - Master node selects worker nodes and informs the client.
   - Client uploads the file to the selected workers.

2. **Download Process**
   - Client sends a download request to the master node.
   - Master node provides the locations of the file.
   - Client downloads the file from one of the workers.

3. **Delete Process**
   - Client requests the deletion of a file.
   - Master node removes metadata and instructs workers to delete the file.

### Replication Strategy

The system uses a replication factor of `2`, meaning each file is stored on two different worker nodes to ensure redundancy and fault tolerance.

### Consistency Management

The master node ensures that all metadata is consistent across the system. Advanced consistency mechanisms such as versioning and conflict resolution could be implemented in future iterations.

### Fault Tolerance

The system is designed to continue functioning even if some worker nodes fail. The master node tracks the status of worker nodes and reroutes requests to ensure continuous operation.

## Future Improvements

- Implement sharding for better scalability.
- Add dynamic load balancing based on real-time metrics.
- Enhance the consistency mechanism with quorum-based voting.
