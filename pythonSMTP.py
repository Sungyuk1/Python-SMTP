#import socket module
from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "mail.egr.msu.edu"
mailport = 25

# Create socket called clientSocket and establish a TCP
# connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailport))
print("After Connection")
#Fill in end

recv = clientSocket.recv(1024).decode()
print("recv : ", recv)

if recv[:3] != "220":
    print("220 reply not received from server.")

# Send HELO command and print server response.
#Fill in start
helo = 'HELO mail.egr.msu.edu\r\n'
heloEncoded = helo.encode()
clientSocket.send(heloEncoded)
#Fill in end

recv1 = clientSocket.recv(1024).decode()
print("recv1 : ", recv1)
if recv1[:3] != "250":
    print("250 reply not received from server.")

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <kwonsun7@egr.msu.edu>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("recv2 : ", recv2)
# Fill in end

# Send RCPT TO command and print server
# response. [replace "xxxx" with a valid account]
# It specifies the recipient of mail.
# Fill in start
rcptto = "RCPT TO: <kwonsun7@egr.msu.edu>\r\n"
clientSocket.send(rcptto.encode())
recv3 = clientSocket.recv(1024).decode()
print("recv3 : ",recv3)
# Fill in end

# Send DATA command and print server response.
# It specifies the beginning of the mail.
# Fill in start
data = 'DATA \r\n' 
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("recv4 : ",recv4)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
#recv5 = clientSocket.recv(1024).decode()
#print("recv5 : ", recv5)
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv6 = clientSocket.recv(1024).decode()
print("recv6 : ",recv6)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = 'QUIT\r\n'
clientSocket.send(quit.encode())
recv7 = clientSocket.recv(1024).decode()
print("recv7 : ",recv7)
# Fill in end

clientSocket.close()
print("End")