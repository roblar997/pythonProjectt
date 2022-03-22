# a TCP/IP server that sends a messages to client

import socket
import threading
import select
import random

def serverFunc(c,cList,verbs):
  try:


    val = random.randint(0, len(verbs) - 1)

    c.send(("Welcome to chat. All clients have bots installed," +
             "that responds to verbs in sentences you come with. I suggest you make a sentence"+
             " containing the word -- {} --   as the first verb in the sentence. To exit, write 'exit' in the terminal".format(verbs[val])).encode().rjust(1024))
    while True:

        #Our sockets is non-blocking, so we just take whats ready
        #to receive or send, then send/receive and move on without any waiting.
        #for the operation to be finished.
        readable, writable, exceptional = select.select(cList,
                                                        cList,
                                                        cList)
        #Connection is ready to send to us
        if c in readable:

             msg = c.recv(1024)
             # For debug purposes
             print("Thread {} sending message. {} \n".format(c,msg.decode().strip()))
             #Stop listening on server side
             if not msg:
                 # For debug purposes
                 print("Thread {} did get empty message. Is now breaking loop\n".format(c))
                 break

             #Terminating a client, which means trying to send a EXIT signal to all bots associated
             #with a client
             msgDec = msg.decode().strip()
             if msgDec[:4]=="EXIT":
                 #Name of the client, that has all the bots
                 name = msgDec[4:]
                 for sock in writable:
                        # For debug purposes
                        print("Thread {} got EXIT signal\n".format(c))
                        sock.send("EXIT{}".format(name).encode().rjust(1024))

             else:
                #Everyone ready to receive a message, which mean that not everyone gets to see the full chat
                #This makes sense if something is in realtime and we can accept that offline users arent supposed
                #to get messages, for example in a realtime gaming chat. That something happens in realtime, is
                 #more important than wheter or not everyone gets all messages
                 for sock in writable:
                 #Make sure not to send to myself
                    if c != sock:
                     # For debug purposes
                     print("Thread {} sending message. {} to {} \n".format(c, msg.decode().strip(),sock))
                     #Send message I just got received, to all than are able to receive.
                     sock.send(msg)

    #For debug purposes
    print("Client {} has been removed from server".format(c))
    #Kick out user
    cList.remove(c)
  except:
      # For debug purposes
      print("Client {} has been removed from server".format(c))
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
        #For debug purposes
        print("Client {} has been connected to server".format(c))
        #Our list of online users
        cList.append(c)

        #One thread per user
        t1 = threading.Thread(target=serverFunc, args=(c,cList,verbs,))
        t1.start()


server(5000)
