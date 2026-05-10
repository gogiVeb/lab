from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import uvicorn

app = FastAPI()

html_path = Path(__file__).parent / "templates"
app.mount("/static", StaticFiles(directory=html_path), name="static")

clients = []

@app.get("/")
async def get():
    html = (html_path / "chat.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html, status_code=200)

@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    username: str = Query(default=None)
):
    await websocket.accept()

    if not username or username.strip() == "":
        await websocket.send_text("ОШИБКА: Имя пользователя не указано.")
        await websocket.close(code=1008)
        return

    username = username.strip()
    client_info = {"ws": websocket, "username": username}
    clients.append(client_info)

    join_message = f"🟢 {username} присоединился к чату"
    for client in clients:
        if client["ws"] != websocket:
            await client["ws"].send_text(join_message)

    try:
        while True:
            data = await websocket.receive_text()
            full_message = f"{username}: {data}"
            for client in clients:
                if client["ws"] != websocket:
                    await client["ws"].send_text(full_message)

    except WebSocketDisconnect:
        clients.remove(client_info)
        leave_message = f"🔴 {username} покинул чат"
        for client in clients:
            await client["ws"].send_text(leave_message)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)