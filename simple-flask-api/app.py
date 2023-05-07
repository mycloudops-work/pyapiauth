from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/post', methods=['POST'])
def testpost():
    input_data = request.get_json(force=True)
    dictToReturn = {'text':input_data['text']}
    return jsonify(dictToReturn)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True, use_reloader=True)