import socket
import sys

f = open(sys.argv[1], "r")
msg = f.read()
msg_length = len(msg)
# print "Message is: " + msg
print "Message Length: %d" % msg_length

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost",23394))

# Send data:
print "Sending Data"
totalsent = 0
while totalsent < msg_length:
    sent = sock.send(msg[totalsent:])
    print "Sent: %d" % sent
    if sent == 0:
        raise RuntimeError("Connection lost while sending")
    totalsent += sent

sock.shutdown(socket.SHUT_WR)

# Receive response:
print "Recieving Data:"
chunks = []
bytes_recd = 0
while bytes_recd < msg_length:
    chunk = sock.recv(2048)
    print "Received %d bytes" % len(chunk)
    chunks.append(chunk)
    bytes_recd = bytes_recd + len(chunk)
    if chunk == '':
        break
response = ''.join(chunks)

sock.close()


# Output:
print "Total bytes received: %d" % bytes_recd
print response
