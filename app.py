from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
    <head>
        <title>Hello, Mahesh!</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
            }
            .container {
                text-align: center;
                margin-top: 100px;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #ffffff;
            }
            h1 {
                color: #007bff;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello, Mahesh!</h1>
            <p>Welcome to your colorful Flask app!</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

