# importing dependencies
from chatterbot import ChatBot
from chatterbot.response_selection import get_random_response
import logging
import sys
import os
import datetime

#trainner
def train (datafolder="", train_corpus = True):
    # Enable info level logging
    logging.basicConfig(level=logging.INFO)

    chatbot = ChatBot(
        'Chatting Bot',
        trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    )

    # Start by training our bot with the custom data(if present) or else with custom data
    if (not datafolder == ""):
        chatbot.train(
            datafolder
        )
    if (train_corpus == True):
        #Start by training our bot with the ChatterBot corpus data
        chatbot.train(
            'chatterbot.corpus.english'
        )
    # Now we can export the data to a file
    #chatbot.trainer.export_for_training('./my_export.json')


#getting a reply
def botreply (messagein, db_location = "db.sqlite3"):
    
    #checking if the model exsists
    if not os.path.exists(db_location):
        error = "ERROR IN REPLYING \n"
        error = error + "Model doesnot exsist at " + db_location + "\n"
        error = str(datetime.datetime.now()) + "\n" + error + "\n"
        print (error)
        return ("Sorry! I am resting right now. Please come back later")


    # Enable info level logging
    logging.basicConfig(level=logging.INFO)

    #creating BOT
    chatbot = ChatBot (
        'Chatting Bot',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch'
            },
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'Help me!',
                'output_text': 'mail your quey here: singhsidhukuldeep@gmail.com'
            },
            {
                'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                'threshold': 0.65,
                'default_response': 'I am sorry, but I do not understand.'
            }
        ],
        database = db_location,
        response_selection_method=get_random_response,
        read_only=True)


    # Now let's get a response to a greeting
    message = messagein
    reply = chatbot.get_response(message)
    response = str(reply)
    print ('\x1b[1;36;46m' + 'YOU (Input):' + '\x1b[0m' + '\t', message)
    print ('\x1b[1;33;43m' + 'BOT:' + '\x1b[0m' + '\t\t', response)
    print ("\n")
    return response