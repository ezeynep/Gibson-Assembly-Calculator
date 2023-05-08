from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#Create routes for different segments
@auth.route('/Protocol')
def Protocol():
    return render_template("protocol.html")

@auth.route('/twoFragments')
def twoFragments():
    return render_template("twoFragments.html")

@auth.route('/threeFragments')
def threeFragments():
    return render_template("threeFragments.html")

@auth.route('/fourFragments')
def fourFragments():
    return render_template("fourFragments.html")

@auth.route('/fiveFragments')
def fiveFragments():
    return render_template("fiveFragments.html")


