"""`backend.tools.google_search` module."""

import os
import json
from typing import Any, Dict

import requests
from requests import RequestException
from smolagents import Tool

class GoogleSearch(Tool):
    name = "google_search"
    description = "Searches Google for a given query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The search query. For example ''"
        },
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.url = "https://google.serper.dev/search"
        self.headers = {
            'X-API-KEY': os.environ["SERPER_API_KEY"],
            'Content-Type': 'application/json'
        }

    def forward(self, query: str) -> str:
        """Executes the Google search."""
        payload = {
            "q": query,
            "num": 10,
        }

        try:
            response = requests.request(
                "POST",
                self.url,
                headers=self.headers,
                data=json.dumps(payload),
                timeout=10,
            )
            response.raise_for_status()
            return response.text
        except RequestException as exc:
            return str(exc)
google_search = GoogleSearch()
