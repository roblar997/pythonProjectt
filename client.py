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
             preSentencesNegative):
    try:
        while True:
            msg = s.recv(1024).decode().strip()
            if (msg.split("--")[0] == "RES"+name):
              print(msg.split("--")[1])
            elif(msg.split("--")[0][:3] == "REQ"):
                str = msg.split("--")[0]
                s.send(("RES{}--{}>{}".format(str[3:len(str)],name,bot(msg.split("--")[1], verbs, chancesPositive, chancesNeutral, preSentencesPositive,
                                      preSentencesNeutral, preSentencesNegative)).encode().rjust(1024)))
    except:
        s.close()
        return
    s.close()


def backgroundClient(host, port, bot,name):

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
    s, name, bot, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative,))

    t1.start()

def interactiveClient(host, port, bot,name):

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
    s, name, bot, verbs, chancesPositive, chancesNeutral, preSentencesPositive, preSentencesNeutral, preSentencesNegative,))
    msg = s.recv(1024).decode().strip()
    print(msg)

    t1.start()

    while True:
        try:
                print("\n")
                print(name + ":")
                msg = input()
                if(msg=="exit"):
                    s.send("EXIT".encode().rjust(1024))
                    msg = s.recv(1024).decode().strip()
                    if not msg:
                        print("Exiting client {}".format(name))

                    return
                s.send(("REQ{}--{}".format(name,msg)).encode().rjust(1024))
                time.sleep(0.1)

        except:
            s.close()
            return
    print("{} has exited chat").format(name)
    s.close()

nameinteractive="Moran"
namesbackground=["Jumper","Hanne","Olivia","Trude"]
botInteractive = bot1

bots = [bot1,bot2,bot3,bot4]

t1 = threading.Thread(target=interactiveClient, args=('localhost', 5000, botInteractive, nameinteractive, ))
t1.start()

for idx, name in enumerate(namesbackground):
    t1 = threading.Thread(target=backgroundClient, args=('localhost', 5000, bots[idx],name, ))
    t1.start()

