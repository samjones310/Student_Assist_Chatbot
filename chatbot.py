from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import re
import datetime
def get_response(usrText):
    now = datetime.datetime.now()
    usrText=usrText.lower()
    regno=usrText[:6]
    usrText=usrText[6:]
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.50,
            'default_response': 'I am sorry'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip()!= 'Bye':
            if usrText.strip()=="time":
                usrText=regno[:4]+usrText
                usrText=usrText+now.strftime('%A')
                return(ustText)
            if usrText.strip()=="mess":
                usrText=regno[:2]+usrText
                usrText=usrText+now.strftime('%A')
                return(usrText)
            if usrText.strip()=="task":
                usrText=regno+usrText
                usrText=usrText+now.strftime('%Y-%m-%d')
                return(usrText)
            result = bot.get_response(usrText)                        
            reply = str(result)
            return(reply)
        elif usrText.strip() == 'Bye':
            return('Bye')
            break
        

        
