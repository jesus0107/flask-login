
from src.app import app
from config import settings

if __name__ == "__main__":
    app.config.from_object(settings['development'])
    app.run()