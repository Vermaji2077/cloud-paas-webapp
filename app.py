
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Cloud Computing Practical 5</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: #eaf4ff;
                padding: 100px 20px;
            }
            h1 { color: #1769aa; }
            .card {
                background: white;
                padding: 30px;
                border-radius: 12px;
                max-width: 600px;
                margin: auto;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Cloud Web Application!</h1>
            <p>Cloud Computing Practical 5</p>
            <p>PaaS Deployment using Render</p>
            <p>Status: Application is running successfully.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
