import asyncio
from telegram import Bot
import schedule

# Token e IDs dos grupos
TOKEN = '7479524024:AAE0WAun0HEQo9QeHYnI5lALtdtWddQyFFU'
GROUP_CHAT_IDS = [
    '-1002248961927',
    '-1002233378018',
    '-1002244712891',
    '-1002486468642',
    '-1002172438260'
]

# Inicializar o bot
bot = Bot(token=TOKEN)

# Função para enviar mensagens de forma sequencial com atrasos
async def send_message_sequential(message):
    for chat_id in GROUP_CHAT_IDS:
        try:
            await bot.send_message(chat_id=chat_id, text=message)
            print(f"Mensagem enviada para o chat {chat_id}")
            await asyncio.sleep(1)  # Atraso de 1 segundo entre mensagens
        except Exception as e:
            print(f"Erro ao enviar para o chat {chat_id}: {e}")

# Função para agendar tarefas
def schedule_task(message):
    asyncio.run(send_message_sequential(message))

# Mensagem padrão
MESSAGE = "Mensagem de teste enviada pelo bot."

# Agendar mensagens
schedule.every(1).minutes.do(schedule_task, MESSAGE)  # Teste com envio a cada 1 minuto

# Loop para executar o agendador
while True:
    schedule.run_pending()
