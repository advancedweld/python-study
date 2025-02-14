from .hello.hello import hello_bp

def init_api(app):
    app.register_blueprint(hello_bp, url_prefix='')
