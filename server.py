#!/usr/bin/python3

import socket
import sys
import threading
import select
import random

def serverFunc(c,cList,verbs):
  try:
    val = random.randint(0, len(verbs) - 1)
    # Our sockets is non-blocking, so we just take whats ready
    # to receive or send, then send/receive and move on without any waiting.
    # for the operation to be finished.
    readable, writable, exceptional = select.select(cList,
                                                    cList,
                                                    cList)

    #Everyime a new client comes, host sends an initative dialoge to everyone.
    #Everyone can see the full dialoge
    for sock in writable:
        sock.send(("HOST--Anyone want to {} ?").format(verbs[val]).encode().rjust(1024))

    while True:


        #Connection is ready to send to us
        if c in readable:
             msg = c.recv(1024)

             #Should not happen disconnection
             if not msg:
                 break

             if msg.decode().strip() == "EXIT":
                 print("{} got EXIT signal".format(c))
                 if c in writable:
                     c.send(msg)
                     break


             #Everyone ready to receive a message, which mean that not everyone gets to see the full chat
             #This makes sense if something is in realtime and we can accept that offline users arent supposed
             #to get messages, for example in a realtime gaming chat. That something happens in realtime, is
             #more important than wheter or not everyone gets all messages
             for sock in writable:
              #Make sure not to send to myself
              if c != sock:
                #Send message I just got received, to all than are able to receive.
                sock.send(msg)

    #Kick out user
    print("Client {} is being kicked out".format(c))
    cList.remove(c)
  except:
      print("Client {} is being kicked out".format(c))
      #Something went wrong, kick out user
      cList.remove(c)

##
#   Load verbs from file
#
def loadFromFile():
    # Load verbs, and corresponding chances for positive and neutral
    # into file.
    fileVerbs = open("verbs.txt", "r")
    verbs = fileVerbs.readlines()
    for idx, verb in enumerate(verbs):
        verbs[idx] = verb.split(" ")[0]
    fileVerbs.close()
    return verbs
def server(port):
    cList = []
    verbs = loadFromFile()
    #I am connecting to server using IP version 4 addresses, and using TCP socket.
    #AF_INET stands for ipv4 and SOCK_STREAM stands for TCP.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Socket gets associated with this host and port
    s.bind(('localhost', port))

    #Max 100 users or sockets can be connected at the same time
    s.listen(100)

    while True:
        #New user
        c, addr = s.accept()
        print("{} is connected".format(c))

        #Non bloking, that is we continue runing instead of waiting for the guy to send/receive
        c.setblocking(0)

        #Our list of online users
        cList.append(c)

        #One thread per user
        t1 = threading.Thread(target=serverFunc, args=(c,cList,verbs,))
        t1.start()
def main(argv):
    port=5000
    if(len(argv) < 2):
        print("Not enough arguments given")
        exit(-1)
    if(str(argv[1])=="-h" or str(argv[1])=="--help"):
        print("Explanation of arguments:\n")
        print("#1 argument: port number --  type: integer")
        exit(0)
    if(argv[1].isnumeric()):
        port=int(argv[1])
    else:
        print("Port should be a number")
        exit(-1)
    server(port)

if __name__ == "__main__":
    main(sys.argv)

