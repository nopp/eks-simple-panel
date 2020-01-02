import json
from flask import *
from lib.panel import *
import babel

app = Flask(__name__)
app.secret_key = 'BYG>.L*((*$jj2h>#'

panel = Panel()

@app.route("/")
def index():
    try:
        return render_template('index.html',results=panel.listNode(),totalnamespaces=panel.listNamespace(),namespaces=panel.listNamespace())
    except:
       print("Error - Can't show index.")

@app.route("/pods/<namespace>",methods=['GET'])
def nodes(namespace):
    try:
        return render_template('pods.html',results=panel.listPodByNamespace(namespace),ns=namespace,namespaces=panel.listNamespace())
    except:
       print("Error - Can't list pods.")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=9191, debug=True)