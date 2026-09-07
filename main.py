import websocket
import json
from analyzer import VolatilityAnalyzer

analyzer = VolatilityAnalyzer()

def on_message(ws, message):
    data = json.loads(message)
    if 'tick' in data:
        price = data['tick']['quote']
        digit = int(str(price)[-1])
        analyzer.add_tick(digit)
        prediction = analyzer.predict()
        print(f"Price: {price} | Digit: {digit} | Predict: {prediction}")

def on_open(ws):
    print("Bot Connected!")
    ws.send(json.dumps({"ticks": "R_75"}))

ws = websocket.WebSocketApp("wss://ws.binaryws.com/websockets/v3?app_id=1089",
  on_open=on_open,
  on_message=on_message)

ws.run_forever()
