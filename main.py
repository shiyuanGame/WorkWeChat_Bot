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

    # 发送 POST 请求
    response = requests.post(webhook_url, json=message)

    # 打印返回的状态码
    print(f"Status Code: {response.status_code}")

    # 如果返回的是 JSON 数据，可以尝试解析并打印
    try:
        response_data = response.json()
        print(f"Response JSON: {response_data}")
    except ValueError:
        # 如果响应不是 JSON 格式，打印原始响应内容
        print(f"Response Text: {response.text}")


print("--执行前----")
send_reminder()
print("--执行后----")
