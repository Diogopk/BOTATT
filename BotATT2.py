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

# Inicializar o bot com parâmetros ajustados
bot = Bot(token=TOKEN, connection_pool_size=10, pool_timeout=30)

# Função para enviar mensagens em lotes
async def send_message_in_batches(message):
    GROUP_BATCH_SIZE = 2  # Enviar mensagens para 2 grupos por vez
    for i in range(0, len(GROUP_CHAT_IDS), GROUP_BATCH_SIZE):
        batch = GROUP_CHAT_IDS[i:i + GROUP_BATCH_SIZE]
        for chat_id in batch:
            try:
                await bot.send_message(chat_id=chat_id, text=message)
                print(f"Mensagem enviada para o chat {chat_id}")
            except Exception as e:
                print(f"Erro ao enviar para o chat {chat_id}: {e}")
        await asyncio.sleep(2)  # Pausa de 2 segundos entre lotes

# Agendar mensagens
def schedule_task(message):
    asyncio.run(send_message_in_batches(message))

# Mensagem padrão
MESSAGE = "Mensagem de teste para grupos."

# Agendar as mensagens
schedule.every(1).minutes.do(schedule_task, MESSAGE)

# Loop para executar o agendamento
while True:
    schedule.run_pending()
