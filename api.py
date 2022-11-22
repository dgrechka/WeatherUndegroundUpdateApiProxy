import flask
import os
import requests
from flask import request

debugMode = os.environ.get('DEBUG',False)

urlPath = '/weatherstation/updateweatherstation.php'

targetHost =os.environ.get('TARGET_URL',"https://weatherstation.wunderground.com")
print(f"Using host: {targetHost}\nUsing URL path: {urlPath}\nSet TARGET_URL to override host")

app = flask.Flask(__name__)

print(f'DEBUG env var set to f{debugMode}')
app.config["DEBUG"] = debugMode


@app.route(urlPath, methods=['GET'])
def proxy():
    args = request.args
    
    x = requests.request(
        method     = "GET",
        url        = f'{targetHost}/{urlPath}',
        params     = args
        )
    print(f"Ok {x.ok}; status: {x.status_code}")
    if x.ok:
        return x.text
    else:
        raise x.text

app.run(host="0.0.0.0")
