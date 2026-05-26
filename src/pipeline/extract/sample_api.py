import requests
from ..config import API_BASE_URL, API_TOKEN

def fetch_events():
    if not API_BASE_URL:
        return [
            {"id": "evt_1", "type": "demo", "timestamp": "2026-05-24T20:00:00Z"},
            {"id": "evt_2", "type": "demo", "timestamp": "2026-05-24T21:00:00Z"},
        ]

    headers = {"Authorization": f"Bearer {API_TOKEN}"} if API_TOKEN else {}
    r = requests.get(f"{API_BASE_URL.rstrip('/')}/events", headers=headers, timeout=30)
    r.raise_for_status