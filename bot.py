from flask import Flask, request
import os, requests

BOT_TOKEN   = '8127820339:AAGW5glNJx6IJtFdBNMUit_-6n86nOrW2-c'
WEBHOOK_URL = 'https://eldoll2.onrender.com'     # ваш поддомен
CHANNEL_ID  = -1001087968824                     # id вашего канала
API_URL     = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

def send_message(cid, text):
    r = requests.post(f"{API_URL}/sendMessage", json={"chat_id": cid, "text": text})
    if not r.ok: print("❌ sendMessage:", r.text)

def send_photo(fid, caption=''):
    r = requests.post(f"{API_URL}/sendPhoto",
                      json={"chat_id": CHANNEL_ID, "photo": fid, "caption": caption})
    if not r.ok: print("❌ sendPhoto:", r.text)

@app.route('/webhook', methods=['POST'])
def webhook():
    upd = request.get_json(force=True)
    msg = upd.get('message', {})
    cid = msg.get('chat', {}).get('id')
    text = msg.get('text', '')

    if text.startswith('/start'):
        send_message(cid, 'Дякуємо за замовлення 💛 Надішліть фото‑відгук — і ми подаруємо промокод!')
    elif 'photo' in msg:
        fid = msg['photo'][-1]['file_id']
        send_photo(fid, f'Фото від {cid}')
        send_message(cid, 'код: babywear5555')
    return 'OK'

if __name__ == '__main__':
    requests.get(f"{API_URL}/setWebhook?url={WEBHOOK_URL}/webhook")
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
