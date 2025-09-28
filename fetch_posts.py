import requests
import json
import os

# Получаем секреты из GitHub Actions
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = os.environ.get("TELEGRAM_CHANNEL_ID") # Например, @tonmonitoring

# Формируем URL для запроса к Telegram Bot API
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatHistory?chat_id={CHANNEL_ID}&limit=100"

# Отправляем запрос и получаем ответ
response = requests.get(url)
data = response.json()

# Сохраняем результат в файл
with open("posts.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Посты успешно сохранены в posts.json")
