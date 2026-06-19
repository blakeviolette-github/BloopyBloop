from openai import OpenAI
import httpx
from .config import OPENAI_API_KEY

class BedtimeStoryEngine:
    def __init__(self):
        # Configure a robust connection pool and higher timeout limit
        # This keeps the server line open even if the cloud network is lagging
        http_client = httpx.Client(
            timeout=httpx.Timeout(60.0, connect=10.0),
            follow_redirects=True
        )
        
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
            http_client=http_client
        )