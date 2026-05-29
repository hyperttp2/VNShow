import requests
import json
import os

print("🚀 Запуск скрипта...")

GROUP_ID = "-98487263"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

if not ACCESS_TOKEN:
    print("❌ Ошибка: ACCESS_TOKEN не найден")
    exit(1)

url = f"https://api.vk.com/method/wall.get?owner_id={GROUP_ID}&count=30&access_token={ACCESS_TOKEN}&v=5.199"

print(f"📡 Запрашиваем данные у ВК...")

res = requests.get(url).json()

if "error" in res:
    print(f"❌ Ошибка VK API: {res['error']['error_msg']}")
    exit(1)

items = res.get("response", {}).get("items", [])

slides = []

for item in items:
    if "attachments" in item:
        for attach in item["attachments"]:
            if attach.get("type") == "photo":
                photo = attach.get("photo", {})
                sizes = photo.get("sizes", [])
                
                # Выбираем фото с максимальной площадью (width * height)
                best_photo = None
                best_size = 0
                
                for size in sizes:
                    width = size.get("width", 0)
                    height = size.get("height", 0)
                    area = width * height
                    if area > best_size:
                        best_size = area
                        best_photo = size.get("url")
                        print(f"  Найдено фото {width}x{height} (площадь: {area})")
                
                if best_photo:
                    text = item.get("text", "").strip()
                    slides.append({
                        "image": best_photo,
                        "text": text
                    })
                    print(f"✅ Добавлен пост с фото, размер: {best_size} пикселей")
                    break  # берем только одно фото из поста

print(f"\n🖼️ Всего найдено постов с фото: {len(slides)}")

# Сохраняем с нормальной кодировкой
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(slides, f, indent=2, ensure_ascii=False)
    
print("✅ data.json сохранен")
