from fastapi import FastAPI
from app.api.endpoints import users
from app.api.endpoints import memories
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
    
)

import mangum

app.include_router(users.router)
app.include_router(memories.router)

app.mount("/", StaticFiles(directory="web", html=True), name="web")
# docker build -t memor -f docker/Dockerfile .
# docker run -d --name mycontainer7 -p 8000:8000 memor
handler = mangum.Mangum(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="0.0.0.0", port=8000)
