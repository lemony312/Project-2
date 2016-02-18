from flask import Flask
from datetime import timedelta

app = Flask(__name__, static_url_path='')

app.secret_key = 'ndapp development key'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@dinerscode.com'
app.config["MAIL_PASSWORD"] = 'DinersCode2015'
# session lifetime to keep user logged in
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(1000)

import nd_app.models
#import nd_app.forms
import nd_app.routes

from nd_app.routes import mail
mail.init_app(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://neurod_devuser:devpwd@166.62.40.36/neurod_database'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://neurod_devuser:devpwd@166.62.40.36/neurod_webappdev'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ndsitedev:devpwd@mysql.server/ndsitedev$NeuroDining_2015'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://devuser:devpwd@localhost/NeuroDining'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 499
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20

from nd_app.models import db
db.init_app(app)



