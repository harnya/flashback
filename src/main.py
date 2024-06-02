from fastapi import FastAPI
from app.api.endpoints import users
from app.api.endpoints import memories
from fastapi.staticfiles import StaticFiles
app = FastAPI()

app.include_router(users.router)
app.include_router(memories.router)

app.mount("/", StaticFiles(directory="web", html=True), name="web")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, workers=3)
