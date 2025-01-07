import requests

# 使用 OpenWeatherMap API 查询天气
API_KEY = 'api_key'  # 你需要替换为自己的 API 密钥

URL = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={API_KEY}"

response = requests.get(URL)
data = response.json()
print(data)
