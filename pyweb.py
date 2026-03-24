from flask import Flask, jsonify
from datetime import date


pyweb = Flask(__name__)


@pyweb.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World - PyWeb</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
            }
            .container {
                text-align: center;
                background: white;
                padding: 50px;
                border-radius: 10px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            }
            h1 {
                color: #333;
                margin: 0;
            }
            p {
                color: #666;
                margin: 10px 0 0 0;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
            a:hover {
                background: #764ba2;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Hello World - PyWeb</h1>
            <p>Welcome to your Flask application!</p>
            <p>Try <a href="/api/time">Get Current Time</a></p>
        </div>
    </body>
    </html>
    """


@pyweb.route("/api/time")
def get_time():
    """Return current date as JSON."""
    today = date.today()
    return jsonify({
        "date": today.strftime("%m/%d/%Y"),
        "day": today.day,
        "month": today.month,
        "year": today.year
    })


if __name__ == "__main__":
    pyweb.run(debug=True)
