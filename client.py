# a TCP/IP client that receives a message from server
import codecs
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

def nextAction(verbs,verb):

    if (verb  in verbs):
      return verbs[(verbs.index(verb)+1) % (len(verbs)-1)]

    return None

def convToEmjoi(msg):

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
def bot3(sentence, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral,preSentencesNegative):

    action = extractAction(verbs, sentence)

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

    return res.format(action)

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

# A function that listen to a socket, and send back a response
def listener(s, name, bot, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral,
             preSentencesNegative,parentName):
    try:
        while True:
            msg = s.recv(1024).decode().strip()
            if (parentName==name and msg.split("--")[0] == "RES"):
               resMsg = msg.split("--")[1]
               print(convToEmjoi(resMsg))


            if (msg.split("--")[0] == "EXIT{}".format(parentName)):

                print("Exiting socket connection associated with bot {}".format(name))
                s.send("")
                s.close()

            elif(msg.split("--")[0] == "REQ"):
                s.send(("RES--{}>{}".format(name,bot(msg.split("--")[1], verbs, chancesPositive, chancesNeutral, preSentencesPositive,
                                      preSentencesNeutral, preSentencesNegative)).encode().rjust(1024)))
    except:
        s.close()
        return
    s.close()


def backgroundClient(host, port, bot,name,parentName):
    try:
        botNumber = bot.__name__[3:]
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
        s, name, bot, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative,parentName,))

        t1.start()

    except:
        return


def interactiveClient(host, port, bot,name,namesbackground,bots):

    botNumber = bot.__name__[3:]
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
    s, name, bot, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative,name,))
    msg = s.recv(1024).decode().strip()
    print(msg)

    t1.start()
    childThreads = []
    #To make sure all bot-clients gets killed, when interactive client gets killed.
    for idx, name2 in enumerate(namesbackground):
        t2 = threading.Thread(target=backgroundClient, args=('localhost', 5000, bots[idx], name2,name,))
        t2.start()
        childThreads.append(t2)

    while True:
        try:
                print("\n")
                print(name + ":")
                msg = input()
                if(msg=="exit"):
                    s.send("EXIT{}".format(name).encode().rjust(1024))
                    for thread in childThreads:
                        thread.join()
                    time.sleep(0.5)
                    print("All socket connections has been terminated. Exiting client")
                    return
                else:
                    s.send(("REQ--{}".format(msg)).encode().rjust(1024))
                time.sleep(0.1)

        except:
            s.close()
            return
    print("{} has exited chat").format(name)
    s.close()

#Interactive-client that can use terminal. This client also have a bot, that responds on behalf on you.
nameinteractive="Moran"
botInteractive = bot1

#One can have a up to 4 types of bot-clients that can work with you in a discussion.
#When you quit the chat, the bots will also leave the chat
namesbackground = ["Jumper", "Hanne", "Olivia", "Trude"]
bots = [bot1,bot2,bot3,bot4]

t1 = threading.Thread(target=interactiveClient, args=('localhost', 5000, botInteractive, nameinteractive,namesbackground,bots, ))
t1.start()



