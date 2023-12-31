# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = gdfge #int(os.environ.get("APP_ID"))
    API_HASH = "etertert" #os.environ.get("API_HASH")
    BOT_TOKEN = "gdfggdd:AAFp4R_qm2Q-c1HiUsmTPlbhgrhrgherbfggdP59HtkrnO4iM" #os.environ.get("BOT_TOKEN")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-egertert"))
    MONGODB_URL = "mongofdgfdv://sp12313213324bot:spymusiregtewy546351231`32`cbot@cluster0.l4pi5sr.mongodb.net/?retryWgertwetyrites=true&w=majority" #os.environ.get("MONGODB_URL")
    BOT_OWNER = "687601w534534655" #int(os.environ.get("BOT_OWNER"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 10  # 10 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 75
    MAX_TASK_DURATION_EXTRACT = 180 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 69120 * 60  # 3 hours (in seconds)
