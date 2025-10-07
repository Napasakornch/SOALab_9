from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/botdata")
def get_bot_data():
    CLIENT_ID = "f36aba42-48a6-4146-9261-4a201ee1a24e"
    url = "https://apigw1.bot.or.th/bot/public/Stat-ExchangeRate/v2/DAILY_AVG_EXG_RATE/"
    params = {
        "start_period": "2017-10-01",
        "end_period": "2017-10-30"
    }
    headers = {
        "X-IBM-Client-Id": CLIENT_ID,
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
