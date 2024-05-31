from fastapi import FastAPI
from app.api.endpoints import users
from fastapi.staticfiles import StaticFiles
app = FastAPI()
# app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})

app.include_router(users.router)
app.mount("/", StaticFiles(directory="web", html=True), name="web")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True, workers=3)
