from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def asaas_webhook():
    data = request.json
    print("📬 Webhook recibido:", data)
    return "OK", 200
