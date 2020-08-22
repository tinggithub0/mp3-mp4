from pytube import YouTube
url1=input("youtube網址: ")

def progress(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')


yt = YouTube(url1, on_progress_callback=progress)
video = yt.streams.filter(only_audio=True).first()
video.download()


