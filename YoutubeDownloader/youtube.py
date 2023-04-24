import pytube

def image(link):
    try:
        video = pytube.YouTube(link)
        return video.thumbnail_url
    except:
        return False

def title(link):
    video = pytube.YouTube(link)
    stream = video.streams.first()
    filename = stream.default_filename
    filename = filename[:-5]
    return filename


def video(link, path):
    video = pytube.YouTube(link)
    stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    filename = stream.default_filename
    try:
        stream.download(output_path=path, filename=filename)
        return True
    except:
        return False

def audio(link, path):
    video = pytube.YouTube(link)
    stream = video.streams.filter(only_audio=True).first()
    filename = stream.default_filename
    filename = filename[:-4]
    filename += ".mp3"
    try:
        stream.download(output_path=path, filename=filename)
        return True
    except:
        return False
