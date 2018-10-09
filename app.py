from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    pot = request.args.get('potato')
    return 'potato: {}'.format(str(pot))

@app.route('/weather', methods=['GET'])
def weather():
    temperature = int(request.args.get('temperature'))
    if temperature < 30:
        return "It's way too cold! Wear a winter jacket"
    elif temperature < 55:
        return "It's still kinda chilly"
    else:
        return "I like the weather"