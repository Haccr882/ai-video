import os

class Settings:

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/ai_video_saas"
    )

    JWT_SECRET = os.getenv("JWT_SECRET", "supersecret")

    HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")


settings = Settings()
