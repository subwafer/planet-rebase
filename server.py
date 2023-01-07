from src import create_app
from config import load_config

if __name__ == "__main__":
    config = load_config()
    server = create_app(config)
    
    server.run(
        debug=config.DEBUG,
        host=config.HOST,
        port=config.PORT
    )