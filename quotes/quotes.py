from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:postgres@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://cqxrukomawgqmw:fa1adebc80c82cd9c363fa7f382b7f89eb46fbbc9ca15cb14e0ed0445c1c684a@ec2-107-20-153-39.compute-1.amazonaws.com:5432/d1u73r8qfs4n0r'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Favquotes(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    author=db.Column(db.String(30))
    quote=db.Column(db.String(3000))

@app.route('/')
def index():
    result=Favquotes.query.all()
    return render_template('index.html',result=result)

@app.route('/quotes')
def quotes():
    return render_template('quotes.html')   

@app.route('/process',methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))

     