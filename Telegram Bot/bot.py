import telegram.ext

Token = "5650427743:AAHKevGUvTpA8RFqxHHJ8CWX4FZes51_D7I"
updater = telegram.ext.Updater("5650427743:AAHKevGUvTpA8RFqxHHJ8CWX4FZes51_D7I", use_context =True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello Wclcome to Trading Career Premium VIP")


def help (update, context):
    update.message.reply_text(
    """
    /start -> Wclcome to Trading Career Premium VIP
    /help -> This Particular massage
    /VIP -> About VIP plan
    /Plan1 -> Purchase Plan 1
    /Plan2 -> Purchase Plan 2
    /done -> Purchase confirmation .
    /Support -> If their is any kind of problem .
    """)
def VIP (update, context):
    update.message.reply_text(
    """
    We provide premium singal with 100% Accuracy Their is 2 plans 
    Plan1 Lifetime Premium Membership 100$ 
    Plan2 Lifetime Premium Membership With Live Support 220$
    /plan1
    /plan2
    """
    )

def plan1 (update, context):
    update.message.reply_text(
    """
    Send 100$ to this Pay ID 
    165944283 
    And please provide us your transaction ID and screenshot. Happy Treading.
    """
    )

def plan2 (update, context):
    update.message.reply_text(
    """
    Send 220$ to this Pay ID 165944283 And please provide us your transaction ID and screenshot. Happy Treading.
    """
    )

def done (update, context):
    update.message.reply_text(
    """
    Thank You , welcome to our vip Channel Please join Using This Link - https://t.me/+TXzBoAswSY8wMTA1
    """
    )

def Support (update, context):
    update.message.reply_text(
    """
    For External Support it will take upto 4 to 8 hour
    """
    )
dispatcher.add_handler(telegram.ext.CommandHandler ('start',start))

dispatcher.add_handler(telegram.ext.CommandHandler ('help',help))

dispatcher.add_handler(telegram.ext.CommandHandler('VIP',VIP))

dispatcher.add_handler(telegram.ext.CommandHandler('plan1',plan1))

dispatcher.add_handler(telegram.ext.CommandHandler('plan2',plan2))

dispatcher.add_handler(telegram.ext.CommandHandler('done',done))

dispatcher.add_handler(telegram.ext.CommandHandler('Support',Support))

updater.start_polling()
updater.idle()