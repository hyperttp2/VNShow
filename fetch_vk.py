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

url = f"https://api.vk.com/method/wall.get?owner_id={GROUP_ID}&count=30&access_token={ACCESS_TOKEN}&v=5.199"

print(f"📡 Запрашиваем данные у ВК: {url[:100]}...")

res = requests.get(url).json()
print("📥 Получен ответ от ВК:", res)

items = res.get("response", {}).get("items", [])

slides = []

for item in items:
    if "attachments" in item:
        for attach in item["attachments"]:
            if attach.get("type") == "photo":
                photo = attach.get("photo", {})
                sizes = photo.get("sizes", [])
                image_url = None
                for size in sizes:
                    if size["type"] in ["x", "y", "w", "z"]:  # Берём большие размеры
                        image_url = size["url"]
                        break
                if image_url:
                    text = item.get("text", "").strip()
                    slides.append({
                        "image": image_url,
                        "text": text
                    })

print(f"🖼️ Найдено постов с фото и текстом: {len(slides)}")

with open("data.json", "w") as f:
    json.dump(slides, f, indent=2)

print("✅ Файл data.json успешно создан")
