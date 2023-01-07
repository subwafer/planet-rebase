from flask import Flask

def create_app(config=None):
    app = Flask(__name__)
    
    if config:
        app.config.from_object(config)
        
    @app.get('/heartbeat')
    def heartbeat():
        status = {
            'message': 'badum badum badum',
            'app_name': 'planet-rebase',
            'app_version': '0.1.0'
        }
        
        return status, 200
    
    return app
