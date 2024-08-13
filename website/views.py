from flask import Blueprint,render_template, redirect, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')