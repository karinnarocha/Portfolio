from flask import Flask
from flask_mail import Mail
from PORTIFOLIO.config import Config

mail = Mail()

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    mail.init_app(app)
    
    from .IndexPage.routes import indexPage
    from .AboutPage.routes import aboutPage
    from .ContactPage.routes import contactPage
    from .AlbertCaseStudy.routes import AlbertStudyCase 
    from .DaniellyCaseStudy.routes import DaniellyStudyCase
    from .HellenCaseStudy.routes import HellenStudyCase
    from .LulunremiCaseStudy.routes import  LulunremiStudyCase

    app.register_blueprint(indexPage)
    app.register_blueprint(AlbertStudyCase)
    app.register_blueprint(aboutPage)
    app.register_blueprint(contactPage)
    app.register_blueprint(DaniellyStudyCase)
    app.register_blueprint(HellenStudyCase)
    app.register_blueprint(LulunremiStudyCase)

    return app
