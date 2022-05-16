from flask import Flask
from flask import flash
from flask_sqlalchemy import SQLAlchemy
from flask import request
app=Flask(__name__)
db=SQLAlchemy(app)
DB_NAME="database.db"
#datra base init
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///{DB_NAME}'
db.SQLlchemy(app)

class Users(db.Model):
    id=db.Column("id", db.Integer, primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    def __init__(self, email):
        self.email=email
@app.route("/",methods=["GET","POST"])
def siginup():
    if request.method=="POST":
        user=request.form.get("email")
        pas=request.form.get("password")
        if user or pas==None:
            flash("[SERVER] invalid email or password, try again!")
            user=Users()
    return render_template("signup.html")
        

if __name__=="__main__":
    db.create_all()
    app.run()
