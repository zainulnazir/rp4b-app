# filepath: venipuncture_app/app.py
from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)
IMAGE_FOLDER = os.path.join("static", "images")


@app.route("/")
def index():
    images = os.listdir(IMAGE_FOLDER)
    return render_template("index.html", images=images)


@app.route("/images/<filename>")
def image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
