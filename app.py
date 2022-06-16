from crypt import methods
import imp
from flask import Flask

app= Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine learning Project-next try"


if __name__=="__main__":
    app.run(debug=True)