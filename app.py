from dotenv import load_dotenv
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from gcp_helper import setup_cloud_logging

load_dotenv()

setup_cloud_logging()

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ready")
def ready():
    return "yes"
