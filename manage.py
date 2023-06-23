from app import create_app
from config import DevelopmentConfig

if __name__ == '__main__':
    config = DevelopmentConfig()
    app = create_app()
    app.run()

# TODO Add manager
