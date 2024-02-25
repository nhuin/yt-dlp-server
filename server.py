from flask import Flask, request, send_file
from yt_dlp import YoutubeDL
import json

app = Flask(__name__)

@app.route('/execute', methods=['GET'])
def execute_binary():
    with YoutubeDL({'outtmpl': '/dl/%(title)s-%(id)s.%(ext)s'}) as ydl:
        info = ydl.extract_info(request.args.get("url"))
        print(f"Saving file to {info['requested_downloads'][0]['filename']}")
        return send_file(info['requested_downloads'][0]['filename'])
    return "Error executing yt-dlp"

if __name__ == '__main__':
    app.run(host='0.0.0.0')

