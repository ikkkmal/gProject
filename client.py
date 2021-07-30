import socket
import sys
import os

s= socket.socket()
port= 443
host=''
s.bind((host, port))

try:
    s.connect((host, port))
    print("\n*** Connected Successfully! ***")

except Exception as e:
    print("\n*** Connection with %s:%d failed. Exception is %s ***" % (host, port, e))
#^^^^ KENG ^^^^
choice= input("\n*** 'download' or 'upload' ***\nYou: ")

if(choice== "download"):
    choice= "download"
    s.send(choice.encode())
    fileName=input("\n*** Please enter filename ***\nYou: ")
    buffer= "Temp"

    while True:
        s.send(fileName.encode())
        buffer= s.recv(2048)
        downFile= open(fileName,"wb")

        print('\n*** Receiving file ***')
        downFile.write(buffer)
        buffer= s.recv(2048)

        print("\n*** File Received ***")
        downFile.close()
        break
#^^^^ MAL ^^^^
elif(choice== "upload"):

    choice= "upload"
    s.send(choice.encode())
    print(os.listdir("/home/ikkkmal/gp/"))
    fileName= input("*** Please enter filename ***\nYou:  ")
    s.send(fileName.encode())

    upFile= open("/home/ikkkmal/gp/" +fileName,"rb")
    Read= upFile.read(2048)

    print("*** Sending file ***")
    s.send(Read)
    Read= upFile.read(2048)

    print("*** File sent ***")
    upFile.close()

s.close()
#^^^^ MEO ^^^^

