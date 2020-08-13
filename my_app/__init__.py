from flask import Flask 
from my_app.offer.views import offer

app = Flask(__name__)
app.register_blueprint(offer)
app.config.from_object('config.ProductionConfig')