import asyncio
import json
import os
from telethon.sync import TelegramClient
from telethon.tl.types import Message

# Получаем данные из секретов GitHub
API_ID = os.environ.get("TELEGRAM_API_ID")
API_HASH = os.environ.get("TELEGRAM_API_HASH")
CHANNEL_USERNAME = os.environ.get("TELEGRAM_CHANNEL_ID")
SESSION_NAME = "telegram_session"

async def main():
    # Создаем клиент и подключаемся
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        posts_data = []
        
        # Запрашиваем 100 последних сообщений
        async for message in client.iter_messages(CHANNEL_USERNAME, limit=100):
            if isinstance(message, Message) and message.text:
                post = {
                    'id': message.id,
                    'text': message.text,
                    'date': message.date.isoformat() # Сохраняем дату в стандартном формате
                }
                posts_data.append(post)

    # Сохраняем данные в posts.json
    with open("posts.json", "w", encoding="utf-8") as f:
        json.dump({"posts": posts_data}, f, ensure_ascii=False, indent=4)
    
    print(f"Успешно сохранено {len(posts_data)} постов в posts.json")

# Запускаем асинхронную функцию
if __name__ == "__main__":
    asyncio.run(main())
