from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', result='')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        video_url = request.form['video_url']

        # Download YouTube video
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(file_extension='mp4').first()
        video_stream.download('static/downloads', filename='output')

        result_message = 'Conversion successful! <a href="/static/downloads/output.mp4" download>Download MP4</a>'
    except Exception as e:
        print(e)
        result_message = 'Conversion failed. Please try again later.'

    return render_template('index.html', result=result_message)

if __name__ == '__main__':
    app.run(debug=True)
