from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! I'm Mahesh. Deployment is successfull'

if __name__ == '__main__':
    app.run()

