"""`backend.tools.jina_rerank` module."""

import os
from typing import Any, Dict

import requests
from requests import RequestException
from smolagents import Tool

class JinaRerank(Tool):
    name = "jina_rerank"
    description = "Reranks documents or links using Jina AI's reranking model."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to rerank documents or links against."
        },
        "documents": {
            "type": "array",
            "description": "List of documents or links to rerank."
        },
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.url = "https://api.jina.ai/v1/rerank"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {os.environ["JINA_API_KEY"]}'
        }

    def forward(self, query: str, documents: list) -> Dict[str, Any]:
        """Executes the Jina AI reranking."""
        payload = {
            "model": "jina-reranker-v2-base-multilingual",
            "query": query,
            "top_n": 3,
            "documents": documents,
        }

        try:
            response = requests.post(
                self.url,
                headers=self.headers,
                json=payload,
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except RequestException as exc:
            return {"error": str(exc)}
    
jina_rerank = JinaRerank()
