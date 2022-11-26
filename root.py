from flask import Flask, Response
from bin.accueil import accueil_page, about_page, service_page, gallery_page

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\xd7s\xdb\xe8\xdd+\xde\x84z5\xae@\x8dI\xce\xc2'
app.register_blueprint(accueil_page)
app.register_blueprint(about_page)
app.register_blueprint(service_page)
app.register_blueprint(gallery_page)

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/robots.txt')
def noindex():
    r = Response(response="User-Agent: *\nDisallow: /\n", status=200, mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r

@app.errorhandler(404)
def page_not_found(e):
    return "error 404"

@app.errorhandler(500)
def internal_server_error(e):
    return "error 500"
