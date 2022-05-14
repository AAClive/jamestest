from flask import Flask
from flask import SQLACHEMLY
from flask import request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def siginup():
    if request.method=="POST":
        user=request.form.get("username")
    return render_template("signup")
        

if __name__=="__main__":
    app.run()
