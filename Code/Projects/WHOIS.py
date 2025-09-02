## Followed https://www.youtube.com/watch?v=tbhYxd2sfAE as a guide

import socket 

def whois_lookup(domain: str): # This function performs a WHOIS lookup for a given domain.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a TCP socket.
    s.connect(("whois.verisign-grs.com", 43)) # Connect to the WHOIS server.
    s.send(f"{domain}\r\n".encode()) # Send the domain query.
    response = s.recv(4096).decode() # Receive the response.
    s.close() # Close the socket.
    return response # Return the WHOIS response.

def main():
    domain = input("Enter a domain to look up: ")
    print(whois_lookup(domain))
