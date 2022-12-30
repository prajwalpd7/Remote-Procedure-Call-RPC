# Remote-Procedure-Call-RPC

# Remote Procedure Call Demonstration

This project contains a demonstration of Remote Procedure Call (RPC) using the `xmlrpc.server` and `os` modules in Python. The project includes a client and a server script, which communicate with each other over a network using the `socket` module.

## Prerequisites

To run this project, you will need to have Python installed on your computer.

## Running the Server

To start the server, use the following command:

$ python server.py


The server will listen for incoming RPC requests on a specified port (the default is 8000).

## Running the Client

To start the client, use the following command:

$ python client.py


The client will send an RPC request to the server and print the response.

## Customizing the RPC Function

The RPC function that is demonstrated in this project is the `os.listdir` function, which returns a list of the files and directories in a specified directory. You can customize the RPC function by modifying the `rpc_function` variable in the server script. For example, you could use a different function from the `os` module, or you could define your own custom function.

## Additional Notes

Remote Procedure Call is a powerful technique for allowing different programs or devices to communicate with each other over a network. This demonstration is just a simple example of the capabilities of RPC, and there are many other ways that RPC can be used in a variety of applications.
