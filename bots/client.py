import os
from dotenv import load_dotenv
from binance.client import Client
from bots.logging_config import logger




load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BASE_URL")



def get_client() :
    try:
        logger.info("Creating Binance CLient")

        client = Client(API_KEY , API_SECRET)


        client.FUTURES_URL = BASE_URL + "/fapi"

        logger.info("Connected to future")

        return client
    except Exception as e:
        logger.error(f"Failed to create CLient : {e}")
        raise