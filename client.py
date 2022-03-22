#!/usr/bin/python3

# a TCP/IP client that receives a message from server
import sys
import random
import socket
import threading
import time


#  Find first occurence of a known verb in a given sentence.
#  Implementation could have been better, but it is not needed
#
#  @param Something one do, an action
#  @sentence Sentence that may contain a verb
def extractAction(verbs, sentence):
    for word in sentence.split():
        if (word in verbs):
            return word
    return None

#Take the next verb in the list of verbs. If goes over edge, take
#the first verb in list
#
#@param verbs a list of verbs
#@param a verb
def nextAction(verbs,verb):

    if (verb  in verbs):
      return verbs[(verbs.index(verb)+1) % (len(verbs)-1)]

    return None

#Convert msg to emjoi in terms of unicode
def convToEmjoi(msg):

    msg = msg.replace(":)", "\U0001f600")
    msg = msg.replace(":(", "\U0001F620")
    msg = msg.replace(":D","\U0001f600")
    msg =msg.replace(":E", "\U0001F605")
    msg =msg.replace(":I", "\U0001F923")
    msg =msg.replace(":M", "\U0001F602")
    msg =msg.replace(":T", "\U0001F642")
    msg =msg.replace(":R", "\U0001F607")
    msg = msg.replace(":J", "\U0001F60D")
    msg =msg.replace(":Z", "\U0001F910")
    msg =msg.replace(":X", "\U0001F910")
    msg = msg.replace(":P", "\U0001F612")

    return msg
# Gives a response to a sentence, by looking on first occurence of a word
# One have different chances of something being presieved postive, neutral or negative
# By giving a response, one random generate a number with three choices in each.
# Each choice has 3 response sentences, that is made based on a random generator
# that gives a number and compared to values in chancesPositive <= val and chancesNeutral + chancesPositive <= val
#
# @param chancesPositive
# @param sentence A sentence that may contain a verb.
# @param chancesPositive list that contains elee
#
#
#
def bot1(sentence, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral,preSentencesNegative):
    action = extractAction(verbs, sentence)

    #No verb found, so use default response
    if action is None:
        return "I don't understand, please explain"
    val = random.uniform(0, 1)
    rand = random.randint(0, len(preSentencesPositive) - 1)

    # Decide how to think about the verb, based on a random generator
    # That is, use the random value to give a positive, neutral og negative response
    if (chancesPositive[rand] <= val):
        res = preSentencesPositive[rand]
    elif (chancesPositive[rand] + chancesNeutral[rand] <= val):
        res = preSentencesNeutral[rand]
    else:
        res = preSentencesNegative[rand]

    return res.format(action)

# Same as bot 1, except that it also takes a random verb that it inserts into the sentence
#
def bot2(sentence, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral,preSentencesNegative):

    action = extractAction(verbs, sentence)
    action2 = verbs[random.randint(0, len(verbs) - 1)]
    #No verb found, so use default response
    if action is None:
        return "This I do not get"
    val = random.uniform(0, 1)
    rand = random.randint(0, len(preSentencesPositive) - 1)

    # Decide how to think about the verb, based on a random generator
    # That is, use the random value to give a positive, neutral og negative response
    if (chancesPositive[rand] <= val):
        res = preSentencesPositive[rand]
    elif (chancesPositive[rand] + chancesNeutral[rand] <= val):
        res = preSentencesNeutral[rand]
    else:
        res = preSentencesNegative[rand]

    return res.format(action,action2)

# Same as bot 1, except it adds ing to end and add it 2 places into the sentences - instead of 1
#
def bot3(sentence, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral,preSentencesNegative):

    action = extractAction(verbs, sentence)

    #No verb found, so use default response
    if action is None:
        return "I cant understand this"
    val = random.uniform(0, 1)
    rand = random.randint(0, len(preSentencesPositive) - 1)

    # Decide how to think about the verb, based on a random generator
    # That is, use the random value to give a positive, neutral og negative response
    if (chancesPositive[rand] <= val):
        res = preSentencesPositive[rand]
    elif (chancesPositive[rand] + chancesNeutral[rand] <= val):
        res = preSentencesNeutral[rand]
    else:
        res = preSentencesNegative[rand]

    return res.format(action+"ing",action+"ing")

