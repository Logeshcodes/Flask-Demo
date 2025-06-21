from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# Entry point for Vercel
def handler(request):
    return app(request.environ, start_response=request.send_response)
