from flask import Flask, render_template, Response
from flask import abort, redirect, url_for
import json
from api.docker_rdr import dockerReader

app = Flask(__name__, template_folder='template', static_folder='template/static')

@app.route('/')
def index():
    return redirect(url_for('dash'))

@app.route('/dash')
def dash():
    retorno = dockerReader() 
    if retorno is not None:
        return render_template("index.html", listServices=retorno)
    else:
        return "404"

@app.route('/info')
def info():
    retorno = dockerReader() 
    jsonResponse = json.dumps(retorno)    
    resp = Response(jsonResponse, status=200, mimetype='application/json')
    return resp
    
if __name__ == "__main__":
    app.run()