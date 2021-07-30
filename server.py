import socket
import threading
import os
import sys

class ThreadedServer():

    def __init__(self):
        host= '192.168.56.101'
        port = 1000
        self.s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((host, port))

    def listenClient(self):
        self.s.listen(10)
        while True:
            print('*** Waiting for client ***')
            c, addr = self.s.accept()
            c.settimeout(60)
            threading.Thread(target= self.clientThread, args= (c, addr)).start()

    def clientThread(self, c, addr):
        buffer= 2048
        print('*** Client (', addr, ') has connected ***')

        buffer= c.recv(2048)

        if(buffer.decode()== "download"):
            print(os.listdir("/home/ikkkmal/gp/"))

            fileName= c.recv(2048)
            for file in os.listdir("/home/ikkkmal/gp/"):
                if file== fileName.decode():
                    fileFound= 1
                    break

            if fileFound == 0:
                print("*** File not found on server ***")

            else:
                print("*** File has been located ***")
                fileUp= fileName.decode()
                upFile= open("/Ambition/server/"+fileUp,"rb")
                Read= upFile.read(2048)
                i= 1
                while Read:
                    print("*** Sending...%d ***" %(i))
                    c.send(Read)
                    Read= upFile.read(2048)
                print("*** File has been sent ***")
                upFile.close()

                c.close()

        elif(buffer.decode() == "upload"):
            fileName = c.recv(2048)
            downFile = fileName.decode()
            buffer= c.recv(2048)
            fileDown= open(downFile,"wb")
            i = 1
            while Data:
                print('*** Recieving...%d ***' %(i))
                fileDown.write(buffer)
                Data= c.recv(2048)
                i= i + 1
            print("*** File successfully received ***")
            fileDown.close()
            c.close()

if __name__ == "__main__":
    ThreadedServer().listenClient()
