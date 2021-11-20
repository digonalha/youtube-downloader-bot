import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
API_URL = f"https://api.telegram.org/bot{API_TOKEN}"


def send_video(chat_id: int, file_name: str):
    data = {"chat_id": chat_id, "title": file_name}

    with open("./temp/" + file_name, "rb") as video_file:
        files = {"video": video_file.read()}

    requests.post(f"{API_URL}/sendVideo", data=data, files=files)


def send_audio(chat_id: int, file_name: str):
    data = {"chat_id": chat_id, "title": file_name}

    with open("./temp/" + file_name, "rb") as audio_file:
        files = {"audio": audio_file.read()}

    requests.post(f"{API_URL}/sendAudio", data=data, files=files)
