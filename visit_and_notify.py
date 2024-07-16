import requests

def visit_url():
    url = "https://d.kstore.space/download/8026/jsm.json"
    response = requests.get(url)
    return response.status_code, response.text

def send_telegram_message(message):
    bot_token = "7383665841:AAE_RBf5P2zFA3LA2tZ0AkrvoTn13kr1FtM"
    chat_id = "6264072063"
    send_text = f"https://api.telegram.org/bot7383665841:AAE_RBf5P2zFA3LA2tZ0AkrvoTn13kr1FtM/sendMessage?chat_id=6264072063&text={message}"
    response = requests.get(send_text)
    return response.status_code

if __name__ == "__main__":
    status_code, content = visit_url()
    message = f"Visited URL, Status Code: {status_code}, Content: {content[:200]}"  # Limit content length
    send_telegram_message(message)
