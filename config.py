# config.py

import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_here")
    MONGODB_SETTINGS = {
        'host': os.getenv("MONGO_URI")
    }
