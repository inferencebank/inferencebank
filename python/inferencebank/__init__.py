import os
import requests


class InferenceBank:
    def __init__(self, api_key: str | None = None):
        if api_key:
            self.api_key = api_key
        else:
            self.api_key = os.environ["INFERENCEBANK_API_KEY"]

    def health_check(self):
        return requests.get("https://inferencebank.com/api/health-check").json()
