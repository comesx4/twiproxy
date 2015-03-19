# twiproxy
A Twisted based proxy server

# Server

Server is designed to listen from clients and commander, when commander send a command to the server, the server will send the command to the special client to excute and get the result when the client's timer connected to the server.

# Client

Client use a timer that with 1 second's interval to connect to the server. When the client receive the special command, it will excute the command and send the result to the server.

# Test

The test floder may has some test cases.

# ENVIRONMENT

Developing in VS2012 now.
