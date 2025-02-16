from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import speedtest
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Serve the frontend files
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# Serve other static files (CSS, JS, etc.)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Speed test endpoint
@app.route('/speedtest', methods=['GET'])
def speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps

    return jsonify({
        'download_speed': round(download_speed, 2),
        'upload_speed': round(upload_speed, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)