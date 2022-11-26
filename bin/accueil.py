from flask import render_template, Blueprint

accueil_page = Blueprint('accueil_page', __name__, template_folder='templates')
about_page = Blueprint('about_page', __name__, template_folder='templates')
gallery_page = Blueprint('gallery_page', __name__, template_folder='templates')
service_page = Blueprint('service_page', __name__, template_folder='templates')


@accueil_page.route('/')
def accueil():
    return render_template('index.html')

@about_page.route('/about')
def accueil():
    return render_template('about.html')

@gallery_page.route('/gallery')
def accueil():
    return render_template('gallery.html')

@service_page.route('/service')
def accueil():
    return render_template('service.html')