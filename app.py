from flask import Flask, request
import json, inspect
from binance.um_futures import UMFutures as Client

app = Flask(__name__)

@app.route("/", methods=['POST'])
def webhook():
    
    try:
        data = json.loads(request.data)
        ticker = data['ticker']
        exchange = data['exchange']
        price = data['price']
        side = data['side']
        positionSide = data['positionSide']
        quantity = data['quantity']
        binanceApiKey = data['binanceApiKey']
        binanceSecretKey = data['binanceSecretKey']
        params = {
            "symbol": ticker,
            "side": side,
            "positionSide": positionSide,
            "type": "MARKET",
            "quantity": quantity,
        }
        Client(binanceApiKey, binanceSecretKey).new_order(**params)
        
    except Exception as e:
        funcName = inspect.stack()[0][3]
        print(f"{funcName}() fonsiyonunda hata oluştu: {e}")
    return {
        "code": "success"
    }
        
        

# app.run()
app.run(host='0.0.0.0', port = 80, debug=True)
