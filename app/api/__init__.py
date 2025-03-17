from .hello.routes import hello_bp

def init_api(app):
    app.register_blueprint(hello_bp, url_prefix='/api-x')
