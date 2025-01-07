import requests


API_KEY = 'api_key'  # 你需要替换为自己的 API 密钥

URL = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={API_KEY}"


def send_reminder():
    webhook_url = URL
    message = {
        "msgtype": "text",
        "text": {
            "content": "@所有人 工时系统填写！",
            # "mentioned_list": ["@all"]
        }
    }
    requests.post(webhook_url, json=message)


send_reminder()
