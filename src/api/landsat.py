import httpx
from datetime import date
class LandsatAPI:
    BASE_URL = 'https://api.nasa.gov/planetary/earth'
    def __init__(self, api_key: str): self.api_key = api_key
    async def get_imagery(self, lat: float, lon: float, date: date) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f'{self.BASE_URL}/imagery', params={'lat': lat, 'lon': lon, 'date': date.isoformat(), 'api_key': self.api_key})
            return resp.json()
    async def get_assets(self, lat: float, lon: float) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f'{self.BASE_URL}/assets', params={'lat': lat, 'lon': lon, 'api_key': self.api_key})
            return resp.json()
