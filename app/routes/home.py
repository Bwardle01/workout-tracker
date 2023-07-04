from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')

# render home page.
@bp.route('/')
def index():
  return render_template('home.html')

# render login page.
@bp.route('/login')
def login():
  # not logged in yet
  # if session.get('loggedIn') is None:
    return render_template('login.html')

#   return redirect('/')

# redner profile page.
# @bp.route('/profile')
# def single(id):
#   return render_template('single-post.html')