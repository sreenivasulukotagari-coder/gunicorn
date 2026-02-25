from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json.get("message", "").lower()
    return jsonify({
        "reply": f"Travel suggestion received: {user}. Have a happy journey!"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)