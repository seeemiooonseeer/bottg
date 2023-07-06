import datetime
from telegram.ext import Updater, MessageHandler, Filters

keyword_count = 0
last_mention_time = None

def message_handler(update, context):
    global keyword_count, last_mention_time
    message_text = update.message.text.lower()
    if ('сосед'or 'соседи'or 'соседу'or 'соседа'or 'соседям'or 'Соседям'or 'Сосед'or 'Соседу'or 'Соседи') in message_text:
        keyword_count += 1
        current_time = datetime.datetime.now()

        if last_mention_time is not None:
            time_difference = current_time - last_mention_time
            time_formatted = str(time_difference)
            update.message.reply_text(f"Прошло {time_formatted} с последнего упоминания слова 'сосед'. Количество упоминаний: {keyword_count}")

        last_mention_time = current_time

updater = Updater("6318509656:AAFKaxPfHSz16HIFHmysUMKuF_52eMAhv04", use_context=True)
dispatcher = updater.dispatcher
message_handler = MessageHandler(Filters.text, message_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()