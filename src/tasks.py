from celery import Celery
import os
import subprocess
from telegram import send_audio, send_video

app = Celery(broker="pyamqp://guest@localhost/")


def create_temp_folder():
    temp_dir = "./temp/"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)


def remove_files_from_temp():
    files = os.listdir("./temp/")
    for file in files:
        os.remove("./temp/" + file)


@app.task()
def download(video_url: str, extract_audio: bool, chat_id: str):
    try:
        create_temp_folder()

        if "youtube" not in video_url:
            raise

        file_format = '-f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b"'

        if extract_audio:
            file_format = '-f "ba" -x --audio-format mp3'

        command = f'yt-dlp {file_format} {video_url} -o "./temp/%(title)s.%(ext)s"'

        subprocess.Popen(command, shell=True).wait()

        files = os.listdir("./temp/")

        if extract_audio:
            send_audio(chat_id, files[0])
        else:
            send_video(chat_id, files[0])

        return "success!"
    except:
        return "failed"
    finally:
        remove_files_from_temp()
