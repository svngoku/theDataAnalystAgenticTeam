import os
import sys
from unittest import mock

import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
os.environ.setdefault("SERPER_API_KEY", "test")
from backend.tools.google_search import GoogleSearch

class MockResponse:
    def __init__(self, text: str, status_code: int = 200):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"status {self.status_code}")


def test_google_search_success(monkeypatch):
    def mock_request(method, url, headers=None, data=None, timeout=None):
        return MockResponse("ok")

    monkeypatch.setattr(requests, "request", mock_request)
    tool = GoogleSearch()
    assert tool.forward("test") == "ok"


def test_google_search_error(monkeypatch):
    def mock_request(method, url, headers=None, data=None, timeout=None):
        raise requests.RequestException("boom")

    monkeypatch.setattr(requests, "request", mock_request)
    tool = GoogleSearch()
    result = tool.forward("test")
    assert "boom" in result
