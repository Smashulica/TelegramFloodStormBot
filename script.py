def start(update, context):
    context.bot.sendMessage(chat_id=update.message.chat_id, 'Text One')
            
def leave(update, context):
    for i in range(100):
         bot.leaveChat(chat_id=update.message.chat_id)
         sleep(0.01)
 
def flodd(update, context):
    while leave:
         context.bot.sendMessage(chat_id=update.message.chat_id, 'Text Two')
         sleep(0.05)
		 
#Non toccare questo script se non sai riprogrammarlo, modifica solo i messaggi.
#Do not touch this script if you can not reprogram it, change only the messages.
