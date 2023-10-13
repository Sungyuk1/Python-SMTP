#import socket module
from socket import *
import ssl
from base64 import *
msg = "\r\n Bonus Question"
endmsg = "\r\n.\r\n"

#Get User Password
clientPassword = input("Enter Password")
clientPassword = b64encode(clientPassword.encode()) + "\r\n".encode()

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "mail.egr.msu.edu"
mailport = 587

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


#Provided Code for TLS
command = "STARTTLS\r\n"
clientSocket.send(command.encode())
recv = clientSocket.recv(1024).decode()
print("recv tls 1 : ", "START TLS: ", recv)
if recv[:3] != "220":
    print ("220 reply not received from server.")

# log in
scs = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
emailAddress = "kwonsun7@egr.msu.edu"
clientEmailAddress = b64encode(emailAddress.encode())
clientEmailAddress = clientEmailAddress + "\r\n".encode()

# Send HELO command and print server response.
#Fill in start
helo = 'HELO mail.egr.msu.edu\r\n'
heloEncoded = helo.encode()
scs.send(heloEncoded)
#Fill in end

recv1 = scs.recv(1024).decode()
print("recv1 : ", recv1)
if recv1[:3] != "250":
    print("250 reply not received from server.")


Auth = "AUTH LOGIN\r\n"
scs.send(Auth.encode())
recv = scs.recv(1024).decode()
print("recv tls 2 : AUTH LOGIN: ", recv)

scs.send(clientEmailAddress)
recv = scs.recv(1024).decode()
print("recv tls 3 : ", recv)

scs.send(clientPassword)
recv = scs.recv(1024).decode()
print("recv tls 4 : ", recv)

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <kwonsun7@egr.msu.edu>\r\n"
scs.send(mailFrom.encode())
recv2 = scs.recv(1024).decode()
print("recv2 : ", recv2)
# Fill in end

# Send RCPT TO command and print server
# response. [replace "xxxx" with a valid account]
# It specifies the recipient of mail.
# Fill in start
rcptto = "RCPT TO: <sungyuk1029@gmail.com>\r\n"
scs.send(rcptto.encode())
recv3 = scs.recv(1024).decode()
print("recv3 : ",recv3)
# Fill in end

# Send DATA command and print server response.
# It specifies the beginning of the mail.
# Fill in start
data = 'DATA \r\n' 
scs.send(data.encode())
recv4 = scs.recv(1024).decode()
print("recv4 : ",recv4)
# Fill in end

# Send message data.
# Fill in start
scs.send(msg.encode())
#recv5 = clientSocket.recv(1024).decode()
#print("recv5 : ", recv5)
# Fill in end

# Message ends with a single period.
# Fill in start
scs.send(endmsg.encode())
recv6 = scs.recv(1024).decode()
print("recv6 : ",recv6)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = 'QUIT\r\n'
scs.send(quit.encode())
recv7 = scs.recv(1024).decode()
print("recv7 : ",recv7)
# Fill in end

scs.close()
print("End")