# Same as bot1, except it also takes a verb through function actionNext that is inserted into the sentence
# actionNext finds next verb in dictonary, relative to the first verb found in given sentence
#
def bot4(sentence, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral,preSentencesNegative):

    action = extractAction(verbs, sentence)
    actionNext = nextAction(verbs,action)

    #No verb found, so use default response
    if action is None:
        return "ohm, this didnt go through my head"
    val = random.uniform(0, 1)
    rand = random.randint(0, len(preSentencesPositive) - 1)

    # Decide how to think about the verb, based on a random generator
    # That is, use the random value to give a positive, neutral og negative response
    if (chancesPositive[rand] <= val):
        res = preSentencesPositive[rand]
    elif (chancesPositive[rand] + chancesNeutral[rand] <= val):
        res = preSentencesNeutral[rand]
    else:
        res = preSentencesNegative[rand]

    return res.format(action, actionNext)
## All sentences and verbs are stored in files
#  This will load all of those into lists, and
#  @return verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative
def loadFromFile(presentenceFileName):

    # Load verbs, and corresponding chances for positive and neutral
    # into file.
    fileVerbs = open("verbs.txt", "r")

    chancesPositive = []
    chancesNeutral = []

    verbs = fileVerbs.readlines()
    for idx, verb in enumerate(verbs):
        verbs[idx] = verb.split(" ")[0]
        chancesPositive.append(float(verb.split(" ")[1]))
        chancesNeutral.append(float(verb.split(" ")[2]))
    fileVerbs.close()


    #Load different response (positive, neutral, negative), corresponding
    #to a random value.
    filePreSentence = open(presentenceFileName, "r")

    preSentencesNegative = []
    preSentencesNeutral = []
    preSentencesPositive = []

    preSentences = filePreSentence.readlines()

    for preSentence in preSentences:
        preSentencesNegative.append(preSentence.split("!!")[0].strip())
        preSentencesNeutral.append(preSentence.split("!!")[1].strip())
        preSentencesPositive.append(preSentence.split("!!")[2].strip().replace("\n", ""))

    filePreSentence.close()
    return verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative

## All sentences and verbs are stored in files
#  This will load all of those into lists, and
#  @return verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative
def loadFromFile(fileName):

    # Load verbs, and corresponding chances for positive and neutral
    # into file.
    fileVerbs = open("verbs.txt", "r")

    chancesPositive = []
    chancesNeutral = []

    verbs = fileVerbs.readlines()
    for idx, verb in enumerate(verbs):
        verbs[idx] = verb.split(" ")[0]
        chancesPositive.append(float(verb.split(" ")[1]))
        chancesNeutral.append(float(verb.split(" ")[2]))
    fileVerbs.close()




    #Load different response (positive, neutral, negative), corresponding
    #to a random value.
    filePreSentence = open(fileName, "r")

    preSentencesNegative = []
    preSentencesNeutral = []
    preSentencesPositive = []

    preSentences = filePreSentence.readlines()
    #Negative, neutral or positive response
    for preSentence in preSentences:
        preSentencesNegative.append(preSentence.split("!!")[0].strip())
        preSentencesNeutral.append(preSentence.split("!!")[1].strip())
        preSentencesPositive.append(preSentence.split("!!")[2].strip().replace("\n", ""))

    filePreSentence.close()
    return verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative

