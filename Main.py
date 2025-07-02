from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

@app.route('/notify', methods=['POST'])
def notify():
    data = request.get_json()
    name = data.get('name', 'ไม่ระบุชื่อ')
    timestamp = data.get('time', 'ไม่ระบุเวลา')
    text = f"📸 ตรวจพบการสแกนหน้า\n👤 ชื่อ: {name}\n🕒 เวลา: {timestamp}"
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={'chat_id': CHAT_ID, 'text': text}
    )
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
