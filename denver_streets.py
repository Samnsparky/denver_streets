from flask import Flask, Response, url_for, request, json
from jinja2 import *
import os
import urllib2
import datetime
import database
import models
from models import *

def shutdown_session(exception=None):
    session.remove()

app = Flask(__name__)
env = Environment(loader=PackageLoader('denver_streets', 'templates'))

@app.route('/')
def index():
    items = ['closures']
    response = { 'items' : [] }
    [ response['items'].append({item+"_href": url_for(item)}) for item in items]
    response_data = json.dumps(response)
    response = Response(response_data, status=200, mimetype='application/json', headers={'Access-Control-Allow-Origin':'*'})
    return response

@app.route('/closures')
def closures():
    closures = database.session.query(Closure).all()
    closures_array = []
    for closure in closures:
        closures_array.append(closure.to_dict())
    response = Response(json.dumps({'items': closures_array}), status=200, mimetype='application/json', headers={'Access-Control-Allow-Origin':'*'})
    return response

@app.route('/closures/<int:closure_id>')
def closure_id():
    return ""
# find closure with closure_id

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
