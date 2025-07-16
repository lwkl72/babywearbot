{\rtf1\ansi\ansicpg1251\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request\
import os, requests\
\
# === \uc0\u1042 \u1040 \u1064 \u1048  \u1044 \u1040 \u1053 \u1053 \u1067 \u1045  =========================================================\
BOT_TOKEN   = '8127820339:AAGW5glNJx6IJtFdBNMUit_-6n86nOrW2-c'\
WEBHOOK_URL = 'https://eldoll2.onrender.com'      # \uc0\u1085 \u1077  \u1079 \u1072 \u1073 \u1091 \u1076 \u1100 \u1090 \u1077  \u1087 \u1086 \u1076 \u1076 \u1086 \u1084 \u1077 \u1085 \
CHANNEL_ID  = -1001087968824                      # ID \uc0\u1082 \u1072 \u1085 \u1072 \u1083 \u1072  / \u1089 \u1091 \u1087 \u1077 \u1088 \u1075 \u1088 \u1091 \u1087 \u1087 \u1099 \
# ========================================================================\
\
API_URL = f"https://api.telegram.org/bot\{BOT_TOKEN\}"\
app = Flask(__name__)\
\
def send_message(chat_id, text):\
    r = requests.post(f"\{API_URL\}/sendMessage",\
                      json=\{"chat_id": chat_id, "text": text\})\
    if not r.ok:\
        print("\uc0\u10060  sendMessage error:", r.text)\
\
def send_photo_to_channel(file_id, caption=''):\
    r = requests.post(f"\{API_URL\}/sendPhoto",\
                      json=\{"chat_id": CHANNEL_ID, "photo": file_id,\
                            "caption": caption\})\
    if not r.ok:\
        print("\uc0\u10060  sendPhoto error:", r.text)\
\
@app.route("/webhook", methods=["POST"])\
def webhook():\
    upd = request.get_json(force=True)\
    msg = upd.get("message", \{\})\
    chat_id = msg.get("chat", \{\}).get("id")\
    text = msg.get("text", "")\
\
    if text.startswith("/start"):\
        send_message(chat_id,\
            "\uc0\u1044 \u1103 \u1082 \u1091 \u1108 \u1084 \u1086  \u1079 \u1072  \u1079 \u1072 \u1084 \u1086 \u1074 \u1083 \u1077 \u1085 \u1085 \u1103  \u55357 \u56475  \u1053 \u1072 \u1076 \u1110 \u1096 \u1083 \u1110 \u1090 \u1100  \u1092 \u1086 \u1090 \u1086 \u8209 \u1074 \u1110 \u1076 \u1075 \u1091 \u1082  \'97 \u1110  \u1084 \u1080  \u1087 \u1086 \u1076 \u1072 \u1088 \u1091 \u1108 \u1084 \u1086  \u1074 \u1072 \u1084  \u1087 \u1088 \u1086 \u1084 \u1086 \u1082 \u1086 \u1076 !")\
    elif "photo" in msg:\
        file_id = msg["photo"][-1]["file_id"]\
        send_photo_to_channel(file_id, f"\uc0\u1060 \u1086 \u1090 \u1086  \u1074 \u1110 \u1076  \{chat_id\}")\
        send_message(chat_id, "\uc0\u1082 \u1086 \u1076 : babywear5555")\
\
    return "OK"\
\
if __name__ == "__main__":\
    resp = requests.get(f"\{API_URL\}/setWebhook?url=\{WEBHOOK_URL\}/webhook")\
    print("\uc0\u55357 \u56615  setWebhook:", resp.text)\
    port = int(os.getenv("PORT", 5000))\
    app.run(host="0.0.0.0", port=port)\
}