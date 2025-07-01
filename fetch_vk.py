import requests
import json

GROUP_ID = "-98487263"
ACCESS_TOKEN = "vk1.a.06J_lFc3VX4J5kA4Fc432jmPK-nDmNzwjuH3qmbSxOU4yc2gpgWtbbDn0a63dJ3O6g-O_sVYdOymd39H7aTG6oZSeVKRHbjWUc_EA9_uZuJRmb1qYKcmL3JcLnqZ_FEevdA5kXvaO-aN-NgN96uXr4_mr6_yjK36PQ1JAIj2ENM16TPbrFubk77EqlgbbU-rcxtKcw3cKrzY-8xio-aCzg"

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
