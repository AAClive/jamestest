from flask import Flask
from flask import SQLACHEMLY
from flask import request

app=Flask(__app__)

@app.route("/",methods={"GET","POST"])
def siginup():
    if request.method=="POST":
        user=request.form.get("username")
        

if __name__=="__main__":
    app.run()
