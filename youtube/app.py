from flask import Flask, redirect, render_template, request
from pytube import YouTube

# link = "https://youtu.be/Tor_gGi7e0g?list=PLTbQvx84FrASVK-B1S2z2fn16dRbLiNdr"

app = Flask(__name__)

# yt = None

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == 'POST':
        url = request.form.get('inputText')
        yt = YouTube(url)
        image = yt.thumbnail_url
        videos = yt.streams.filter(file_extension='mp4')

        print(yt,"k*****")

        url_test = url.split('?')[1]

        return render_template('home.html', videos = videos, picture = image, title = yt.title, views = yt.views, url = url_test, yt = yt)

    return render_template('home.html')


@app.route('/downloader/<itag>/<url>')
def downloader(itag,url):

    # print(yt)
    print(itag)
    yt = YouTube("https://www.youtube.com/watch?"+url)
    ys = yt.streams.get_by_itag(itag)

    print("Downloading...")
    ys.download()
    # print("Download completed!!")

    return redirect('/')


if __name__=='__main__':
    app.run(debug=True,port=5000)