import logging
from telegram.ext import updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getlogger(__name__)

def main():
    """Start the bot."""
    updater = Updater("TOKEN HERE", use_context=True)
    
    #Get dispatcher to register handles
     dp = updater.dispatcher
				
    #commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
			
    #noncommand
    dp.add_handler(MessageHandler(Filters.text, echo))
			
    #error logs
    dp.add_error_handler(error)
			
    #Start the bot
    updater.start polling()
				
    #run the bot
    updater.idle()
			
if __name__ = '__main__':main()


Code © @Abhijith-Sudhakaran 
