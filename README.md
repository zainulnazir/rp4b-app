# Vein Detector System - Flask App

This Flask app is designed to display processed images from a Vein Detector System based on the IR spectrum. It is optimized to run on a **Raspberry Pi 4B** with **Raspberry Pi OS**.

## Prerequisites

- **Raspberry Pi 4B** (or compatible)
- **Raspberry Pi OS** (preferably the latest version, based on Debian Bullseye)
- **Python 3.x** (pre-installed on Raspberry Pi OS)
- **Pip** (Python package manager)
- **Git** (to clone the repository)

---

## Setup Instructions

### 1. Install Git
Git is not pre-installed on Raspberry Pi OS. To install it, run:
```bash
sudo apt update
sudo apt install git
```

Verify the installation:

```bash
git --version
```

### 2. Clone the Repository

Clone this repository to your Raspberry Pi:

```bash
git clone https://github.com/zainulnazir/rp4b-app.git
cd rp4b-app/
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Prepare the Image Folder

Place your processed images in the static/images/ folder. Supported formats: .jpg, .jpeg, .png, .gif.

### 5. Run the Flask App

Start the Flask application:

```bash
python app.py
```

The app will be accessible at:

```bash
http://<raspberry_pi_ip>:5001
```

### 6. Access the Web Interface

Open a browser and navigate to:

```bash
http://<raspberry_pi_ip>:5001/web
```

### 7. API Endpoint

You can also access the image data via the API:

```bash
http://<raspberry_pi_ip>:5001/api/images
```

## Running on Boot (Optional)

To run the app automatically when the Raspberry Pi boots up, you can create a systemd service.

### 1. Create a Systemd Service File

Create a new service file:

```bash
sudo nano /etc/systemd/system/rp4b-app.service
```

Add the following content:
```bash
[Unit]
Description=Vein Detector Flask App
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/your-repo-name
ExecStart=/usr/bin/python3 /home/pi/your-repo-name/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Save and exit (Ctrl + X, then Y).

### 2. Enable and Start the Service

Reload systemd to recognize the new service:

```bash
sudo systemctl daemon-reload
```

Enable the service to start on boot:

```bash
sudo systemctl enable rp4b-app.service
```

Start the service:

```bash
sudo systemctl start rp4b-app.service
```

Check the status of the service:

```bash
sudo systemctl status rp4b-app.service
```

## Troubleshooting

### 1. Externally Managed Environment Error

If you encounter the externally-managed-environment error when installing packages, use a virtual environment:

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

### 2. Port Already in Use

If port 5001 is already in use, change the port in app.py:

```bash
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)  # Change to an available port
```

### 3. Missing Dependencies

If you encounter missing dependencies, install them using apt:

```bash
sudo apt install python3-venv
```

