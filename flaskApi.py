from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-message")
def get_message():
    message_data = {
        "message": "Hello World!"
    }
    return jsonify(message_data), 200

@app.route("/create-message", methods=["POST"])
def create_message():
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)