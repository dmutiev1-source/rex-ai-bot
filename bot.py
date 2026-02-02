import os
from datetime import datetime
from telegram.ext import Updater

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_report(context):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    text = f"""
🤖 REX-AI | Market Report
🕒 {now}

📊 Фьючерсы: анализ формируется
🪙 Криптовалюта: анализ формируется
🥇 Золото: анализ формируется
🛢 Нефть: анализ формируется

📰 Новости:
— мониторинг рынка активен

⚠️ Не инвестиционная рекомендация
"""
    context.bot.send_message(chat_id=CHAT_ID, text=text)

updater = Updater(TOKEN, use_context=True)
updater.job_queue.run_repeating(send_report, interval=3600, first=10)
updater.start_polling()
updater.idle()
