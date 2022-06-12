from flask import Flask
from flask_cors import CORS
from main_api import bp

app = Flask(__name__)
app.config.from_object("config.Config")
cors = CORS(app)
app.register_blueprint(bp)


if __name__ == "__main__":
    app.run()
