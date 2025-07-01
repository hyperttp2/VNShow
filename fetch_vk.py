import requests
import json
import os

print("🚀 Запуск скрипта...")

GROUP_ID = "-98487263"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")  # Получаем из GitHub Secrets

if not ACCESS_TOKEN:
    print("❌ Ошибка: ACCESS_TOKEN не найден")
    exit(1)

print("🔑 Токен загружен")

url = f" https://api.vk.com/method/wall.get?owner_id={GROUP_ID}&count=30&access_token={ACCESS_TOKEN}&v=5.199"

print(f"📡 Запрашиваем данные у ВК: {url[:100]}...")

res = requests.get(url).json()
print("📥 Получен ответ от ВК:", res)

items = res.get("response", {}).get("items", [])

image_urls = []
for item in items:
    if "attachments" in item:
        for attach in item["attachments"]:
            if attach.get("type") == "photo":
                photo = attach.get("photo", {})
                image_url = photo.get("photo_1280") or photo.get("photo_807") or photo.get("photo_604")
                if image_url:
                    image_urls.append(image_url)

print(f"🖼️ Найдено изображений: {len(image_urls)}")

with open("data.json", "w") as f:
    json.dump(image_urls, f, indent=2)

print("✅ Файл data.json успешно создан")
