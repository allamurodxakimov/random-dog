from dotenv import load_dotenv
import os

load_dotenv()
def get_token():
    TOKEN = os.getenv("TOKEN")
    if TOKEN is None:
        raise ValueError("TOKEN yo'q")
    return TOKEN