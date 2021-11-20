from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.requests import Request
from tasks import download
import uvicorn


async def download_video(request: Request):
    payload = await request.json()

    download.delay(payload["video_url"], payload["extract_audio"], payload["chat_id"])

    return JSONResponse({"result": "task added on queue"})


routes = [
    Route("/", endpoint=download_video, methods=["POST"]),
]

app = Starlette(
    debug=True,
    routes=routes,
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000)
