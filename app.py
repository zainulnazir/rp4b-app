""" Libraries """
import os
import time
from flask import Flask, jsonify, render_template, send_from_directory, redirect
from flask_cors import CORS

app = Flask(__name__, template_folder="templates")
CORS(app)  # Enable CORS for all routes
IMAGE_FOLDER = os.path.join("static", "images")


@app.route("/")
def index():
    return redirect("/web")


@app.route("/web")
def web_endpoint():
    """Returns a list of images to be displayed on a webpage"""
    images = [
        img
        for img in os.listdir(IMAGE_FOLDER)
        if img.endswith((".jpg", ".jpeg", ".png", ".gif"))
    ]
    return render_template("index.html", images=images)


@app.route("/images/<filename>")
def get_image(filename):
    """Returns the image file"""
    try:
        return send_from_directory(IMAGE_FOLDER, filename)
    except FileNotFoundError:
        return jsonify({"error": "Image not found"}), 404


@app.route("/api/images")
def api_images():
    images_data = []
    for img in os.listdir(IMAGE_FOLDER):
        if img.endswith((".jpg", ".jpeg", ".png", ".gif")):
            images_data.append(
                {
                    "imageUrl": f"http://<raspberry_pi_ip>:5001/images/{img}",
                    "timeTaken": int(time.time()),
                }
            )
    return jsonify(images_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
