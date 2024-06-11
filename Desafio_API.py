# !pip install flask
# !pip install flask-ngrok
# !pip install pyngrok


from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok
import json


app = Flask(__name__)
run_with_ngrok(app)


planilha_de_dados = [
    {"id":1,"Name":"Mahesh", "Age":25, "City":"Bangalore", "Country":"India"},
    {"id":2,"Name":"Alex", "Age":26, "City":"London", "Country":"UK"},
    {"id":3,"Name":"David", "Age":27, "City":"San Francisco", "Country":"USA"},
    {"id":4,"Name":"John", "Age":28, "City":"Toronto", "Country":"Canada"},
    {"id":5,"Name":"Chris", "Age":29, "City":"Paris", "Country":"France"}
]


@app.route('/index', methods=['GET'])
def index():
  return jsonify(planilha_de_dados)


ngrok_tunnel = ngrok.connect(5000)
if __name__ == "__main__":
  app.run()
