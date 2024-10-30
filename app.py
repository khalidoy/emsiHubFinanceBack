# app.py

from flask import Flask
from flask_mongoengine import MongoEngine
from config import Config
import logging
from logging.handlers import RotatingFileHandler
import os
from flask_cors import CORS

# Initialize MongoEngine
db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    
    # Enable CORS for all routes and origins
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=False)
    
    # Register Blueprints
    from routes.auth import auth_bp
    from routes.students import students_bp
    from routes.payments import payments_bp
    from routes.depences import depences_bp
    from routes.accounting import accounting_bp
    from routes.schoolyearperiods import schoolyearperiods_bp
    from routes.reports import reports_bp  # Import the reports blueprint
    from routes.creditreports import creditreports_bp  # Import the creditreports blueprint
    from routes.dailyaccreport import dailyacc_bp
    from routes.transportreport import transport_bp  
    from routes.paymentsReport import payments_report_bp  # Import the payments_report blueprint
    
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(students_bp, url_prefix='/students')
    app.register_blueprint(payments_bp, url_prefix='/payments')
    app.register_blueprint(depences_bp, url_prefix='/depences')
    app.register_blueprint(accounting_bp, url_prefix='/accounting')
    app.register_blueprint(schoolyearperiods_bp, url_prefix='/schoolyearperiods')
    app.register_blueprint(reports_bp, url_prefix='/reports')  # Register the reports blueprint
    app.register_blueprint(creditreports_bp, url_prefix='/creditreports')  # Register the creditreports blueprint
    app.register_blueprint(dailyacc_bp, url_prefix='/dailyacc')
    app.register_blueprint(transport_bp, url_prefix='/transport')
    app.register_blueprint(payments_report_bp, url_prefix='/payments-report')  # Register the payments_report blueprint
    
    # Setup Logging
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/gsp_finance.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    
    app.logger.setLevel(logging.INFO)
    app.logger.info('GSP Finance Backend Startup')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
