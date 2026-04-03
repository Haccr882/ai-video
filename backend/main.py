from fastapi import FastAPI
from app.core.database import Base, engine

from app.routes import auth, video, upload, ai, payment

app = FastAPI(title="AI Video SaaS")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(video.router)
app.include_router(upload.router)
app.include_router(ai.router)
app.include_router(payment.router)


@app.get("/")
def root():
    return {"message": "Backend running on Render"}
