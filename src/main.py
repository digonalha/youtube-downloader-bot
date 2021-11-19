from yt_dlp import YoutubeDL
from yt_dlp.postprocessor.common import PostProcessor
import os

tmp_dir = "./tmp/"
if not os.path.exists(tmp_dir):
    os.makedirs(tmp_dir)

link = "https://www.youtube.com/watch?v=eB4oFu4BtQ8"


def my_hook(d):
    if d["status"] == "finished":
        print("Done downloading, now converting ...")


ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "progress_hooks": [my_hook],
    "outtmpl": "./tmp/%(title)s.%(ext)s",
}


class MyCustomPP(PostProcessor):
    def run(self, info):
        self.to_screen("Video downloaded! Now converting to .mp3...")
        return [], info


yt_downloader = YoutubeDL(ydl_opts)

with yt_downloader:
    yt_downloader.add_post_processor(MyCustomPP())
    result = yt_downloader.extract_info(link, download=True)


print(result)
