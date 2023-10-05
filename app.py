# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, world! Im Mahesh. Deployment is not successfull'

# if __name__ == '__main__':
#     app.run()
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! Im Mahesh. Deployment is successful'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

