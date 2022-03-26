from datetime import datetime, timedelta
from flask import Flask
from flask.helpers import make_response
from flask import request
from flask import redirect;
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS, cross_origin
import jwt
from dbpy import Data, Base

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismyflasksecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:qwerty123@localhost/py3'
datab = SQLAlchemy(app)


@app.route('/login')
def login():

    auth = request.authorization
    res = datab.session.query(Data).all()
    for row in res:
        if auth and auth.username == row.login:
            if auth and auth.password == row.password:
                log = auth.username
                token = jwt.encode({'user':auth.username, 'exp':datetime.utcnow() + timedelta(minutes=30)}, app.config['SECRET_KEY'])
                user = datab.session.query(Data).filter_by(login = log).first()
                user.token = token
                datab.session.commit()
                return  jsonify({'token': token})
            else:
                   continue
        else:
             continue
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'}) 


@app.route('/protected')
def protected():

    token = request.args.get('token')
    tokens = datab.session.query(Data).all()
    for row in tokens:
        if token == row.token:
            return '<h1>Hello Dear {}! token is correct! </h1>'.format(row.login)
        else:
            continue

        return '<h1>Sorry! The token is incorrect!</h1>'.format(token)



if __name__ == '__main__':
    app.run(debug=True)