# A function that listen to a socket, and send back a response
def listener(s, name, bot, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral,
             preSentencesNegative):
    try:
        while True:
            msg = s.recv(1024).decode().strip()
            print(msg)
            if (msg.split("--")[0][:3] == "RES"):
                print(convToEmjoi(msg.split("--")[1]))
            elif (msg.split("--")[0][:3] == "REQ"):
                str = msg.split("--")[0]
                toSend = "RES{}-->{}".format(str[3:len(str)], name,
                                             bot(msg.split("--")[1], verbs, chancesPositive, chancesNeutral,
                                                 preSentencesPositive,
                                                 preSentencesNeutral, preSentencesNegative))
                s.send((toSend).encode().rjust(1024))
                # Writing host message to screen, and responding to suggestion from host

                # Response to host, from other participants
            elif (msg.split("--")[0][:7] == "HOSTRES"):
                print("OK")
                print(convToEmjoi(msg.split("--")[1]))

            elif (msg.split("--")[0][:4] == "HOST"):
                print("Host>{}".format(convToEmjoi(msg.split("--")[1])))
                response = "{}>{}".format(name, bot(msg.split("--")[1], verbs, chancesPositive, chancesNeutral,
                                                         preSentencesPositive,
                                                         preSentencesNeutral, preSentencesNegative))
                toSend = "HOSTRES--{}".format(response)
                print(toSend)
                s.send((toSend).encode().rjust(1024))



            #Parent thread wants to quit, and server is notified and agrees
            #Time to stops listening to socket
            if (msg=="EXIT"):
                s.socket()
                break


    except:
        s.close()
        print("Client is shuting down")
        return
    print("Client is shuting down")
    s.close()



def client(host, port, bot,name = None):


    botNumber = bot.__name__[3:]

    if(int(botNumber) <= 0 or int(botNumber) > 4):
        print("Illegal name of bot function")
        exit(-1)

    if name == None:
         names = ["Olivia", "Per", "Jacob", "Severin"]
         name = names[int(botNumber)-1]

    fileName = "preSentence{}.txt".format(botNumber)

    #Loading stuff that is important to make decision on how to respond to a sentence
    #That is chances for an action to be associated as a positive thing and a natural thing
    #A response can be either positive sentence, a netural sentence or a negative sentence
    #
    verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative = loadFromFile(fileName)

    # connect it to server and port number
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    t1 = threading.Thread(target=listener, args=(
    s, name, bot, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative,))

    t1.start()

    while True:
        try:

            #If one want it as user input
            msg = input("Terminal::{}>".format(name))

            print(u"\n{}>{}".format(name,convToEmjoi(msg)))
            if(msg=="exit"):
                s.send("EXIT".encode().rjust(1024))
                t1.join()
                exit(0)
            else:
                s.send(("REQ{}--{}".format(name,msg)).encode().rjust(1024))
            time.sleep(0.5)
            print("\n")

        except:
            s.close()
            return
    s.close()




def main(argv):

    if(len(argv) == 2 and (str(argv[1])=="-h" or str(argv[1])=="--help")):
        print("Explanation of arguments\n")
        print("#1 argument: hostname             --  type: string\n")
        print("#2 argument: port number          --  type: integer\n")
        print("#3 argument: name of bot function --  type: string\n")
        print("#4 argument [OPTIONAL]: name of client --  type: string\n")
        exit(0)
    if(len(argv) < 4):
        print("Not enough arguments given\n")
        exit(-1)
    bot=bot1
    localhost='localhost'
    port=5000

    if(argv[1].isprintable()):
        localhost=str(argv[1])
    else:
        print("Localhost should be a string\n")
        exit(-1)

    if(argv[2].isnumeric()):
        port=int(argv[2])
    else:
        print("Port should be a number\n")
        exit(-1)

    if(str(argv[3])=="bot1"):
        bot=bot1
    elif(str(argv[3])=="bot2"):
        bot=bot2
    elif (str(argv[3]) == "bot3"):
        bot = bot3
    elif (str(argv[3]) == "bot4"):
        bot = bot4
    else:
        print("Bot function does not exist. Only bot1,bot2,bot3 and bot4 function exist\n")
        exit(-1)
    if(len(argv)>=5 and argv[4].isprintable()):
        name = str(argv[4])
        client(localhost, port, bot,name)

    else:
        client(localhost, port, bot)



if __name__ == "__main__":
    main(sys.argv)
