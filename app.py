from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from config.config import Config
from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp
from utils.logger import setup_logging
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize CORS with specific configuration
    CORS(app, 
         origins=["http://localhost:3000", "http://127.0.0.1:3000"],
         allow_headers=["Content-Type", "Authorization"],
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
    
    # Initialize mail
    mail = Mail(app)
    app.mail = mail
    
    # Setup logging
    setup_logging()
    
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    @app.route('/')
    def health_check():
        return {
            "status": "RetailShield AI Backend is running", 
            "version": "1.0.0",
            "endpoints": {
                "login": "/api/login",
                "status": "/api/status", 
                "admin_logs": "/api/admin/logs",
                "admin_blocks": "/api/admin/blocks",
                "admin_stats": "/api/admin/stats"
            }
        }
    
    @app.route('/api/health')
    def api_health():
        return {"status": "API is healthy", "timestamp": "2024-01-15T10:30:00Z"}
    
    # Add error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {"error": "Endpoint not found"}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return {"error": "Internal server error"}, 500
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("🚀 Starting RetailShield AI Backend...")
    print("📡 API will be available at: http://localhost:5000")
    print("🔗 Frontend should connect to: http://localhost:5000/api")
    print("🏥 Health check: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
