import requests

def get_hitokoto():
    url = "https://v1.hitokoto.cn/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        hitokoto = data.get("hitokoto")
        return hitokoto
    except requests.RequestException as e:
        print(f"请求错误: {e}")
        return None

if __name__ == "__main__":
    result = get_hitokoto()
    if result:
        print("Hitokoto:", result)
    else:
        print("未获取到 hitokoto")