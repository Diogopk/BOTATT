import schedule
from telegram import Bot
import asyncio

TOKEN = '7479524024:AAE0WAun0HEQo9QeHYnI5lALtdtWddQyFFU'
GROUP_CHAT_IDS = [
    '-1002248961927',
    '-1002233378018',
    '-1002244712891',
    '-1002486468642',
    '-1002172438260'
]
bot = Bot(token=TOKEN)

# Função para enviar mensagens
async def send_message(message):
    for chat_id in GROUP_CHAT_IDS:
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"Mensagem enviada para o chat {chat_id}")
        except Exception as e:
            print(f"Erro ao enviar para o chat {chat_id}: {e}")

# Função para agendamento
def schedule_task(message):
    asyncio.run(send_message(message))

# Mensagem
MESSAGE = "Mensagem de teste para grupos."

# Agendar mensagens
schedule.every(1).minutes.do(schedule_task, MESSAGE)  # Executar a cada 1 minuto para teste

# Loop do agendador
while True:
    schedule.run_pending()
