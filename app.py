from flask import Flask


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['host'] = '0.0.0.0'


# Canary
@app.route('/canary')
def canary():
    return 'Ok'


if __name__ == '__main__':
    app.run(host=app.config['host'])
