"""
Project Settings file
"""
import os

DEFAULT_ROUTE_STR = "/api"

# Mongo configuration
MONGO_MAX_CONNECTIONS = int(os.getenv("MAX_CONNECTIONS_COUNT", "10"))
MONGO_MIN_CONNECTIONS = int(os.getenv("MIN_CONNECTIONS_COUNT", "10"))
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")
MONGO_URI = f"mongodb+srv:/\
    {MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.xlodq.mongodb.net/\
        {MONGO_DB_NAME}?retryWrites=true&w=majority"

# API key to access endpoints
SERVER_KEY = os.getenv("API_KEY")
