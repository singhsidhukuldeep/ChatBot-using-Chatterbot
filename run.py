#getting response
import ChatBot

# Now let's get a response to a greeting
while True:
    message = input('\x1b[1;34;44m' + 'Ask Bot:' + '\x1b[0m' + '\t')
    if (message.strip().lower() == "bye"):
        print('\x1b[1;31;41m' + 'ENDING' + '\x1b[0m')
        break
 
    response = ChatBot.botreply(message)
    # print ('\x1b[1;36;46m' + 'You (Input):' + '\x1b[0m' + '\t', message)
    # print ('\x1b[1;33;43m' + 'Jadoo:' + '\x1b[0m' + '\t\t', response)
    print ("\n\n")