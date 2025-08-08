from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

client: AsyncIOMotorCleint | None = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(settings.MONGO_URI)
    db = client(settings.DB_NAME)

async def close_mongo_connection():
    global client
    if client:
        client.close()
        