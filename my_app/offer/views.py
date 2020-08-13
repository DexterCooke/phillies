from flask import Blueprint, render_template 
from my_app.offer.models import calculate_offer

offer = Blueprint('offer', __name__)

@offer.route('/offer')
def contract():
    return render_template('home.html', offer=calculate_offer()) 