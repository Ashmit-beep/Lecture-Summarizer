from pydantic import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "lecture_summarizer"

    class Config:
        env_file = ".env"

settings = Settings()