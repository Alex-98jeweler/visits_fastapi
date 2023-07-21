import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient

from src.main import app




async def test_success_resposne(ac: AsyncClient):
    links = {
        'links': ['https://example1.com', 'https://example2.com', 'https://example3.com']
    }
    response = await ac.post('/visited_links', json=links)
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "success", "data": []}

async def test_validation_error_response(ac: AsyncClient):
    links = {
        'links': [1, 2, 3, ]
    }
    response = await ac.post('/visited_links', json=links)
    assert response.status_code == 422


async def test_get_domains(ac: AsyncClient):
    response = await ac.get("/visited_domains")
    json = response.json()
    assert response.status_code == 200
    assert json['status'] == 'success'