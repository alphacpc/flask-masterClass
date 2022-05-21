from flask import Flask, render_template
from pytube import YouTube

link = "https://www.youtube.com/watch?v=te2vKEjRUv0"

app = Flask(__name__)


@app.route('/', methods=["POST"])
def home():

    # yt = YouTube(link)

    # print(yt)
    # print("Title: ",yt.title)
    # print("Number of views: ",yt.views)
    # print("Length of video: ",yt.length,"seconds")
    # print("Liste Streams : ",yt.streams)
    # print("Les audios : ",yt.streams.filter(only_audio=True))
    # print("Les video : ",yt.streams.filter(only_video=True))

    # ys = yt.streams.get_by_itag('18')

    # print("Downloading...")
    # ys.download()
    # print("Download completed!!")

    return render_template('home.html')


if __name__=='__main__':
    app.run(debug=True,port=5000)