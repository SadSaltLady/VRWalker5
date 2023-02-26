#!/usr/bin/env python
import socket

FILE = None

def cleanQuery(query):
    temp = ""
    for byte in query:
        if byte == 44 or 48 <=  byte <= 57:
            temp += chr(byte)
    temp = temp.strip()
    temp = temp.split(',')
    cleaned = []
    if (len(temp) <= 1): return []
    for val in temp:
        cleaned.append(int(val))
    return cleaned

def validateQuery(query, idealLength = -1):#tests
    if len(query) != idealLength:
        return False
    for val in query:
        if not (0 <= val <= 100):
            return False
    return True

def TransmitData(content):
    print("Sending: \n")
    print(content)
    conn.send(bytes(str(content), 'utf-8'))  # echo


def ProcessData(data):
    data = data + "\n"
    FILE.write(data)
    return data

def CreateFile(data):
    filename = data + ".csv"
    file = open(filename, 'w')
    print(type(file))
    return filename, file

    

AwaitingFileName = False
AwaitingData = False
fileName = ""
TCP_IP = "192.168.146.45" #'127.0.0.1' local host value
TCP_PORT = 54000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("Listening for clients, further messages will appear below when someone connects to me! \n")
conn, addr = s.accept()
print('Connection address:', addr)
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    str = data.decode()
    if (str == "start"):
        AwaitingFileName = True
    elif (str == "stop"):
        AwaitingData = False
        FILE.close()
    elif AwaitingFileName:
        fileName, f = CreateFile(str)
        FILE = f
        AwaitingFileName = False
        AwaitingData = True
    elif AwaitingData:
        output = ProcessData(str)
        print("Wrote: " + output)
    
    
 

    #query = cleanQuery(data)
    #if (validateQuery(query, 16)):
    #    TransmitData("Data Received")
    #TransmitData(-1)
    #TransmitData(len(query))
conn.close()