from flask import Flask, jsonify, send_from_directory
import os
import time

app = Flask(__name__)
IMAGE_FOLDER = os.path.join("static", "images")  # Adjust the path if needed


@app.route("/")
def index():
    images = os.listdir(IMAGE_FOLDER)
    image_data = []
    for img in images:
        if img.endswith((".jpg", ".jpeg", ".png", ".gif")):  # Filter for image files
            time_taken = round(time.time() * 1000)
            image_url = f"https://vulture-pet-hen.ngrok-free.app/images/{img}"
            image_data.append({"imageUrl": image_url, "timeTaken": time_taken})
    return jsonify(image_data)


@app.route("/images/<filename>")
def image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
