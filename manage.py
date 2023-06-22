import os

from app import create_app

if __name__ == '__main__':
    app = create_app(os.getenv('FLASK_ENV') or 'config.DevelopmentConfig')
    app.run()

# TODO Add manager
