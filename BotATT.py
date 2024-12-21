import schedule
from telegram import Bot
import asyncio
import pytz
from datetime import datetime

# Definir o fuso horário (exemplo, horário de Brasília)
timezone = pytz.timezone("America/Sao_Paulo")

# Seu token do bot (verifique se está correto e ativo)
TOKEN = '7479524024:AAE0WAun0HEQo9QeHYnI5lALtdtWddQyFFU'

# IDs dos grupos (verifique se os grupos permitem mensagens do bot)
GROUP_CHAT_IDS = [
    '-1002248961927',
    '-1002233378018',
    '-1002244712891',
    '-1002486468642',
    '-1002172438260'
]

# Inicializar o bot
bot = Bot(token=TOKEN)

# Função para enviar mensagem
async def send_message(message):
    tasks = []
    for chat_id in GROUP_CHAT_IDS:
        tasks.append(bot.send_message(chat_id=chat_id, text=message))

    # Executar todas as mensagens
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Verificar se as mensagens foram enviadas com sucesso
    for chat_id, result in zip(GROUP_CHAT_IDS, results):
        if isinstance(result, Exception):
            print(f"Erro ao enviar para o chat {chat_id}: {result}")
        else:
            print(f"Mensagem enviada com sucesso para o chat {chat_id}")

# Função para agendar tarefas
def schedule_task(message):
    asyncio.run(send_message(message))

# Mensagem padrão
MESSAGE = """
⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
🚴🚴‍♀️     🏍🏍

Próximo turno se inicia em 1 hora.

Entregadores que se agendaram ficarão disponíveis automaticamente no APP.

QUEM NÃO SE AGENDOU, POR FAVOR, FAÇA SUA SOLICITAÇÃO DE VAGA NO GRUPO.

Pedimos que caso não possam rodar no turno agendado, nos informem com antecedência, por favor.
Antes de cada turno ser iniciado.

Contamos com a compreensão de todos e que nos ajudem nessas questões ✌🏻

Equipe ABJP RJ Taquara 💙
"""

# Agendar mensagens
schedule.every().day.at("00:00").do(schedule_task, MESSAGE)
schedule.every().day.at("00:02").do(schedule_task, MESSAGE)
schedule.every().day.at("00:03").do(schedule_task, MESSAGE)
schedule.every().day.at("21:00").do(schedule_task, MESSAGE)

# Loop para executar o agendamento
async def run_scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(1)

# Executar o agendador
if __name__ == "__main__":
    try:
        asyncio.run(run_scheduler())
    except Exception as e:
        print(f"Erro no bot: {e}")
