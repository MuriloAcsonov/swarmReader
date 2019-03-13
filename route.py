from flask import Flask, render_template
from flask import abort, redirect, url_for
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
    return render_template("info_block.html")
    
if __name__ == "__main__":
    app.run()