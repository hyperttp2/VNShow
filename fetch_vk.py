import requests
import json
import os

GROUP_ID = "-98487263"
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")  # <-- Получаем токен из переменной окружения

if not ACCESS_TOKEN:
    raise ValueError("ACCESS_TOKEN не найден в переменных окружения")

url = f"https://api.vk.com/method/wall.get?owner_id={GROUP_ID}&count=30&access_token={ACCESS_TOKEN}&v=5.199"

res = requests.get(url).json()
items = res.get("response", {}).get("items", [])

image_urls = []
for item in items:
    if "attachments" in item and item["attachments"][0]["type"] == "photo":
        photo = item["attachments"][0]["photo"]
        image_url = photo.get("photo_1280") or photo.get("photo_807") or photo.get("photo_604")
        if image_url:
            image_urls.append(image_url)

with open("data.json", "w") as f:
    json.dump(image_urls, f, indent=2)
