from flask import Flask, request, send_file
from yt_dlp import YoutubeDL
import json

app = Flask(__name__)

@app.route('/execute', methods=['GET'])
def execute_binary():
    with YoutubeDL() as ydl:
        info = ydl.extract_info(request.args.get("url"))
        return send_file(info['requested_downloads'][0]['filename'])
    return "Error executing yt-dlp"

if __name__ == '__main__':
    app.run()

