from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    # Fill in end
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailfromcommand = 'MAIL FROM:\r\n'
    clientSocket.send(mailfromcommand.encode())
    # Fill in start
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send RCPT TO command and handle server response.
    rcpttocommand = 'RCPT TO: \r\n'
    clientSocket.send(rcpttocommand.encode())
    # Fill in start
    recv3 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send DATA command and handle server response.
    dataCommand = 'DATA\r\n'
    clientSocket.write(dataCommand.encode())
    # Fill in start
    recv4 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())

    # Fill in start
    recv5 = clientSocket.recv(1024).decode()
    # Fill in end

    # Send QUIT command and handle server response.
    quitCommand = 'QUIT\r\n'
    # Fill in start
    clientSocket.send(quitCommand.encode())
    # Fill in end
    recv6 = clientSocket.recv(1024).decode()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')