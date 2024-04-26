from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from os import getenv




app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)   

@app.get("/")
async def get_index():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    port = int(getenv("PORT",8000))
    uvicorn.run("main:app",host="0.0.0.0",port=port,reload=True)
