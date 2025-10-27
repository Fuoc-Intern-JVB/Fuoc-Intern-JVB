import uvicorn
from fastapi import FastAPI

from routers import auth, user

app = FastAPI()


@app.get("/ping")
async def ping_pong():
    return {"message": "pong"}


app.include_router(auth.router, tags=["auth"], prefix="/api/v1")
app.include_router(user.router, tags=["user"], prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)