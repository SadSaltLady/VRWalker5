#!/usr/bin/env python
import socket
import queue
import json


DataQueue = queue.Queue()
Delimiter = "!"
FILE = None
LeftOverData = ""

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

# def TransmitData(content):
#     print("Sending: \n")
#     print(content)
#     conn.send(bytes(str(content), 'utf-8'))  # echo
#

def ProcessData(data):
    data = data + "\n"
    global FILE
    FILE.write(data)
    return data

def CreateFile(data):
    filename = data + ".csv"
    file = open(filename, 'w')
    print(type(file))
    return filename, file

def ProcessCommand(data):
    # no guarantee that str contains the data we need, so we should make sure we get all we need.
    str = data.decode()
    commands = str.split(Delimiter)
    for i in range(len(commands)):
        DataQueue.put(commands[i])


def ProcessQueue():
    global FILE #uses the global FILE variable
    #no valid commands inside the queue
    if DataQueue.empty():
        return
    while not DataQueue.empty():
        values = DataQueue.get()
        # if command is FileName, then create the file
        if values.has_key("FileName"):
            fileName, f = CreateFile(values["FileName"])
            FILE = f
            return
        # if command is stop
        if values.has_key("Stop"):
            FILE.close()
            return
        # if command is data
        if values.has_key("data"):
            ProcessData(values["data"])
            return


def server():
    # AwaitingFileName = False
    # AwaitingData = False
    # fileName = ""

    TCP_IP = '127.0.0.1' #"192.168.137.37" #'127.0.0.1' local host value
    TCP_PORT = 54000
    BUFFER_SIZE = 16384  # Normally 1024, but we want fast response

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print("Listening for clients, further messages will appear below when someone connects to me! \n")
    conn, addr = s.accept()
    print('Connection address:', addr)
    # TODO: timeout and dump to file (if there is known filename) after no data after say... 5 seconds
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        #no guarantee data has complete commands, so needs to be processed
        ProcessCommand(data)
        ProcessQueue()
    conn.close()

server()