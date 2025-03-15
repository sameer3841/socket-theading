# TCP File Transfer with Multiple Clients

## Overview

I built this project to deepen my understanding of network programming and multithreading in Python. The goal was to take a simple TCP file transfer system and enhance it to handle multiple simultaneous clients. This meant implementing a multithreaded server that efficiently manages multiple file transfers at the same time.



## Why I Built This

I've always been interested in how large-scale systems handle network communication efficiently. File transfer is a fundamental networking problem, and I wanted to explore how to improve performance by leveraging Python's threading capabilities. This project gave me hands-on experience working with sockets, concurrency, and error handling.



## How It Works

### 1. The Original Single-Client Server

Initially, the server handled file transfers sequentially:

1. A client connects to the server.
2. The server receives a message containing the file name and size.
3. The server acknowledges with `b'go ahead'`.
4. The client sends the file in chunks, which the server writes to disk.
5. Once complete, the connection is closed, and the server waits for another client.

While this approach works, it limits performance because only one file transfer can happen at a time.



### 2. Upgrading to a Multithreaded Server

To allow multiple clients to transfer files simultaneously, I modified the server to spawn a new thread for each client connection. Now, the workflow is:

1. The server listens for incoming connections.
2. When a client connects, a new thread is created to handle the file transfer.
3. The main server continues listening for other clients while file transfers occur in parallel.

This improves performance by handling multiple transfers concurrently instead of sequentially.



## Testing

To ensure the server could handle multiple simultaneous clients, I:
- Ran multiple client instances sending different files at the same time.
- Introduced artificial delays to simulate real-world network latency.
- Verified that all files were received correctly without corruption.

The results confirmed that the server could efficiently manage multiple clients without blocking or crashing.



## Lessons Learned

- **Threading in Python:** Managing concurrent network connections with `threading.Thread`.
- **Error Handling:** Ensuring that incomplete file transfers don’t leave corrupted files.
- **Socket Programming:** Deepened my understanding of TCP sockets and file streaming.



## Next Steps

Some potential improvements I’d like to explore:
- Implementing an asynchronous version using `asyncio` for even better performance.
- Adding encryption to secure file transfers.
- Creating a graphical client interface for ease of use.



## Final Thoughts

This was a fun and rewarding project that gave me hands-on experience with network programming. If you're interested in working with sockets and multithreading, this is a great starting point!

