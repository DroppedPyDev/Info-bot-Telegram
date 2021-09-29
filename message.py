def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
   #edit this hi with your Bot status or your reason. you can also add your chat links in message!
		
def help(update, context):
    """Send a message when the command /help is issued"""
    update.message.reply_text('Help')')
    #edit help message with your message!

def echo(update, context):
    """ Just replying same text back """
    #echo, bot respond with your same message

def error(update, context):
    """Log Errors caused by Updates. """
    logger.warning('Update "%s" caused error "%s", update, context.error')

