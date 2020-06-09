from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '2346882f1c3d7bd12480bc6c2b39dd96'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://vhxomcftugirup:164208ed27dbf52ef74ecbce78ee37c6d1252d230a9dd15dc3228c75766ce188@ec2-35-174-88-65.compute-1.amazonaws.com:5432/d8nml3fptpdh5i'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)



from application import route
