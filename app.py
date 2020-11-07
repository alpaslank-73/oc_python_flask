from flask import Flask, render_template, request, session, redirect, url_for, g, Response

#from flask import Flask, request


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return ('Hello World - 4')

@app.route('/healthz', methods = ['GET'])
def healthz():
    resp = app.make_response('ok')
    resp.headers['Custom-Header'] = 'Awesome'
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
