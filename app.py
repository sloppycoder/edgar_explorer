import json
import logging
import logging.config
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

load_dotenv()

with open(Path(__file__).parent / "logger_config.json", "r") as f:
    logging.config.dictConfig(json.load(f))


app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ready")
def ready():
    return "yes"
