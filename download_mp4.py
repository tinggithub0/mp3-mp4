from pytube import YouTube
url=input("youtube網址: ")

def progress(chunk, file_handle, bytes_remaining):
    contentSize = video.filesize
    size = contentSize - bytes_remaining

    print("\r" + "[Download progress]:[%s%s]%.2f%%;" % (
    "█" * int(size*20/contentSize), " "*(20-int(size*20/contentSize)), float(size/contentSize*100)), end="")


yt = YouTube(url, on_progress_callback=progress)
video = yt.streams.filter(file_extension="mp4").first()
video.download()





###  要mp4 or mp3 code 區  ###
# choice = int(input("要下載mp4請輸入\"4\"，要下載mp3請輸入\"3\": "))
# if choice == 4 :
#     yt = YouTube(url, on_progress_callback=progress)
#     video = yt.streams.filter(file_extension="mp4").first()
#     video.download(
#         output_path=SAVE_PATH, 
#     )
# elif choice == 3 :
#     yt = YouTube(url, on_progress_callback=progress)
#     video = yt.streams.filter(only_audio=True).first()
#     video.download(
#         output_path=SAVE_PATH, 
#     )
# else:
#     print("只能輸入3或4")

