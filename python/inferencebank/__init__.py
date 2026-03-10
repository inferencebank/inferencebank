import os
import requests


class InferenceBank:
    def __init__(self, api_key: str | None = None):
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = os.environ["IBP_API_KEY"]

    def health_check(self):
        host = os.environ.get("IBP_HOST", "https://central.inferencebank.ai")
        return requests.get(f"{host}/api/health-check").json()
