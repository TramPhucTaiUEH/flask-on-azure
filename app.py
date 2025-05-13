from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Render!"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))  # PORT do Render cấp
    app.run(host="0.0.0.0", port=port)
