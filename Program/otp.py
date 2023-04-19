from flask import Flask, jsonify, request
import random
import json

app = Flask(__name__)


@app.route("/otp", methods=["POST"])
def generate_otp():
    data = request.get_data()
    data_json = json.loads(data)
    phone_number = data_json['phone_number']
    code = int("".join([str(random.randint(0, 10)) for _ in range(6)]))
    result = {"code": code, "phone_number": phone_number}
    return jsonify(result)


if __name__ == "__main__":
    app.run()